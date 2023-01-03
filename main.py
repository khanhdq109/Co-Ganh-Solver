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
            
def move(prev_board, board, player, remain_time_x, remain_time_o):
    start = timeit.default_timer()
    
    # Use depth = 2 when fighting online with 'random move' bot
    # Use depth >= 4 when fighting offline with another team's bot
    depth = 4
    
    # Using Minimax
    solver = Minimax.Solver(depth, prev_board, board, player)
    result = solver.solv()
    
    # Using MCTS
    """
    threshold = 15
    solver = MCTS.Solver(prev_board, board, player, threshold)
    result = solver.solv()
    """
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    if player == 1:
        remain_time_o -= time_step
    else:
        remain_time_x -= time_step
        
    return result

restart('input.txt')
restart('output.txt')

cg = game.CoGanh()

bot = input('--> Bot(X/O): ')
if bot == 'x' or bot == 'X': player = 'O'
else: player = 'X'
print('\n--> Player(X/O): ' + player)
inp = input('\n--> First(X/O): ')

remain_time_x = 100
remain_time_o = 100

board = None
prev_board = None

while True:
    print('\n================================================\n- TURN: ' + inp)
    
    if inp == 'o' or inp == 'O':
        board = readBoard('input.txt')
        printBoard(board)
        
        if bot == 'o' or bot == 'O':
            step = move(prev_board, board, 1, remain_time_x, remain_time_o)
            print(step)
            start, end = (step[0][0], step[0][1]), (step[1][0], step[1][1])
            prev_board = board
        else:
            pos = input('POSITION: ')
            tmp = [int(x) for x in pos]
            start, end = (tmp[0], tmp[1]), (tmp[2], tmp[3])
            prev_board = None
        
        cg.simple_move(board, start, end)
        
        saveBoard(board, 'output.txt')
        
        if cg.end_game(board):
            break
        
        inp = 'X'
        
    elif inp == 'x' or inp == 'X':
        board = readBoard('output.txt')
        printBoard(board)
        
        if bot == 'x' or bot == 'X':
            step = move(prev_board, board, -1, remain_time_x, remain_time_o)
            print(step)
            start, end = (step[0][0], step[0][1]), (step[1][0], step[1][1])
            prev_board = board
        else:
            pos = input('POSITION: ')
            tmp = [int(x) for x in pos]
            start, end = (tmp[0], tmp[1]), (tmp[2], tmp[3])
            prev_board = None
        
        cg.simple_move(board, start, end)
        
        saveBoard(board, 'input.txt')
        
        if cg.end_game(board):
            break
        
        inp = 'O'
        
    else:
        print("\nEND PROGRAM")
        break