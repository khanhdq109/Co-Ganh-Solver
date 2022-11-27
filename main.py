import timeit

import Minimax
import MCTS

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
    
def saveBoard(board, file):
    with open(file) as f:
        for i in board:
            f.write(str(i) + '\n')
            
def move(board, player, remain_time_x, remain_time_y):
    start = timeit.default_timer()
    
    solver = Minimax.Solver(2, board, player)
    result = solver.minimax()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    if player == 1:
        remain_time_x -= time_step
    else:
        remain_time_y -= time_step
        
    print('Total time: ' + str(time_step) + '\n')
        
    return result

board = readBoard('input.txt')
printBoard(board)

step = move(board, 1, 100, 100)
print(step)