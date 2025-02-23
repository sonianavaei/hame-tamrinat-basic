def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                print(" ", end=" | ")
            elif board[i][j] == 1:
                print("\u001b[0m", "\u001b[34;1m", "●", "\u001b[0m", end=" | ", sep="")
            elif board[i][j] == -1:
                print("\u001b[0m", "\u001b[31m", "●", "\u001b[0m", end=" | ", sep="")
        print()
        print("-" * 26)

def apply_move(dictionary1, board):
    player = next(iter(dictionary1))
    played_space = next(iter(dictionary1.values()))

    for i in range(len(board) - 1, -1, -1):  # Loop from bottom to top
        if board[i][played_space] == 0:  # Find the first empty space
            board[i][played_space] = -1 if player == "p1" else 1
            return board  # Return the updated board
    return board  # Return unchanged board if column is full

def check_board(board):
    for i in range(6):
        for j in range(7):
            # Horizontal check
            if j + 3 < 7 and all(board[i][j + k] == 1 for k in range(4)):
                print("Winner is player 2 (1)")
                return True
            if j + 3 < 7 and all(board[i][j + k] == -1 for k in range(4)):
                print("Winner is player 1 (2)")
                return True

            # Vertical check
            if i + 3 < 6 and all(board[i + k][j] == 1 for k in range(4)):
                print("Winner is player 2 (1)")
                return True
            if i + 3 < 6 and all(board[i + k][j] == -1 for k in range(4)):
                print("Winner is player 1 (2)")
                return True

            # Diagonal checks
            if i + 3 < 6 and j + 3 < 7 and all(board[i + k][j + k] == 1 for k in range(4)):
                print("Winner is player 2 (1)")
                return True
            if i + 3 < 6 and j + 3 < 7 and all(board[i + k][j + k] == -1 for k in range(4)):
                print("Winner is player 1 (2)")
                return True
            
            if i + 3 < 6 and j - 3 >= 0 and all(board[i + k][j - k] == 1 for k in range(4)):
                print("Winner is player 2 (1)")
                return True
            if i + 3 < 6 and j - 3 >= 0 and all(board[i + k][j - k] == -1 for k in range(4)):
                print("Winner is player 1 (2)")
                return True

    return False

def get_input1(board):
    dictionary1 = {"p1": int(input("Player 1 (p1) - Enter column (0-6): "))}
    board = apply_move(dictionary1, board)
    print_board(board)
    return check_board(board)

def get_input2(board):
    dictionary2 = {"p2": int(input("Player 2 (p2) - Enter column (0-6): "))}
    board = apply_move(dictionary2, board)
    print_board(board)
    return check_board(board)

def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    print_board(board)
    while True:
        if get_input1(board):
            break
        if get_input2(board):
            break

if __name__ == "__main__":
    main()
