import game
import Minimax
import MCTS

import random
import time

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
    for i in range(5):
        for j in range(5):
            e = ''
            if j == 4: e = '\n'
            if board[i][j] != -1:
                print(' ' + str(board[i][j]) + ' ', end = e)
            else:
                print(str(board[i][j]) + ' ', end = e)
    print('')
        
def move(board, player, remain_time_x = 100, remain_time_y = 100):
    solver = Minimax.Solver(8, board, player)
    result = solver.solv()
    return result

def test_move(board):
    print(move(board, 1))
    
def test_simple(board):
    cg = game.CoGanh()
    cg.simple_move(board, (3, 1), (2, 2))
    print("\nSECOND BOARD\n")
    printBoard(board)

def test_chan(board):
    cg = game.CoGanh()
    cg.chan(board, -1)
    print("\nSECOND BOARD\n")
    printBoard(board)
    
def test_ganh(board):
    cg = game.CoGanh()
    cg.ganh(board, (2, 2))
    print("\nSECOND BOARD\n")
    printBoard(board)
    
def test_moveGen(board):
    node = game.Node_1(board)
    cg = game.CoGanh()
    result = cg.move_gen(node, (2, 0))
    print("\nGENERATED:\n")
    for gen in result:
        print(gen[1], ", score: ", str(sum(map(sum, gen[0].board))))
        print('\n')

board = readBoard('input.txt')

printBoard(board)
test_move(board)