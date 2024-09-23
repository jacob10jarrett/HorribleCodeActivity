# goodcode.py

# Prints the Tic-Tac-Toe board (Single Responsibility)
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


# Checks for a winner (DRY Code, Single Responsibility)
def check_winner(board):
    winning_combinations = [
        [board[0][0], board[0][1], board[0][2]],  # rows
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],  # columns
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],  # diagonals
        [board[0][2], board[1][1], board[2][0]]
    ]
    for combo in winning_combinations:
        if combo[0] == combo[1] == combo[2] != " ":
            return combo[0]
    return None


# Handles player input with validation (Single Responsibility)
def get_player_move(player, board):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, 2): "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter values between 0 and 2.")
            elif board[row][col] != " ":
                print("This position is already taken. Choose another.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Please enter numeric values.")


# Main Tic-Tac-Toe game (KISS, DRY, Single Responsibility)
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    for i in range(9):
        player = "X" if i % 2 == 0 else "O"

        row, col = get_player_move(player, board)
        board[row][col] = player

        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            return

    print("It's a tie!")


tic_tac_toe()
