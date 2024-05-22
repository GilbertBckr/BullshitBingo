from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Depends, HTTPException
import schemas
import security

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

with open("view.html", "r") as f:
    html = f.read()


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

class GameManager():
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
        game = self.get_game_throws_error(game_id)

        for player in game.players:
            if player.name == username:
                return False
        return True

    
    def get_game_throws_error(self, game_id: str) -> schemas.Game:
        """Returns the game, throws error if it does not exist"""
        game = self.active_games.get(game_id)
        if game is None:
            raise Exception()
        return game
    
    def join_game(self, game_id: str, create_player_data: schemas.CreatePlayer):
        game: schemas.Game = self.get_game_throws_error(game_id)
        game.players.append(schemas.Player(**create_player_data.model_dump()))


game_manager = GameManager()

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/create-game")
async def create(websocket: WebSocket):
    """Create a game and immediatly connect to it"""
    await manager.connect(websocket)
    try:
        # As this is the create endpoint we require the user to immediatly send the game data before further communication is possible
        create_game_data = await websocket.receive_json()
        # Checking if the data is valid TODO error handling
        validated_create_game_data: schemas.CreateGame = schemas.CreateGame(**create_game_data)
        game: schemas.Game = game_manager.add_game(validated_create_game_data)

        await websocket.send_json(game.model_dump_json())
        while True:
            data = await websocket.receive_json()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"{data}")


    except WebSocketDisconnect:
        print("Admin disconnected")
        # TODO handle case
        pass



@app.websocket("/ws/join-game/{game_id}/{username}")
async def join_game(websocket: WebSocket, game_id: str, username: str, user_id: str = Depends(security.mocked_user_token)):
    await manager.connect(websocket)
    try:
        if not game_manager.can_join_game(game_id):
            raise HTTPException(400, "Can not join game")
        if not game_manager.name_is_available(game_id, username):
            raise HTTPException(400, "Username is not available")
    
        create_player_data = schemas.CreatePlayer(name=username, token_hash=security.get_hash(user_id))
        game_manager.join_game(game_id, create_player_data )
        
        
        
        while True:
            pass

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # TODO handle disconnect case


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"{data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")