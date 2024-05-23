import bingoUtils
from schemas import Player, Game, Field

def test_check_bingo_false():
    # false
    fields: list[list[Field]] = [[Field(content='', checked=False) for _ in range(3)] for _ in range(3)]
    board: Player = Player(name="name", token_hash="token", fields=fields, has_bingo=False)

    assert not bingoUtils.check_bingo(board)

def test_check_bingo_horizontal():
    fields: list[list[Field]] = [[Field(content='', checked=False) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        fields[0][i].checked = True 

    board: Player = Player(name="name", token_hash="token", fields=fields, has_bingo=False)

    assert bingoUtils.check_bingo(board)

def test_check_bingo_vertical():
    fields: list[list[Field]] = [[Field(content='', checked=False) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        fields[i][0].checked = True 

    board: Player = Player(name="name", token_hash="token", fields=fields, has_bingo=False)

    assert bingoUtils.check_bingo(board)

def test_check_bingo_primary_diagonal():
    fields: list[list[Field]] = [[Field(content='', checked=False) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        fields[i][i].checked = True 

    board: Player = Player(name="name", token_hash="token", fields=fields, has_bingo=False)

    assert bingoUtils.check_bingo(board)

def test_check_bingo_secondary_diagonal():
    fields: list[list[Field]] = [[Field(content='', checked=False) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        fields[i][len(fields)-i-1].checked = True 

    board: Player = Player(name="name", token_hash="token", fields=fields, has_bingo=False)

    assert bingoUtils.check_bingo(board)


def test_check_game_is_complete_true():
    player1: Player = Player(name="player1", token_hash="01", fields=[[Field(content='', checked=False) for _ in range(3)] for _ in range(3)], has_bingo=False)
    player2: Player = Player(name="player2", token_hash="02", fields=[[Field(content='', checked=False) for _ in range(3)] for _ in range(3)], has_bingo=False)
    player3: Player = Player(name="player3", token_hash="03", fields=[[Field(content='', checked=False) for _ in range(3)] for _ in range(3)], has_bingo=False)

    game: Game = Game(
            private=False,
            dimensions=3,
            theme="theme",
            admin_token_hash="admin_token_hash",
            id="id",
            players=[player1, player2, player3],
            game_state="DRAFT"
            )

    assert bingoUtils.check_game_is_complete(game)


def test_check_game_is_complete_false():
    player1: Player = Player(name="player1", token_hash="01", fields=[[Field(content='', checked=False) for _ in range(2)] for _ in range(3)], has_bingo=False)
    player2: Player = Player(name="player2", token_hash="02", fields=[[Field(content='', checked=False) for _ in range(3)] for _ in range(3)], has_bingo=False)
    player3: Player = Player(name="player3", token_hash="03", fields=[[Field(content='', checked=False) for _ in range(3)] for _ in range(3)], has_bingo=False)

    game: Game = Game(
            private=False,
            dimensions=3,
            theme="theme",
            admin_token_hash="admin_token_hash",
            id="id",
            players=[player1, player2, player3],
            game_state="DRAFT"
            )

    assert not bingoUtils.check_game_is_complete(game) 
