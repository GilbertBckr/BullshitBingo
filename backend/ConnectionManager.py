from fastapi import WebSocket


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

    async def broadcast(self, game_id: str, data: str):
        """Sends messages to all the active websocket's of a game"""
        sockets = self.active_connections[game_id].values()

        for socket in sockets:
            # TODO optimize parallelization
            try:
                await socket.send_text(data)
            except:
                pass