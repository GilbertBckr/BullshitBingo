from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi import Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

from . import ConnectionManager
from . import GameManager
from . import schemas
import uuid
from . import security
from .utils import bingoUtils as bingoUtils
from . import command_handler

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])



connection_manager = ConnectionManager.ConnectionManager()

game_manager = GameManager.GameManager(connection_manager)

command_handler_instance = command_handler.CommandHandler(game_manager)




@app.get("/active-games", response_model=list[schemas.Game])
async def get_active_games():
    return game_manager.get_active_games()


@app.websocket("/create-game/{username}")
async def create(
    websocket: WebSocket,
    username: str,
):
    """Create a game and immediately connect to it"""
    await websocket.accept()

    token = await websocket.receive_text()
    user_id = security.get_current_user_id(token)
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
        print(f"{game=}")
        game_manager.join_game(game.id, validated_create_player_data)

        # After creating the game the admin socket is saved and receives the game state
        await connection_manager.save_connection(
            game_id=game.id, user_id=user_id, websocket=websocket
        )
        await game_manager.broadcast_game_state(game.id)

        while True:
            print("Added admind")
            command: str = await websocket.receive_text()
            await command_handler_instance.handle_command(command, game.id, user_id)

    except WebSocketDisconnect:
        print("Admin disconnected")
        # TODO handle case
        pass


@app.websocket("/join-game/{game_id}/{username}")
async def join_game(
    websocket: WebSocket,
    game_id: str,
    username: str,
):

    if not game_manager.can_join_game(game_id):
        raise HTTPException(400, "Can not join game")
    if not game_manager.name_is_available(game_id, username):
        raise HTTPException(400, "Username is not available")

    await websocket.accept()
    token: str = await websocket.receive_text()
    user_id: str = security.get_current_user_id(token)

    create_player_data: schemas.CreatePlayer = schemas.CreatePlayer(
        name=username, user_id=user_id
    )
    game_manager.join_game(game_id, create_player_data)
    await connection_manager.save_connection(game_id, user_id, websocket)
    await game_manager.broadcast_game_state(game_id)

    try:
        while True:
            command: str = await websocket.receive_text()
            await command_handler_instance.handle_command(command, game_id, user_id)

    except WebSocketDisconnect:
        connection_manager.disconnect(user_id, game_id)


@app.post("/token")
async def login_for_access_token() -> security.Token:
    user_id = uuid.uuid4()
    access_token = security.create_access_token(data={"sub": str(user_id)})
    return security.Token(access_token=access_token, user_id=str(user_id))


@app.get("/users/me/", response_model=str)
async def read_users_me(
    current_user: Annotated[str, Depends(security.get_current_user_id)],
):
    return current_user
