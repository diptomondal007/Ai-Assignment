import os
import time


class Move:
    def __init__(self, row, col):
        self.row = row
        self.col = col


player = 'x'
ai = 'o'


def is_move_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return True
    return False


def check_position(board, row, col):
    if board[row][col] == '_':
        return True
    return False


def evaluate(board):
    # checking for row if someone has won
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == ai:
                return +10
            elif board[row][0] == player:
                return -10

    # checking for column if someone has won
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == ai:
                return +10
            elif board[0][col] == player:
                return -10
    # checking for diagonal if someone has won
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == ai:
            return +10
        elif board[0][0] == player:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == ai:
            return +10
        elif board[0][2] == player:
            return -10


def mini_max(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score
    if score == -10:
        return score

    if not is_move_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = ai
                    best = max(best, mini_max(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = min(best, mini_max(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best


def find_best_move(board):
    best_value = -1000
    best_move = Move(-1, -1)
    for i in range(3):
        for j in range(3):
            # Check if cell is empty
            if board[i][j] == '_':
                # Make the move
                board[i][j] = ai
                # compute evaluation function for this move.
                move_val = mini_max(board, 0, False);
                # Undo the move
                board[i][j] = '_';
                if move_val > best_value:
                    best_move.row = i
                    best_move.col = j
                    best_value = move_val
    return best_move


def draw_board(board):
    print(" %c | %c | %c " % (board[0][0], board[0][1], board[0][2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[1][0], board[1][1], board[1][2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[2][0], board[2][1], board[2][2]))
    print("   |   |   ")


if __name__ == "__main__":
    tic_toc_board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    while True:
        draw_board(tic_toc_board)
        val = evaluate(tic_toc_board)
        if val == 10:
            print("====== Ai win ======")
            break
        elif val == -10:
            print("====== You win ======")
            break
        elif (val is not 10 or -10) and is_move_left(tic_toc_board) is False:
            print("====== Draw ======")
            break
        choice = int(input("Enter the position between [1-9]"))
        if choice == 1:
            if check_position(tic_toc_board, 0, 0):
                tic_toc_board[0][0] = player
            else:
                os.system('clear')
                print("sorry the choice is already filled up. try again!")
                continue
        if choice == 2:
            if check_position(tic_toc_board, 0, 1):
                tic_toc_board[0][1] = player
            else:
                os.system('clear')
                print("sorry the choice is already filled up. try again!")
                continue
        if choice == 3:
            if check_position(tic_toc_board, 0, 2):
                tic_toc_board[0][2] = player
            else:
                os.system('clear')
                print("sorry the choice is already filled up. try again!")
                continue
        if choice == 4:
            if check_position(tic_toc_board, 1, 0):
                tic_toc_board[1][0] = player
            else:
                os.system('clear')
                print("sorry the choice is already filled up. try again!")
                continue
        if choice == 5:
            if check_position(tic_toc_board, 1, 1):
                tic_toc_board[1][1] = player
            else:
                os.system('clear')
                print("sorry the choice is already filled up. try again!")
                continue
        if choice == 6:
            if check_position(tic_toc_board, 1, 2):
                tic_toc_board[1][2] = player
            else:
                os.system('clear')
                print("sorry the choice is already filled up. try again!")
                continue
        if choice == 7:
            if check_position(tic_toc_board, 2, 0):
                tic_toc_board[2][0] = player
            else:
                os.system('clear')
                print("sorry the choice is already filled up. try again!")
                continue
        if choice == 8:
            if check_position(tic_toc_board, 2, 1):
                tic_toc_board[2][1] = player
            else:
                os.system('clear')
                print("sorry the choice is already filled up. try again!")
                continue
        if choice == 9:
            if check_position(tic_toc_board, 2, 2):
                print("-------")
                tic_toc_board[2][2] = player
            else:
                os.system('clear')
                print("sorry the choice is already filled up. try again!")
                continue
        os.system('clear')
        draw_board(tic_toc_board)
        if is_move_left(tic_toc_board):
            os.system('clear')
            print("waiting for the ai's move")
            time.sleep(3)
            move = find_best_move(board=tic_toc_board)
            tic_toc_board[move.row][move.col] = ai
        os.system('clear')
