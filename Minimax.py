import copy

import game
        
class Solver:
    def __init__(self,
                 depth: int = 2,
                 board: list = None,
                 player: int = 1,):
        self.depth = depth
        self.board = copy.deepcopy(board)
        self.player, self.opponent = player, -1 * player
        
        self.start = None
        self.end = None
    
    def evaluate(self, board):
        return sum(map(sum, board))
    
    def play(self, node, dp, alpha = -100, beta = 100):
        if dp > self.depth:
            return
        
        # LEAF NODE
        if dp == self.depth:
            return self.evaluate(node.board)
        
        g = False
        cg = game.CoGanh()
        
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
        node = game.Node_1(self.board)
        score = self.play(node, 0)
        return (self.start, self.end)