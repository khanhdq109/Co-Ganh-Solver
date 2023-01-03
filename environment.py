# Environment for bots to interact with each other
import copy
import random
import timeit

import game
import Minimax
import MCTS

def nums(board, player):
    ans = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == player:
                ans += 1
    return ans

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
    for i in range(4, -1, -1):
        for j in range(5):
            e = ''
            if j == 4: e = '\n'
            if board[i][j] == -1:
                print(' X ', end = e)
            elif board[i][j] == 1:
                print(' O ', end = e)
            else:
                print(' - ', end = e)
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
            
def restart(file):
    with open(file, 'w') as f:
        f.write(' 1  1  1  1  1\n')
        f.write(' 1  0  0  0  1\n')
        f.write('-1  0  0  0  1\n')
        f.write('-1  0  0  0 -1\n')
        f.write('-1 -1 -1 -1 -1')
            
# Using Minimax
def move_1(prev_board, board, player, remain_time_x, remain_time_o):
    start = timeit.default_timer()
    
    # Use depth = 2 when fighting online with 'random move' bot
    # Use depth >= 4 when fighting offline with another team's bot
    depth = 4
    solver = Minimax.Solver(depth, prev_board, board, player)
    result = solver.solv()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    if player == 1:
        remain_time_o -= time_step
    else:
        remain_time_x -= time_step
        
    return result

# Using Monte Carlo Tree Search
def move_2(prev_board, board, player, remain_time_x, remain_time_o):
    start = timeit.default_timer()
    
    simu_threshold = 15
    solver = MCTS.Solver(prev_board, board, player, simu_threshold)
    result = solver.solv()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    if player == 1:
        remain_time_o -= time_step
    else:
        remain_time_x -= time_step
        
    return result

# Combine version of minimax and mcts
def move(prev_board, board, player, remain_time_x, remain_time_o):
    start = timeit.default_timer()

    solver = None
    s = nums(board, player)
    rand = random.randint(0, 100)
    
    if (s <= 13 and s >= 3) and rand % 5 == 0:
        print("Using MCTS!\n")
        simu_threshold = 15
        solver = MCTS.Solver(prev_board, board, player, simu_threshold)
    else:
        print("Using Minimax!\n")
        depth = 4
        solver = Minimax.Solver(depth, prev_board, board, player)
        
    result = solver.solv()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    if player == 1:
        remain_time_o -= time_step
    else:
        remain_time_x -= time_step
        
    return result

def choose_algorithm(alg):
    alg = alg.lower()
    
    if alg == 'minimax':
        return move_1
    elif alg == 'mcts':
        return move_2
    elif alg == 'hybrid':
        return move
    else:
        print('INVALID! ALGORITHM IS NOT AVAILABLE')
        return None

restart('input.txt')
restart('output.txt')

cg = game.CoGanh()
inp = input("--> First(X/O): ")

algo1 = input("\n--> Choose algorithm for X: ")
algo2 = input("\n--> Choose algorithm for O: ")
algorithm_1 = choose_algorithm(algo1)
algorithm_2 = choose_algorithm(algo2)

board = None
prev_board = None
remain_time_x = 100
remain_time_o = 100

count = 0
while True:
    count += 1
    print('================================================\n- TURN ' + str(count) + ': ' + inp)
    
    if inp == 'x' or inp == 'X':
        board = readBoard('input.txt')
        
        step = algorithm_1(prev_board, board, -1, remain_time_x, remain_time_o)
        print(step)
        
        prev_board = copy.deepcopy(board)
        start, end = step[0], step[1]
        cg.simple_move(board, start, end)
        
        saveBoard(board, 'output.txt')
        
        if cg.end_game(board):
            break
        
        inp = 'O'
        
        if count == 100:
            print("================================================\n- Reach 100 turns! Game over!\n")
            printBoard(board)
            print('--> X: ' + str(nums(board, -1)) + '\n')
            print('--> O: ' + str(nums(board, 1)) + '\n')
            break
            
    elif inp == 'o' or inp == 'O':
        board = readBoard('output.txt')
        
        step = algorithm_2(prev_board, board, 1, remain_time_x, remain_time_o)
        print(step)
        
        prev_board = copy.deepcopy(board)
        start, end = step[0], step[1]
        cg.simple_move(board, start, end)
        
        saveBoard(board, 'input.txt')
        
        if cg.end_game(board):
            break
        
        inp = 'X'
        
        if count == 100:
            print("================================================\n- Reach 100 turns! Game over!\n")
            printBoard(board)
            print('--> X: ' + str(nums(board, -1)) + '\n')
            print('--> O: ' + str(nums(board, 1)) + '\n')
            break
            
    else:
        print("\nEND PROGRAM")
        break