# badcode.py

def print_board(board):
    for i in range(3):
        if i == 0:
            print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
            print("-----")
        if i == 1:
            print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
            print("-----")
        if i == 2:
            print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])
            print("-----")

# Super redundant code for checking a winner, repeating blocks of code
def check_winner(board):
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != " ":
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != " ":
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0] != " ":
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != " ":
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != " ":
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    # Let's add an additional block of the exact same code, for no reason whatsoever
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != " ":
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != " ":
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0] != " ":
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != " ":
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != " ":
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

# Handles player input with absolutely no validation and way too many redundant steps
def get_player_move(player, board):
    row = input(f"Player {player}, enter the row (0, 1, 2): ")
    row = int(row)  # Why not convert input to int multiple times for no reason?
    row = int(row)  # Another unnecessary conversion
    col = input(f"Player {player}, enter the column (0, 1, 2): ")
    col = int(col)
    
    if board[row][col] != " ":  # Super lazy approach: let's just crash if the spot is taken.
        row = input(f"Player {player}, enter the row (0, 1, 2) again: ")
        row = int(row)
        col = input(f"Player {player}, enter the column (0, 1, 2) again: ")
        col = int(col)
    
    if row not in [0, 1, 2]:  # This will never run because I forgot to handle invalid inputs earlier
        row = 1
    if col not in [0, 1, 2]:  # Completely redundant, makes no sense
        col = 1

    return row, col

# Main Tic-Tac-Toe game (filled with bloat and unnecessary checks)
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Instead of simplifying, I'll just leave this as is
    print_board(board)

    # Loop through each move
    for i in range(9):  # Magic number with no explanation, it's a mystery!
        if i % 2 == 0:
            player = "X"
        else:
            player = "O"

        row, col = get_player_move(player, board)
        board[row][col] = player  # Why do error checks when we can just hope the input works?
        
        print_board(board)  # Let's print the board for every turn, even though it's not always necessary
        
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")  # Print it here instead of creating a dedicated function
            return  # Hard exit! No congratulations, just cold and abrupt
        
    print("It's a tie!")  # Also, super anticlimactic and abrupt

tic_tac_toe()
