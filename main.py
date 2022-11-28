import timeit

import game
import Minimax
import MCTS

def readBoard(file):
    count = 0
    board = []
    with open(file, 'r') as f:
        for line in f:
            board.append([int(x) for x in line.split()])
            count += 1
            if count == 5: break
    return board

def printBoard(board):
    for i in board:
        print(str(i) + '\n')
    
def saveBoard(board, file):
    with open(file, 'w') as f:
        for i in range(5):
            for j in range(5):
                f.write(str(board[i][j]) + ' ')
            f.write('\n')
            
def move(board, player, remain_time_x, remain_time_y):
    start = timeit.default_timer()
    
    solver = Minimax.Solver(4, board, player)
    result = solver.minimax()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    if player == 1:
        remain_time_x -= time_step
    else:
        remain_time_y -= time_step
        
    print('Total time: ' + str(time_step) + '\n')
        
    return result

cg = game.CoGanh()

while True:
    inp = input('TURN: ')
    
    if inp == 'x' or inp == 'X':
        board = readBoard('input.txt')
        
        step = move(board, 1, 100, 100)
        print(step)
        
        start, end = step[0], step[1]
        cg.simple_move(board, start, end)
        
        saveBoard(board, 'output.txt')
        
        if cg.end_game(board):
            break
    elif inp == 'o' or inp == 'O':
        board = readBoard('output.txt')
        
        pos = input('POSITION: ')
        tmp = [int(x) for x in pos]
        
        start, end = (tmp[0], tmp[1]), (tmp[2], tmp[3])
        cg.simple_move(board, start, end)
        
        saveBoard(board, 'input.txt')
        
        if cg.end_game(board):
            break
    else:
        print("\nEND PROGRAM")
        break