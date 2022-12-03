# move_1() and move_2() function is just two version of move() function
# using Minimax and Monte Carlo Tree Search

# prev_board parameter in both two above function is used for nothing

import sys
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
            e = ''
            if j == 4: e = '\n'
            if board[i][j] != -1:
                print(' ' + str(board[i][j]) + ' ', end = e)
            else:
                print(str(board[i][j]) + ' ', end = e)
    print('')
    
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
            
# Using Minimax
def move_1(prev_board, board, player, remain_time_x, remain_time_y):
    start = timeit.default_timer()
    
    # Use depth = 2 when fighting online with 'random move' bot
    # Use depth >= 4 when fighting offline with another teams's bot
    depth = 4
    
    solver = Minimax.Solver(depth, board, player)
    result = solver.solv()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    print('--> Total time: ' + str(time_step) + '\n')
    if player == 1:
        remain_time_x -= time_step
    else:
        remain_time_y -= time_step
        
    return result

# Using Monte Carlo Tree Search
def move_2(prev_board, board, player, remain_time_x, remain_time_y):
    start = timeit.default_timer()
    
    solver = MCTS.Solver(board, player)
    result = solver.solv()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    print('--> Total time: ' + str(time_step) + '\n')
    if player == 1:
        remain_time_x -= time_step
    else:
        remain_time_y -= time_step
        
    return result

def choose_algorithm(alg):
    alg = alg.lower()
    
    if alg == 'minimax':
        return move_1
    elif alg == 'mcts':
        return move_2
    else:
        print('INVALID! ALGORITHM IS NOT AVAILABLE')
        return

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

algorithm = choose_algorithm(str(sys.argv[1:][0]))

while True:
    print('================================================\n- TURN: ' + inp)
    
    if inp == 'x' or inp == 'X':
        prev_board = []
        board = readBoard('input.txt')
        printBoard(board)
        
        step = algorithm(prev_board, board, 1, remain_time_x, remain_time_y)
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