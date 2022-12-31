import copy

import game
        
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
        
        cg = game.CoGanh()
        trap = None
        
        # PLAYER
        if dp % 2 == 0:
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
                    if s[3]:
                        isTrapped = True
                        break
                    
                for s in successor:
                    if isTrapped:
                        if not s[3]:
                            continue
                        
                    if self.player == -1:
                        if cg.X_win(s[0].board):
                            if dp == 0:
                                self.start = s[2]
                                self.end = s[1]
                            return 75
                    else:
                        if cg.O_win(s[0].board):
                            if dp == 0:
                                self.start = s[2]
                                self.end = s[1]
                            return 75
                    
                    value = self.play(s[0], dp + 1, alpha, beta)
                    if value > alpha:
                        alpha = value
                        if dp == 0:
                            self.start = s[2]
                            self.end = s[1]
                    if alpha >= beta:
                        return alpha
            return alpha
                            
        # OPPONENT
        else:
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
                    if s[3]:
                        isTrapped = True
                        break
                    
                for s in successor:
                    if isTrapped:
                        if not s[3]:
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
        node = game.Node_1(self.board, self.prev_board)
        score = self.play(node, 0)
        if self.start == None or self.end == None:
            return None
        return (self.start, self.end)