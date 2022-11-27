import copy
import timeit

import game
        
class solver:
    def __init__(self,
                 depth: int = 2,
                 board: list = None):
        self.depth = depth
        self.board = board
        self.start = None
        self.end = None
    
    def evaluate(self, board):
        result = 0
        for i in board:
            for j in i:
                result += j
        return result
    
    def player(self, node, dp):
        if dp > self.depth: 
            return
        
        # LEAF NODE
        if dp == self.depth:
            return self.evaluate(node.board)
        
        score = 0
        # PLAYER
        if dp % 2 == 0:
            score = -100
            pos = game.getPosition(node.board, 1)
            for p in pos:
                successor = game.move_gen(node, p)
                for s in successor:
                    value = self.player(s[0].board, dp + 1)
                    if value > score:
                        score = value
                        if dp == 0:
                            self.start = p
                            self.end = s[1]
        # OPPONENT
        else:
            score = 100
            pos = game.getPosition(node.board, -1)
            for p in pos:
                successor = game.move_gen(node, p)
                for s in successor:
                    value = self.player(s[0].board, dp + 1)
                    if value < score:
                        score = value
                        
        return score
    
    def minimax(self):
        node = game.Node(self.board)
        score = self.player(self.board, self.depth)
        return (self.start, self.end)