from schemas import Player, Game


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



def check_board_is_complete(game: Game):
    dim = Game.dimensions

    for board in game.boards:
        flatten = [x for row in board.fields for x in row]
        if flatten != dim*dim:
            return False



