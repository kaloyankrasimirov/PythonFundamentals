def check_winner(some_board:list, player:int) ->bool:
    winning_row = [player, player, player]
    for row in some_board:
        if row == winning_row:
            return True

    for col_index in range(3):
        element_1 = some_board[0][col_index]
        element_2 = some_board[1][col_index]
        element_3 = some_board[2][col_index]
        if element_1 == element_2 == element_3 == player:
            return True

    if some_board[0][0] == some_board[1][1] == some_board[2][2] == player:
        return True

    if some_board[0][2] == some_board[1][1] == some_board[2][0] == player:
        return True

    return False


first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))

board = [first_row, second_row, third_row]

if check_winner(board, 1):
    print("First player won")
elif check_winner(board, 2):
    print("Second player won")
else:
    print("Draw!")

