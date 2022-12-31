import copy
import time
import random

import timeit

class Node_1:
    def __init__(self,
                 board: list,
                 prev_board: list = None,):
        self.board = copy.deepcopy(board)
        self.prev_board = copy.deepcopy(prev_board)
          
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
    
    def checkTrap(self, prev_board, board, opponent):
        x, y = 0, 0
        
        for i in range(5):
            for j in range(5):
                if prev_board[i][j] == opponent and board[i][j] == 0:
                    x, y = i, j
                    break
        isTrap = False
        
        # HORIZONTAL
        if x > 0 and x < 4:
            if board[x - 1][y] == opponent and board[x + 1][y] == opponent:
                isTrap = True
        # VERTICAL
        if y > 0 and y < 4:
            if board[x][y - 1] == opponent and board[x][y + 1] == opponent:
                isTrap = True
        # DIAGONAL
        if ((x + y) % 2 == 0 and (x > 0 and x < 4) and (y > 0 and y < 4)):
            if board[x - 1][y - 1] == opponent and board[x + 1][y + 1] == opponent:
                isTrap = True
            if board[x - 1][y + 1] == opponent and board[x + 1][y - 1] == opponent:
                isTrap = True
        
        if isTrap:
            return (x, y)
        return None

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
                    return False
        
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
    def move_gen(self, node: Node_1, position: tuple, trap):
        x, y = position[0], position[1]
        player = node.board[x][y]
        opponent = -1 * player
        result = []
        
        if trap != None:
            x1, y1 = trap[0], trap[1]
            if (
                    (x1 == x + 1 and y1 == y) or
                    (x1 == x - 1 and y1 == y) or
                    (x1 == x and y1 == y + 1) or
                    (x1 == x and y1 == y - 1) or
                    ((x + y) % 2 == 0 and
                        (
                            (x1 == x - 1 and y1 == y - 1) or
                            (x1 == x + 1 and y1 == y - 1) or
                            (x1 == x - 1 and y1 == y + 1) or
                            (x1 == x + 1 and y1 == y + 1)
                        )
                    )
            ):
                tmp_board = copy.deepcopy(node.board)
                tmp_board[x1][y1] = copy.deepcopy(player)
                tmp_board[x][y] = 0
                
                self.ganh(tmp_board, (x1, y1))
                self.chan(tmp_board, opponent)
                
                tmp = Node_1(tmp_board, node.board)
                result.append(((tmp, (x1, y1), True, position, True)))
                
                return result

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
                    
                tmp = Node_1(tmp_board, node.board)
                if len(check) > 0:
                    result.append((tmp, (x - 1, y), True, position, False))
                else:
                    result.append((tmp, (x - 1, y), False, position, False))
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
                    
                tmp = Node_1(tmp_board, node.board)
                if len(check) > 0:
                    result.append((tmp, (x + 1, y), True, position, False))
                else:
                    result.append((tmp, (x + 1, y), False, position, False))
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
                    
                tmp = Node_1(tmp_board, node.board)
                if len(check) > 0:
                    result.append((tmp, (x, y - 1), True, position, False))
                else:
                    result.append((tmp, (x, y - 1), False, position, False))
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
                    
                tmp = Node_1(tmp_board, node.board)
                if len(check) > 0:
                    result.append((tmp, (x, y + 1), True, position, False))
                else:
                    result.append((tmp, (x, y + 1), False, position, False))
                
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
                        
                    tmp = Node_1(tmp_board, node.board)
                    if len(check) > 0:
                        result.append((tmp, (x - 1, y - 1), True, position, False))
                    else:
                        result.append((tmp, (x - 1, y - 1), False, position, False))
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
                        
                    tmp = Node_1(tmp_board, node.board)
                    if len(check) > 0:
                        result.append((tmp, (x - 1, y + 1), True, position, False))
                    else:
                        result.append((tmp, (x - 1, y + 1), False, position, False))
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
                        
                    tmp = Node_1(tmp_board, node.board)
                    if len(check) > 0:
                        result.append((tmp, (x + 1, y - 1), True, position, False))
                    else:
                        result.append((tmp, (x + 1, y - 1), False, position, False))
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
                        
                    tmp = Node_1(tmp_board, node.board)
                    if len(check) > 0:
                        result.append((tmp, (x + 1, y + 1), True, position, False))
                    else:
                        result.append((tmp, (x + 1, y + 1), False, position, False))
                    
        return result

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
                 prev_board: list = None,
                 board: list = None,
                 player: int = -1,):
        self.depth = depth
        self.prev_board = copy.deepcopy(prev_board)
        self.board = copy.deepcopy(board)
        self.player = player
        self.opponent = -1 * player
        
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
            trap = None
            if node.prev_board != None:
                trap = cg.checkTrap(node.prev_board, node.board, self.opponent)
            
            successor = []
            pos = cg.getPosition(node.board, self.player)
                    
            for p in pos:
                ans = cg.move_gen(node, p, trap)
                if ans != None:
                    successor += cg.move_gen(node, p, trap)
                
            isTrapped = False
            if len(successor) > 0:
                for s in successor:
                    if s[4]:
                        isTrapped = True
                        g = True
                        break
                if not isTrapped:
                    for s in successor:
                        if s[2]:
                            g = True
                            break
                    
                for s in successor:
                    if g:
                        if not s[2]:
                            continue
                    
                    if isTrapped:
                        if not s[4]:
                            continue
                        
                    if self.player == -1:
                        if cg.X_win(s[0].board):
                            if dp == 0:
                                self.start = s[3]
                                self.end = s[1]
                            return 75
                    else:
                        if cg.O_win(s[0].board):
                            if dp == 0:
                                self.start = s[3]
                                self.end = s[1]
                            return 75
                    
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
            trap = None
            if node.prev_board != None:
                trap = cg.checkTrap(node.prev_board, node.board, self.player)
            
            successor = []
            pos = cg.getPosition(node.board, self.opponent)
                
            for p in pos:
                ans = cg.move_gen(node, p, trap)
                if ans != None:
                    successor += cg.move_gen(node, p, trap)
                
            isTrapped = False
            if len(successor) > 0:
                for s in successor:
                    if s[4]:
                        isTrapped = True
                        g = True
                        break
                if not isTrapped:
                    for s in successor:
                        if s[2]:
                            g = True
                            break
                    
                for s in successor:
                    if g:
                        if not s[2]:
                            continue
                        
                    if isTrapped:
                        if not s[4]:
                            continue
                        
                    if self.player == -1:
                        if cg.O_win(s[0].board): 
                            return -50
                    else:
                        if cg.X_win(s[0].board):
                            return -50
                    
                    value = self.play(s[0], dp + 1, alpha, beta)
                    if value < beta:
                        beta = value
                    if beta <= alpha:
                        return beta
            return beta
    
    def solv(self):
        node = Node_1(self.board, self.prev_board)
        score = self.play(node, 0)
        if self.start == None or self.end == None:
            return None
        return (self.start, self.end)

def move(prev_board, board, player, remain_time_x, remain_time_o):
    start = timeit.default_timer()
    
    # Use depth = 2 when fighting online with 'random move' bot
    # Use depth >= 4 when fighting offline with another team's bot
    depth = 5
    
    # Using Minimax
    solver = Solver(depth, prev_board, board, player)
    result = solver.solv()
    
    stop = timeit.default_timer()
    
    time_step = stop - start
    if player == 1:
        remain_time_o -= time_step
    else:
        remain_time_x -= time_step
        
    return result