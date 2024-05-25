from schemas import Player, Game
import string
import random


def check_bingo(board:Player) -> bool:

    # horizontal 
    for row in board.fields:
        line: list[bool] = list(map(lambda x: x.checked, row))
        if all(line):
            return True

    # vertical 
    for col_index in range(len(board.fields[0])):
        col: list[bool] = [board.fields[row_num][col_index].checked for row_num in range(len(board.fields[col_index]))]
        if all(col):
            return True

    primary_diagonal: list[bool] = [board.fields[i][i].checked for i in range(len(board.fields))]
    if all(primary_diagonal):
        return True
    
    secondary_diagonal: list[bool] = [board.fields[i][len(board.fields)-i-1].checked for i in range(len(board.fields))]
    if all(secondary_diagonal):
        return True

    return False



def check_game_is_complete(game: Game) -> bool:
    dim: int = game.dimensions

    for player in game.players:
        i: int = 0
        for i, row in enumerate(player.fields):
            # horizontal 
            if len(row) != dim:
                return False 

            # check if content is empty
            for field in row:
                if not field.content:
                    return False
            
        # vertical 
        if i != dim-1:
            return False

    return True

def create_id(length: int = 5) -> str:
    alphabet: list[str] = list(string.ascii_uppercase)
    id: str = "" 
    for _ in range(length):
        index: int = random.randint(0, 25)
        id += alphabet[index]
    return id


