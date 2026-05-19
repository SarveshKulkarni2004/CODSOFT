# Tic Tac Toe AI using Minimax

import math

board = [" " for i in range(9)]

def show_board():

    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def winner(player):

    win = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for i in win:

        if board[i[0]] == board[i[1]] == board[i[2]] == player:
            return True

    return False

def draw():

    if " " not in board:
        return True

    return False

def minimax(turn):

    if winner("O"):
        return 1

    if winner("X"):
        return -1

    if draw():
        return 0

    if turn == True:

        best = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                if score > best:
                    best = score

        return best

    else:

        best = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                if score < best:
                    best = score

        return best

def computer_move():

    best = -math.inf
    move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best:

                best = score
                move = i

    board[move] = "O"

while True:

    show_board()

    user = int(input("Enter position (1-9) : ")) - 1

    if board[user] == " ":

        board[user] = "X"

    else:

        print("Position already filled")
        continue

    if winner("X"):

        show_board()
        print("You Win")
        break

    if draw():

        show_board()
        print("Match Draw")
        break

    computer_move()

    if winner("O"):

        show_board()
        print("Computer Wins")
        break

    if draw():

        show_board()
        print("Match Draw")
        break
