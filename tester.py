import game
import Minimax

def readBoard(file):
    count = 0
    board = []
    with open(file) as f:
        for line in f:
            board.append([int(x) for x in line.split()])
            count += 1
            if count == 5: break
    return board

def printBoard(board):
    for i in board:
        print(str(i) + '\n')

board = readBoard('input.txt')
print("FIRST BOARD\n")
printBoard(board)

game.chan(board, -1)
print("\SECOND BOARD\n")
printBoard(board)