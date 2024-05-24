from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Depends, HTTPException
import schemas
import uuid
import security
from typing import Annotated, Any

app = FastAPI()


with open("view.html", "r") as f:
    html = f.read()


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, dict[str, WebSocket]] = {}

    async def save_connection(self, game_id: str, user_id: str, websocket: WebSocket):
        """Saves the websocket for the specified"""
        game_connections: dict[str, WebSocket] | None = self.active_connections.get(
            game_id, None
        )
        if game_connections is None:
            self.active_connections[game_id] = {user_id: websocket}
        else:
            game_connections[user_id] = websocket

    def disconnect(self, user_id: str, game_id: str):
        """Removes the websocket of the specified user from the specified game"""
        self.active_connections[game_id].pop(user_id)

    # async def send_personal_message(self, message: str, websocket: WebSocket):
    # await websocket.send_text(message)

    async def broadcast(self, game_id: str, data: Any):
        """Sends messages to all the active websocket's of a game"""
        sockets = self.active_connections[game_id].values()

        for socket in sockets:
            # TODO optimize parallelization
            await socket.send_json(data)


websocket_manager = ConnectionManager()


class GameManager:
    def __init__(self) -> None:
        self.active_games: dict[str, schemas.Game] = {}

    def add_game(self, create_game_data: schemas.CreateGame) -> schemas.Game:
        """Throws error"""
        # TODO logic for generating game ids
        game = schemas.Game(**create_game_data.model_dump())
        self.active_games[game.id] = game
        return game

    def can_join_game(self, game_id: str) -> bool:
        """Determines if the specified game can be joined"""
        game = self.active_games.get(game_id, None)
        if game is None:
            return False
        return game.game_state == "DRAFT"

    def name_is_available(self, game_id: str, username: str) -> bool:
        # TODO handle reconnect case
        """Checks if the given name is available for the given game, throws error if game is not available"""
        game: schemas.Game = self.get_game_throws_error(game_id)

        for player in game.players:
            if player.name == username:
                return False
        return True

    def get_game_throws_error(self, game_id: str) -> schemas.Game:
        """Returns the game, throws error if it does not exist"""
        game: schemas.Game | None = self.active_games.get(game_id)
        if game is None:
            raise Exception()
        return game

    def join_game(self, game_id: str, create_player_data: schemas.CreatePlayer):
        game: schemas.Game = self.get_game_throws_error(game_id)
        game.players.append(schemas.Player(**create_player_data.model_dump()))

    async def broadcast_game_state(self, game_id: str) -> None:
        game: schemas.Game = self.get_game_throws_error(game_id)
        await websocket_manager.broadcast(game_id, game.model_dump_json())

        pass

    def get_active_games(self) -> list[schemas.Game]:
        return list(self.active_games.values())


game_manager = GameManager()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.get("/active-games", response_model=list[schemas.Game])
async def get_active_games():
    return game_manager.get_active_games()


@app.websocket("/create-game/{username}")
async def create(
    websocket: WebSocket,
    username: str,
    user_id: Annotated[str, Depends(security.get_current_user_id)],
):
    """Create a game and immediately connect to it"""
    await websocket.accept()
    try:
        # As this is the create endpoint we require the user to immediately send the game data before further communication is possible
        create_game_data = await websocket.receive_json()

        # Checking if the data is valid TODO error handling
        validated_create_game_data: schemas.CreateGame = schemas.CreateGame(
            **create_game_data, admin_id=user_id
        )
        game: schemas.Game = game_manager.add_game(validated_create_game_data)

        # Admin needs to join the game as well
        validated_create_player_data = schemas.CreatePlayer(
            name=username, user_id=user_id
        )
        game_manager.join_game(game.id, validated_create_player_data)

        # After creating the game the admin socket is saved and receives the game state
        await websocket_manager.save_connection(
            game_id=game.id, user_id=user_id, websocket=websocket
        )
        await game_manager.broadcast_game_state(game.id)

        while True:
            print("Added admind")
            data = await websocket.receive_json()
            print(data)
            # TODO handle data
            # await websocket_manager.broadcast(f"{data}")

    except WebSocketDisconnect:
        print("Admin disconnected")
        # TODO handle case
        pass


@app.websocket("/ws/join-game/{game_id}/{username}")
async def join_game(
    websocket: WebSocket,
    game_id: str,
    username: str,
    user_id: Annotated[str, Depends(security.get_current_user_id)],
):

    if not game_manager.can_join_game(game_id):
        raise HTTPException(400, "Can not join game")
    if not game_manager.name_is_available(game_id, username):
        raise HTTPException(400, "Username is not available")

    create_player_data = schemas.CreatePlayer(name=username, user_id=user_id)
    game_manager.join_game(game_id, create_player_data)
    await websocket.accept()
    await websocket_manager.save_connection(game_id, user_id, websocket)
    await game_manager.broadcast_game_state(game_id)

    try:
        while True:
            await websocket.receive_json()

    except WebSocketDisconnect:
        websocket_manager.disconnect(user_id, game_id)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    # await websocket_manager.connect(websocket)
    await websocket.accept()
    try:
        while True:
            pass
            # data = await websocket.receive_text()
            # await websocket_manager.send_personal_message(f"You wrote: {data}", websocket)
            # await websocket_manager.broadcast(f"{data}")
    except WebSocketDisconnect:
        pass
        # websocket_manager.disconnect(websocket)
        # await websocket_manager.broadcast(f"Client #{client_id} left the chat")


@app.post("/token")
async def login_for_access_token() -> security.Token:
    user_id = uuid.uuid4()
    access_token = security.create_access_token(data={"sub": str(user_id)})
    return security.Token(access_token=access_token)


@app.get("/users/me/", response_model=str)
async def read_users_me(
    current_user: Annotated[str, Depends(security.get_current_user_id)],
):
    return current_user
