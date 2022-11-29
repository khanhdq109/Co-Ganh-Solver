import copy
import timeit

import game
        
class Solver:
    def __init__(self,
                 depth: int = 2,
                 board: list = None,
                 player: int = 1):
        self.depth = depth
        self.board = board
        self.player, self.opponent = player, -1 * player
        self.start = None
        self.end = None
    
    def evaluate(self, board):
        return sum(map(sum, board))
    
    def play(self, node, dp):
        if dp > self.depth: 
            return
        
        # LEAF NODE
        if dp == self.depth:
            return self.evaluate(node.board)
        
        score = 0
        cg = game.CoGanh()
        # PLAYER
        if dp % 2 == 0:
            score = -100
            pos = cg.getPosition(node.board, self.player)
            for p in pos:
                successor = cg.move_gen(node, p)
                if len(successor) == 0: continue
                for s in successor:
                    if cg.X_win(s[0].board): 
                        return 16
                    
                    value = self.play(s[0], dp + 1)
                    if value > score:
                        score = value
                        if dp == 0:
                            self.start = p
                            self.end = s[1]
        # OPPONENT
        else:
            score = 100
            pos = cg.getPosition(node.board, self.opponent)
            for p in pos:
                successor = cg.move_gen(node, p)
                if len(successor) == 0: continue
                for s in successor:
                    if cg.O_win(s[0].board): 
                        return -16
                    
                    value = self.play(s[0], dp + 1)
                    if value < score:
                        score = value
                        
        return score
    
    def minimax(self):
        node = game.Node(self.board)
        score = self.play(node, 0)
        return (self.start, self.end)