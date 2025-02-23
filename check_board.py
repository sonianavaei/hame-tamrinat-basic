def check_board(a):
    for i in range(6):
        for j in range(7):
            sliced_list1 = []
            sliced_list2 = []
            sliced_list3 = []
            sliced_list4 = []

            for k in range(4):
                if j + k < 7:
                    sliced_list1.append(a[i][j + k])
                if i + k < 6:
                    sliced_list2.append(a[i + k][j])
                if i + k < 6 and j - k >= 0:
                    sliced_list3.append(a[i + k][j - k])
                if i + k < 6 and j + k < 7:
                    sliced_list4.append(a[i + k][j + k])

            for sliced_list in [sliced_list1, sliced_list2, sliced_list3, sliced_list4]:
                if len(sliced_list) == 4 and all(x == 1 for x in sliced_list):
                    print("Winner is player 2 (1)")
                    return True
                elif len(sliced_list) == 4 and all(x == -1 for x in sliced_list):
                    print("Winner is player 1 (2)")
                    return True

    return False

# قسمت main
from apply_move import *
from print_board import *
from check_board import *

board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

def get_input1(board):
    dictionary1 = {"p1": -1}
    board = apply_move(dictionary1, board)
    print_board(board)
    return check_board(board)

def get_input2(board):
    dictionary2 = {"p2": 1}
    board = apply_move(dictionary2, board)
    print_board(board)
    return check_board(board)

def main():
    print_board(board)
    while True:
        if get_input1(board):
            break
        if get_input2(board):
            break

main()
def apply_move(dictionary1, board):
    player = next(iter(dictionary1))
    played_space = next(iter(dictionary1.values()))

    for i in range(len(board) - 1, -1, -1):  
        if board[i][played_space] == 0:  
            if player == "p1":
                board[i][played_space] = -1
            elif player == "p2":
                board[i][played_space] = 1
            return board 
   