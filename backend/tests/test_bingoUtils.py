from ..schemas import Player, Game, Field
from typing import Final

import utils.bingoUtils as bingoUtils


DIM: Final[int] = 3


def create_player(content: str="", checked=False) -> Player:
    fields: list[list[Field]] = [
        [Field(content=content, checked=checked) for _ in range(DIM)] for _ in range(DIM)
    ]

    player: Player = Player(name="", user_id="token", fields=fields, has_bingo=False)

    return player 


def test_check_bingo_false():
    board: Player = create_player()

    assert not bingoUtils.check_bingo(board)


def test_check_bingo_horizontal():

    board: Player = create_player()
    for i in range(3):
        board.fields[0][i].checked = True



    assert bingoUtils.check_bingo(board)


def test_check_bingo_vertical():
    board: Player = create_player()
    for i in range(DIM):
        board.fields[i][0].checked = True

    assert bingoUtils.check_bingo(board)


def test_check_bingo_primary_diagonal():
    board: Player = create_player()
    for i in range(DIM):
        board.fields[i][i].checked = True

    assert bingoUtils.check_bingo(board)


def test_check_bingo_secondary_diagonal():
    board: Player = create_player()

    for i in range(3):
        board.fields[i][len(board.fields) - i - 1].checked = True

    assert bingoUtils.check_bingo(board)


def test_check_game_is_complete_true():

    player1: Player = create_player(content="test")
    player2: Player = create_player(content="test")
    player3: Player = create_player(content="test")

    game: Game = Game(
        private=False,
        dimensions=DIM,
        theme="theme",
        admin_id="admin_token",
        id="id",
        players=[player1, player2, player3],
        game_state="DRAFT",
    )

    assert bingoUtils.check_game_is_complete(game)


def test_check_game_is_complete_false():
    player1: Player = create_player()
    player2: Player = create_player()
    player3: Player = create_player()

    game: Game = Game(
        private=False,
        dimensions=3,
        theme="theme",
        admin_id="admin_token_hash",
        id="id",
        players=[player1, player2, player3],
        game_state="DRAFT",
    )

    assert not bingoUtils.check_game_is_complete(game)
