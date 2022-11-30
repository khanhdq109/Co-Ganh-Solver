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
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:
                print(' ' + str(board[i][j]) + ' ', end = '')
            else:
                print(str(board[i][j]) + ' ', end = '')
        print('\n')
    
def saveBoard(board, file):
    with open(file, 'w') as f:
        for i in range(5):
            for j in range(5):
                if board[i][j] != -1:
                    f.write(' ' + str(board[i][j]) + ' ')
                else:
                    f.write(str(board[i][j]) + ' ')
            f.write('\n')
            
def nums(board, player):
    ans = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == player:
                ans += 1
    return ans
            
def move(prev_board, board, player, remain_time_x, remain_time_y):
    start = timeit.default_timer()
    
    # Using prev_board for nothing
    
    # Use depth = 2 when fighting online with 'random move' bot
    # Use depth >= 4 when fighting offline with another teams's bot
    depth = 4
    
    solver = Minimax.Solver(depth, board, player)
    result = solver.minimax()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    print('--> Total time: ' + str(time_step) + '\n')
    if player == 1:
        remain_time_x -= time_step
    else:
        remain_time_y -= time_step
        
    return result

def restart():
    with open('input.txt', 'w') as f:
        f.write(' 1  1  1  1  1\n')
        f.write(' 1  0  0  0  1\n')
        f.write('-1  0  0  0  1\n')
        f.write('-1  0  0  0 -1\n')
        f.write('-1 -1 -1 -1 -1')

restart()
cg = game.CoGanh()
inp = 'X'
remain_time_x = 100
remain_time_y = 100

while True:
    print('================================================\n- TURN: ' + inp)
    
    if inp == 'x' or inp == 'X':
        board = readBoard('input.txt')
        prev_board = []
        printBoard(board)
        
        step = move(prev_board, board, 1, remain_time_x, remain_time_y)
        print(step)
        
        start, end = step[0], step[1]
        cg.simple_move(board, start, end)
        
        saveBoard(board, 'output.txt')
        
        if cg.end_game(board):
            break
        
        inp = 'O'
    elif inp == 'o' or inp == 'O':
        board = readBoard('output.txt')
        printBoard(board)
        
        pos = input('POSITION: ')
        tmp = [int(x) for x in pos]
        
        start, end = (tmp[0], tmp[1]), (tmp[2], tmp[3])
        cg.simple_move(board, start, end)
        
        saveBoard(board, 'input.txt')
        
        if cg.end_game(board):
            break
        
        inp = 'X'
    else:
        print("\nEND PROGRAM")
        break