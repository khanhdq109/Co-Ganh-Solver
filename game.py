import copy

class Node:
    def __init__(self,
                 board: list,
                 parents: 'Node' = None,):
        self.board = copy.deepcopy(board)
        self.parents = parents
        
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
    
    # Return Node and a position
    def move_gen(self, node, position):
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
                    
                tmp = Node(tmp_board, node)
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
                    
                tmp = Node(tmp_board, node)
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
                    
                tmp = Node(tmp_board, node)
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
                    
                tmp = Node(tmp_board, node)
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
                        
                    tmp = Node(tmp_board, node)
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
                        
                    tmp = Node(tmp_board, node)
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
                        
                    tmp = Node(tmp_board, node)
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
                        
                    tmp = Node(tmp_board, node)
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
        
    def end_game(self, board):
        score = sum(map(sum, board))
        if score == 16:
            print("\nX WIN!!!")
            return True
        elif score == -16:
            print("\nO WIN!!!")
            return True
        return False
    
    def X_win(self, board):
        score = sum(map(sum, board))
        if score == 16:
            return True
        return False
    
    def O_win(self, board):
        score = sum(map(sum, board))
        if score == -16:
            return True
        return False
    
    def nums(self, board, player):
        ans = 0
        for i in range(5):
            for i in range(5):
                if board[i][j] == player:
                    ans += 1
        return ans