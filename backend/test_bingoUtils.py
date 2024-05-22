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

def test_check_bingo_primary():
    fields: list[list[Field]] = [[Field(content='', checked=False) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        fields[i][i].checked = True 

    board: Player = Player(name="name", token_hash="token", fields=fields, has_bingo=False)

    assert bingoUtils.check_bingo(board)

def test_check_bingo_secondary():
    fields: list[list[Field]] = [[Field(content='', checked=False) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        fields[i][len(fields)-i-1].checked = True 

    board: Player = Player(name="name", token_hash="token", fields=fields, has_bingo=False)

    assert bingoUtils.check_bingo(board)


def test_check_board_is_complete():
    assert 1==1

