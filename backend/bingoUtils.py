from schemas import Player


def check_bingo(board:Player) -> bool:
    for row in board.fields:
        line: list[bool] = list(map(lambda x: x.checked, row))
        if all(line):
            return True


    for col_index in range(len(board.fields[0])):
        col: list[bool] = [board.fields[col_index][row_num].checked for row_num in range(len(board.fields[0]))]
        if all(col):
            return True

    primary_diagonal: list[bool] = [board.fields[i][i].checked for i in range(len(board.fields))]
    if all(primary_diagonal):
        return True
    
    secondary_diagonal: list[bool] = [board.fields[i][len(board.fields)-i-1].checked for i in range(len(board.fields))]
    if all(secondary_diagonal):
        return True

    return False
