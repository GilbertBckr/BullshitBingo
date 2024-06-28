from . import ConnectionManager
from . import schemas
from .utils import bingoUtils as bingoUtils


class GameManager:
    def __init__(self, websocket_manager: ConnectionManager.ConnectionManager) -> None:
        self.active_games: dict[str, schemas.Game] = {}
        self.websocket_manager = websocket_manager

    def add_game(self, create_game_data: schemas.CreateGame) -> schemas.Game:
        """Throws error"""
        game = schemas.Game(**create_game_data.model_dump(), id=self.generate_id())
        self.active_games[game.id] = game
        return game

    async def set_ready(self, game_id: str, current_user_id: str) -> None:
        game: schemas.Game = self.get_game_throws_error(game_id)

        for player in game.players:
            if player.user_id == current_user_id and bingoUtils.check_board_is_complete(player):
                player.is_ready = True
                break

        await self.websocket_manager.broadcast(game_id, game.model_dump_json())

    def generate_id(self) -> str:
        while True:
            id: str = bingoUtils.create_id()
            if id in self.active_games:
                pass

            return id

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
            raise Exception("Game does not exist")
        return game

    def join_game(self, game_id: str, create_player_data: schemas.CreatePlayer):
        game: schemas.Game = self.get_game_throws_error(game_id)
        game.players.append(
            schemas.Player(
                **create_player_data.model_dump(),
                fields=[
                    [
                        schemas.Field(checked=False, content="")
                        for _ in range(game.dimensions)
                    ]
                    for _ in range(game.dimensions)
                ],
            )
        )

    async def change_cell_checked(self, payload: str, current_user_id: str) -> None:
        """Checks if the call is valid and changes the cell"""
        validated_payload: schemas.ChangeCellCheckedPayload = (
            schemas.ChangeCellCheckedPayload.model_validate_json(payload)
        )
        if current_user_id != validated_payload.user_id:
            print("Attempted to change field did not belong to user")
            return

        game: schemas.Game = self.get_game_throws_error(validated_payload.game_id)
        choosen_player = None
        for player in game.players:
            if player.user_id == validated_payload.user_id:
                choosen_player = player
                break
        if choosen_player is None:
            raise Exception(f"Player ${validated_payload.user_id} not found")
        field: schemas.Field = choosen_player.fields[validated_payload.row][
            validated_payload.col
        ]

        field.checked = validated_payload.new_checked

        choosen_player.has_bingo = bingoUtils.check_bingo(choosen_player)

        await self.broadcast_game_state(validated_payload.game_id)

    async def broadcast_game_state(self, game_id: str) -> None:
        game: schemas.Game = self.get_game_throws_error(game_id)
        print(f"{game.model_dump_json()=}")
        await self.websocket_manager.broadcast(game_id, game.model_dump_json())
        print("braodcasting game state")

    def get_active_games(self) -> list[schemas.Game]:
        games: dict[str, schemas.Game] = {
            k: v
            for k, v in self.active_games.items()
            if not v.private and v.game_state == "DRAFT"
        }
        return list(games.values())

    async def change_cell_text(self, payload: str, current_user_id: str) -> None:
        validated_payload: schemas.ChangeCellTextPayload = (
            schemas.ChangeCellTextPayload.model_validate_json(payload)
        )
        if current_user_id != validated_payload.user_id:
            print("Attempted to change field did not belong to user")
            return

        game: schemas.Game = self.get_game_throws_error(validated_payload.game_id)
        choosen_player = None
        for player in game.players:
            if player.user_id == validated_payload.user_id:
                choosen_player = player
                break
        if choosen_player is None:
            raise Exception(f"Player ${validated_payload.user_id} not found")
        field: schemas.Field = choosen_player.fields[validated_payload.row][
            validated_payload.col
        ]

        # TODO check if text can be changed
        field.content = validated_payload.new_text

        await self.broadcast_game_state(validated_payload.game_id)

    async def start_game(self, payload: str, current_user_id: str) -> None:
        game: schemas.Game = self.get_game_throws_error(payload)

        if game.admin_id != current_user_id:
            print("user is not admin")
            return

        for player in game.players:
            if not player.is_ready:
                return

        game.game_state = "RUNNING"
        print(f"Changed game state {payload=}")
        print(f"{game.game_state=}")
        await self.broadcast_game_state(payload)