from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import main


class CommandHandler:

    def __init__(self, game_manager: "main.GameManager") -> None:
        self.game_manager = game_manager

    async def handle_command(self, command: str, game_id: str, logged_in_user_id: str):
        command_splitted: list[str] = command.split(" ")
        match command_splitted[0]:
            case "REFRESH":
                await self.game_manager.broadcast_game_state(game_id)
            case "CHANGE_CELL_CHECKED":
                await self.game_manager.change_cell_checked(" ".join(command_splitted[1:]), logged_in_user_id)
            case "SET_READY":
                await self.game_manager.set_ready(game_id,logged_in_user_id)
            case _:
                print(f"command {command=} is not know")
