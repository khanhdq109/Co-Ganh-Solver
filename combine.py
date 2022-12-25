import copy
import time
import random

import timeit

random.seed(time.time())

class Node_1:
    def __init__(self,
                 board: list,):
        self.board = copy.deepcopy(board)
          
class CoGanh:
    def __init__(self):
        # 2: Initial value, processing
        # 1: can move
        # 0: can't move
        self.moveBoard = []
        
    def getPosition(self, board, player):
        result = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == player:
                    result.append((i, j))
        return result

    # If 0, the chessman at this position can move. Otherwise, it can't
    def cantMove(self, board, position):
        x, y = position[0], position[1]
        
        if self.moveBoard[x][y] == 0:
            return True
        elif self.moveBoard[x][y] == 1:
            return False
        
        # PART I
        if x > 0:
            if board[x - 1][y] == 0: 
                self.moveBoard[x][y] = 1
                return False
        if x < 4:
            if board[x + 1][y] == 0:
                self.moveBoard[x][y] = 1
                return False
        if y > 0:
            if board[x][y - 1] == 0:
                self.moveBoard[x][y] = 1
                return False
        if y < 4:
            if board[x][y + 1] == 0:
                self.moveBoard[x][y] = 1
                return False
        
        if (x + y) % 2 == 0:
            if x > 0 and y > 0:
                if board[x - 1][y - 1] == 0:
                    self.moveBoard[x][y] = 1
                    return False
            if x < 4 and y > 0:
                if board[x + 1][y - 1] == 0:
                    self.moveBoard[x][y] = 1
                    return False
            if x > 0 and y < 4:
                if board[x - 1][y + 1] == 0:
                    self.moveBoard[x][y] = 1
                    return False
            if x < 4 and y < 4:
                if board[x + 1][y + 1] == 0:
                    self.moveBoard[x][y] = 1
                    return 0
        
        # PART II
        player = board[x][y]
        board[x][y] = 2
        result = True
        
        if x > 0:
            if board[x - 1][y] == player:
                result = result and self.cantMove(board, (x - 1, y))
        if x < 4:
            if board[x + 1][y] == player:
                result = result and self.cantMove(board, (x + 1, y))
        if y > 0:
            if board[x][y - 1] == player:
                result = result and self.cantMove(board, (x, y - 1))
        if y < 4:
            if board[x][y + 1] == player:
                result = result and self.cantMove(board, (x, y + 1))
                
        if (x + y) % 2 == 0:
            if x > 0 and y > 0:
                if board[x - 1][y - 1] == player:
                    result = result and self.cantMove(board, (x - 1, y - 1))
            if x < 4 and y > 0:
                if board[x + 1][y - 1] == player:
                    result = result and self.cantMove(board, (x + 1, y - 1))
            if x > 0 and y < 4:
                if board[x - 1][y + 1] == player:
                    result = result and self.cantMove(board, (x - 1, y + 1))
            if x < 4 and y < 4:
                if board[x + 1][y + 1] == player:
                    result = result and self.cantMove(board, (x + 1, y + 1))
            
        if result:
            later = False
            if x > 0 and not later:
                if board[x - 1][y] == 2: later = True
            if x < 4 and not later:
                if board[x + 1][y] == 2: later = True
            if y > 0 and not later:
                if board[x][y - 1] == 2: later = True
            if y < 4 and not later:
                if board[x][y + 1] == 2: later = True
            if (x + y) % 2 == 0:
                if x > 0 and y > 0 and not later:
                    if board[x - 1][y - 1] == 2: later = True
                if x < 4 and y > 0 and not later:
                    if board[x + 1][y - 1] == 2: later = True
                if x > 0 and y < 4 and not later:
                    if board[x - 1][y + 1] == 2: later = True
                if x < 4 and y < 4 and not later:
                    if board[x + 1][y + 1] == 2: later = True
            
            if not later:
                self.moveBoard[x][y] = 0
        else:
            self.moveBoard[x][y] = 1
        
        return result
            
    def ganh(self, board, position, check = []):
        x, y = position[0], position[1]
        player = board[x][y]
        opponent = -1 * board[x][y]
        
        # HORIZONTAL
        if x > 0 and x < 4:
            if board[x - 1][y] == opponent and board[x + 1][y] == opponent:
                board[x - 1][y], board[x + 1][y] = player, player
                check.append(True)
        # VERTICAL
        if y > 0 and y < 4:
            if board[x][y - 1] == opponent and board[x][y + 1] == opponent:
                board[x][y - 1], board[x][y + 1] = player, player
                check.append(True)
        # DIAGONAL
        if ((x + y) % 2 == 0 and (x > 0 and x < 4) and (y > 0 and y < 4)):
            if board[x - 1][y - 1] == opponent and board[x + 1][y + 1] == opponent:
                board[x - 1][y - 1], board[x + 1][y + 1] = player, player
                check.append(True)
            if board[x - 1][y + 1] == opponent and board[x + 1][y - 1] == opponent:
                board[x - 1][y + 1], board[x + 1][y - 1] = player, player
                check.append(True)

    def chan(self, board, player):
        # Init moveBoard
        self.moveBoard = []
        for i in range(5):
            tmp = []
            for j in range(5):
                tmp.append(2)
            self.moveBoard.append(tmp)
        
        pos = self.getPosition(board, player)
        
        # Check which position is "chan"ed
        for p in pos:
            if self.cantMove(board, p):
                board[p[0]][p[1]] = -1 * player
                
            for i in range(5):
                for j in range(5):
                    if board[i][j] == 2:
                        board[i][j] = player
    
    # Return Node_1 and a position
    def move_gen(self, node: Node_1, position: tuple):
        x, y = position[0], position[1]
        player = node.board[x][y]
        opponent = -1 * player
        result = []
            
        # UP
        if x > 0:
            if node.board[x - 1][y] == 0:
                tmp_board = copy.deepcopy(node.board)
                tmp_board[x - 1][y] = copy.deepcopy(player)
                tmp_board[x][y] = 0
                
                # If len(check) > 0, then this move can "ganh"
                check = []
            
                self.ganh(tmp_board, (x - 1, y), check)
                self.chan(tmp_board, opponent)
                    
                tmp = Node_1(tmp_board)
                if len(check) > 0:
                    result.append((tmp, (x - 1, y), True, position))
                else:
                    result.append((tmp, (x - 1, y), False, position))
        # DOWN
        if x < 4:
            if node.board[x + 1][y] == 0:
                tmp_board = copy.deepcopy(node.board)
                tmp_board[x + 1][y] = copy.deepcopy(player)
                tmp_board[x][y] = 0
                
                # If len(check) > 0, then this move can "ganh"
                check = []
                
                self.ganh(tmp_board, (x + 1, y), check)
                self.chan(tmp_board, opponent)
                    
                tmp = Node_1(tmp_board)
                if len(check) > 0:
                    result.append((tmp, (x + 1, y), True, position))
                else:
                    result.append((tmp, (x + 1, y), False, position))
        # LEFT
        if y > 0:
            if node.board[x][y - 1] == 0:
                tmp_board = copy.deepcopy(node.board)
                tmp_board[x][y - 1] = copy.deepcopy(player)
                tmp_board[x][y] = 0
                
                # If len(check) > 0, then this move can "ganh"
                check = []
                
                self.ganh(tmp_board, (x, y - 1), check)
                self.chan(tmp_board, opponent)
                    
                tmp = Node_1(tmp_board)
                if len(check) > 0:
                    result.append((tmp, (x, y - 1), True, position))
                else:
                    result.append((tmp, (x, y - 1), False, position))
        # RIGHT
        if y < 4:
            if node.board[x][y + 1] == 0:
                tmp_board = copy.deepcopy(node.board)
                tmp_board[x][y + 1] = copy.deepcopy(player)
                tmp_board[x][y] = 0
                
                # If len(check) > 0, then this move can "ganh"
                check = []
                
                self.ganh(tmp_board, (x, y + 1), check)
                self.chan(tmp_board, opponent)
                    
                tmp = Node_1(tmp_board)
                if len(check) > 0:
                    result.append((tmp, (x, y + 1), True, position))
                else:
                    result.append((tmp, (x, y + 1), False, position))
                
        # DIAGONAL
        if (x + y) % 2 == 0:
            # UP LEFT
            if x > 0 and y > 0:
                if node.board[x - 1][y - 1] == 0:
                    tmp_board = copy.deepcopy(node.board)
                    tmp_board[x - 1][y - 1] = copy.deepcopy(player)
                    tmp_board[x][y] = 0
                    
                    # If len(check) > 0, then this move can "ganh"
                    check = []
                    
                    self.ganh(tmp_board, (x - 1, y - 1), check)
                    self.chan(tmp_board, opponent)
                        
                    tmp = Node_1(tmp_board)
                    if len(check) > 0:
                        result.append((tmp, (x - 1, y - 1), True, position))
                    else:
                        result.append((tmp, (x - 1, y - 1), False, position))
            # UP RIGHT
            if x > 0 and y < 4:
                if node.board[x - 1][y + 1] == 0:
                    tmp_board = copy.deepcopy(node.board)
                    tmp_board[x - 1][y + 1] = copy.deepcopy(player)
                    tmp_board[x][y] = 0
                    
                    # If len(check) > 0, then this move can "ganh"
                    check = []
                    
                    self.ganh(tmp_board, (x - 1, y + 1), check)
                    self.chan(tmp_board, opponent)
                        
                    tmp = Node_1(tmp_board)
                    if len(check) > 0:
                        result.append((tmp, (x - 1, y + 1), True, position))
                    else:
                        result.append((tmp, (x - 1, y + 1), False, position))
            # DOWN LEFT
            if x < 4 and y > 0:
                if node.board[x + 1][y - 1] == 0:
                    tmp_board = copy.deepcopy(node.board)
                    tmp_board[x + 1][y - 1] = copy.deepcopy(player)
                    tmp_board[x][y] = 0
                    
                    # If len(check) > 0, then this move can "ganh"
                    check = []
                    
                    self.ganh(tmp_board, (x + 1, y - 1), check)
                    self.chan(tmp_board, opponent)
                        
                    tmp = Node_1(tmp_board)
                    if len(check) > 0:
                        result.append((tmp, (x + 1, y - 1), True, position))
                    else:
                        result.append((tmp, (x + 1, y - 1), False, position))
            # DOWN RIGHT
            if x < 4 and y < 4:
                if node.board[x + 1][y + 1] == 0:
                    tmp_board = copy.deepcopy(node.board)
                    tmp_board[x + 1][y + 1] = copy.deepcopy(player)
                    tmp_board[x][y] = 0
                    
                    # If len(check) > 0, then this move can "ganh"
                    check = []
                    
                    self.ganh(tmp_board, (x + 1, y + 1), check)
                    self.chan(tmp_board, opponent)
                        
                    tmp = Node_1(tmp_board)
                    if len(check) > 0:
                        result.append((tmp, (x + 1, y + 1), True, position))
                    else:
                        result.append((tmp, (x + 1, y + 1), False, position))
                    
        return result

    def simple_move(self, board, start, end):
        x0, y0 = start[0], start[1]
        x1, y1 = end[0], end[1]
        
        # Check if it's a valid move
        valid = False
        if (
            x1 >= 0 and x1 < 5 and
            y1 >= 0 and y1 < 5 and
            (
                (x1 == x0 + 1 and y1 == y0) or
                (x1 == x0 - 1 and y1 == y0) or
                (x1 == x0 and y1 == y0 + 1) or
                (x1 == x0 and y1 == y0 -1) or
                ((x0 + y0) % 2 == 0 and
                    (x1 == x0 - 1 and y1 == y0 - 1) or
                    (x1 == x0 + 1 and y1 == y0 - 1) or
                    (x1 == x0 - 1 and y1 == y0 + 1) or
                    (x1 == x0 + 1 and y1 == y0 + 1)
                )
            )
        ):
            valid = True
        
        if not valid:
            print("Invalid move!!!")
            return
        
        board[x1][y1] = board[x0][y0]
        board[x0][y0] = 0
        
        self.ganh(board, end)
        self.chan(board, -1 * board[x1][y1])
        
    def end_game(self, board, notice = True):
        score = sum(map(sum, board))
        if score == 16:
            if notice:
                print("\nO WIN!!!")
            return True
        elif score == -16:
            if notice:
                print("\nX WIN!!!")
            return True
        return False
    
    def X_win(self, board):
        score = sum(map(sum, board))
        if score == -16:
            return True
        return False
    
    def O_win(self, board):
        score = sum(map(sum, board))
        if score == 16:
            return True
        return False
    
class Solver:
    def __init__(self,
                 depth: int = 2,
                 board: list = None,
                 player: int = -1,):
        self.depth = depth
        self.board = copy.deepcopy(board)
        self.player, self.opponent = player, -1 * player
        
        self.start = None
        self.end = None
    
    def evaluate(self, board):
        result = sum(map(sum, board))
        if self.player == -1:
            result *= -1
        return result
    
    def play(self, node, dp, alpha = -100, beta = 100):
        if dp > self.depth:
            return
        
        # LEAF NODE
        if dp == self.depth:
            return self.evaluate(node.board)
        
        g = False
        cg = CoGanh()
        
        # PLAYER
        if dp % 2 == 0:
            successor = []
            pos = cg.getPosition(node.board, self.player)
                
            for p in pos:
                successor += cg.move_gen(node, p)
                
            if len(successor) > 0:
                for s in successor:
                    if s[2]:
                        g = True
                        break
                    
                for s in successor:
                    if g:
                        if not s[2]:
                            continue
                        
                    if self.player == -1:
                        if cg.X_win(s[0].board):
                            if dp == 0:
                                self.start = s[3]
                                self.end = s[1]
                            return 100
                    else:
                        if cg.O_win(s[0].board):
                            if dp == 0:
                                self.start = s[3]
                                self.end = s[1]
                            return 100
                    
                    value = self.play(s[0], dp + 1, alpha, beta)
                    if value > alpha:
                        alpha = value
                        if dp == 0:
                            self.start = s[3]
                            self.end = s[1]
                    if alpha >= beta:
                        return alpha
            return alpha
                            
        # OPPONENT
        else:
            successor = []
            pos = cg.getPosition(node.board, self.opponent)
                
            for p in pos:
                successor += cg.move_gen(node, p)
                
            if len(successor) > 0:
                for s in successor:
                    if s[2]:
                        g = True
                        break
                    
                for s in successor:
                    if g:
                        if not s[2]:
                            continue
                        
                    if self.player == -1:
                        if cg.O_win(s[0].board): 
                            return -100
                    else:
                        if cg.X_win(s[0].board):
                            return -100
                    
                    value = self.play(s[0], dp + 1, alpha, beta)
                    if value < beta:
                        beta = value
                    if beta <= alpha:
                        return beta
            return beta
    
    def solv(self):
        node = Node_1(self.board)
        score = self.play(node, 0)
        x0, y0 = 4 - self.start[0], self.start[1]
        x1, y1 = 4 - self.end[0], self.end[1]
        return ((x0, y0), (x1, y1))
    
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
    solver = Solver(depth, board, player)
    result = solver.solv()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    # print('TIME: ' + str(time_step))
    if player == 1:
        remain_time_o -= time_step
    else:
        remain_time_x -= time_step
        
    return result

restart('input.txt')
restart('output.txt')
cg = CoGanh()
inp = 'X'
remain_time_x = 100
remain_time_o = 100

while True:
    print('================================================\n- TURN: ' + inp)
    
    if inp == 'x' or inp == 'X':
        prev_board = []
        board = readBoard('input.txt')
        printBoard(board)
        
        step = move(prev_board, board, -1, remain_time_x, remain_time_o)
        print(step)
        x0, y0, x1, y1 = 4 - step[0][0], step[0][1], 4 - step[1][0], step[1][1]
        
        start, end = (x0, y0), (x1, y1)
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
        
        start, end = (4 - tmp[0], tmp[1]), (4 - tmp[2], tmp[3])
        cg.simple_move(board, start, end)
        
        saveBoard(board, 'input.txt')
        
        if cg.end_game(board):
            break
        
        inp = 'X'
        
    else:
        print("\nEND PROGRAM")
        break