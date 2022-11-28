import copy

# 2: Initial value, processing
# 1: can move
# 0: can't move
moveBoard = []

class Node:
    def __init__(self,
                 board: list,
                 parents: 'Node' = None,):
        self.board = copy.deepcopy(board)
        self.parents = parents
        
def getPosition(board, player):
    result = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == player:
                result.append((i, j))
    return result
        
# If False, the chessman at this position can move. Otherwise, it can't
def cantMove(board, position):
    x, y = position[0], position[1]
    
    if moveBoard[x][y] == 0:
        return True
    elif moveBoard[x][y] == 1:
        return False
    
    # PART I
    if x > 0:
        if board[x - 1][y] == 0: 
            moveBoard[x][y] = 1
            return False
    if x < 4:
        if board[x + 1][y] == 0:
            moveBoard[x][y] = 1
            return False
    if y > 0:
        if board[x][y - 1] == 0:
            moveBoard[x][y] = 1
            return False
    if y < 4:
        if board[x][y + 1] == 0:
            moveBoard[x][y] = 1
            return False
    
    if x + y % 2 == 0:
        if x > 0 and y > 0:
            if board[x - 1][y - 1] == 0:
                moveBoard[x][y] = 1
                return False
        if x < 4 and y > 0:
            if board[x + 1][y - 1] == 0:
                moveBoard[x][y] = 1
                return False
        if x > 0 and y < 4:
            if board[x - 1][y + 1] == 0:
                moveBoard[x][y] = 1
                return False
        if x < 4 and y < 4:
            if board[x + 1][y + 1] == 0:
                moveBoard[x][y] = 1
                return False
    
    # PART II
    player = board[x][y]
    board[x][y] = 2
    check = []
    
    if x > 0:
        if board[x - 1][y] == player:
            check.append(cantMove(board, (x - 1, y)))
    if x < 4:
        if board[x + 1][y] == player:
            check.append(cantMove(board, (x + 1, y)))
    if y > 0:
        if board[x][y - 1] == player:
            check.append(cantMove(board, (x, y - 1)))
    if y < 4:
        if board[x][y + 1] == player:
            check.append(cantMove(board, (x, y + 1)))
            
    if x + y % 2 == 0:
        if x > 0 and y > 0:
            if board[x - 1][y - 1] == player:
                check.append(cantMove(board, (x - 1, y - 1)))
        if x < 4 and y > 0:
            if board[x + 1][y - 1] == player:
                check.append(cantMove(board, (x + 1, y - 1)))
        if x > 0 and y < 4:
            if board[x - 1][y + 1] == player:
                check.append(cantMove(board, (x - 1, y + 1)))
        if x < 4 and y < 4:
            if board[x + 1][y + 1] == player:
                check.append(cantMove(board, (x + 1, y + 1)))
                
    result = True
    for i in check:
        result = result and i
        
    if result:
        moveBoard[x][y] = 0
    else:
        moveBoard[x][y] = 1
    
    return result
        
def ganh(board, position):
    x, y = position[0], position[1]
    op = -1 * board[x][y]
    
    # HORIZONTAL
    if x > 0 and x < 4:
        if board[x - 1][y] == op and board[x + 1][y] == op:
            board[x - 1][y], board[x + 1][y] = board[x][y], board[x][y]
    # VERTICAL
    if y > 0 and y < 4:
        if board[x][y - 1] == op and board[x][y + 1] == op:
            board[x][y - 1], board[x][y + 1] = board[x][y], board[x][y]
    # DIAGONAL
    if (
        x + y % 2 == 0 and
        x > 0 and x < 4 and
        y > 0 and y < 4
    ):
        if board[x - 1][y - 1] == op and board[x + 1][y + 1] == op:
            board[x - 1][y - 1], board[x + 1][y + 1] = board[x][y], board[x][y]
        if board[x - 1][y + 1] == op and board[x + 1][y - 1] == op:
            board[x - 1][y + 1], board[x + 1][y + 1] = board[x][y], board[x][y]
         
def chan(board, player):
    # Init moveBoard
    moveBoard = []
    for i in range(5):
        tmp = []
        for j in range(5):
            tmp.append(2)
        moveBoard.append(tmp)
    
    pos = getPosition(board, player)
    
    # Check which position is "chan"
    for p in pos:
        if cantMove(board, p):
            board[p[0]][p[1]] = -1 * player
            
    for i in range(5):
        for j in range(5):
            if board[i][j] == 2:
                board[i][j] = player

# Return Node and a position
def move_gen(node, position):
    board = node.board
    x, y = position[0], position[1]
    player = board[x][y]
    opponent = -1 * player
    result = []
        
    # UP
    if x > 0 and tmp_board[x - 1][y] == 0:
        tmp_board = copy.deepcopy(board)
        tmp_board[x - 1][y] = copy.deepcopy(player)
        tmp_board[x][y] = 0
        
        ganh(tmp_board, (x - 1, y))
        chan(tmp_board, opponent)
        
        tmp = Node(tmp_board, node)
        result.append((tmp, (x - 1, y)))
    # DOWN
    if x < 4 and tmp_board[x + 1][y] == 0:
        tmp_board = copy.deepcopy(board)
        tmp_board[x + 1][y] = copy.deepcopy(player)
        tmp_board[x][y] = 0
        
        ganh(tmp_board, (x + 1, y))
        chan(tmp_board, opponent)
        
        tmp = Node(tmp_board, node)
        result.append((tmp, (x + 1, y)))
    # LEFT
    if y > 0 and tmp_board[x][y - 1] == 0:
        tmp_board = copy.deepcopy(board)
        tmp_board[x][y - 1] = copy.deepcopy(player)
        tmp_board[x][y] = 0
        
        ganh(tmp_board, (x, y - 1))
        chan(tmp_board, opponent)
        
        tmp = Node(tmp_board, node)
        result.append((tmp, (x, y - 1)))
    # RIGHT
    if y < 4 and tmp_board[x][y + 1] == 0:
        tmp_board = copy.deepcopy(board)
        tmp_board[x][y + 1] = copy.deepcopy(player)
        tmp_board[x][y] = 0
        
        ganh(tmp_board, (x, y + 1))
        chan(tmp_board, opponent)
        
        tmp = Node(tmp_board, node)
        result.append((tmp, (x, y + 1)))
            
    # DIAGONAL
    if x + y % 2 == 0:
        # UP LEFT
        if x > 0 and y > 0 and tmp_board[x - 1][y - 1] == 0:
            tmp_board = copy.deepcopy(board)
            tmp_board[x - 1][y - 1] = copy.deepcopy(player)
            tmp_board[x][y] = 0
            
            ganh(tmp_board, (x - 1, y - 1))
            chan(tmp_board, opponent)
            
            tmp = Node(tmp_board, node)
            result.append((tmp, (x - 1, y - 1)))
        # UP RIGHT
        if x > 0 and y < 4 and tmp_board[x - 1][y + 1] == 0:
            tmp_board = copy.deepcopy(board)
            tmp_board[x - 1][y + 1] = copy.deepcopy(player)
            tmp_board[x][y] = 0
            
            ganh(tmp_board, (x - 1, y + 1))
            chan(tmp_board, opponent)
            
            tmp = Node(tmp_board, node)
            result.append((tmp, (x - 1, y + 1)))
        # DOWN LEFT
        if x < 4 and y > 0 and tmp_board[x + 1][y - 1] == 0:
            tmp_board = copy.deepcopy(board)
            tmp_board[x + 1][y - 1] = copy.deepcopy(player)
            tmp_board[x][y] = 0
            
            ganh(tmp_board, (x + 1, y - 1))
            chan(tmp_board, opponent)
            
            tmp = Node(tmp_board, node)
            result.append((tmp, (x + 1, y - 1)))
        # DOWN RIGHT
        if x < 4 and y < 4 and tmp_board[x + 1][y + 1] == 0:
            tmp_board = copy.deepcopy(board)
            tmp_board[x + 1][y + 1] = copy.deepcopy(player)
            tmp_board[x][y] = 0
            
            ganh(tmp_board, (x + 1, y + 1))
            chan(tmp_board, opponent)
            
            tmp = Node(tmp_board, node)
            result.append((tmp, (x + 1, y + 1)))
                
    return result

def move(node, start, end):
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
            (x0 + y0 % 2 == 0 and
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
    
    node.board[x1][y1] = node.board[x0][y0]
    node.board[x0][y0] = 0