from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import main

class CommandHandler:

    def __init__(self, game_manager: 'main.GameManager') -> None:
        self.game_manager = game_manager

    async def handle_command(self, command: str, game_id: str):
        match command:
            case "REFRESH":
                await self.game_manager.broadcast_game_state(game_id)
            case _:
                print(f"command {command=} is not know")
        
