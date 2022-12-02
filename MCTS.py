import math
import copy

import game

class Solver:
    def __init__(self,
                 board: list = None,
                 player: int = 1,):
        self.board = board
        self.player, self.opponent = player, -1 * player
        self.total_simu = 0
        self.simu_threshold = 1000
        
        self.cg = game.CoGanh()

    # depend on the ratio win_simu / nums_sime of each node
    def choose_1(self, chessmans):
        best_move = None
        max_ratio = 0
        
        for c in chessmans:
            list = c.child
            for node in list:
                ratio = node.ratio()
                if ratio > max_ratio:
                    max_ratio = ratio
                    best_move = node
                
        return best_move
    
    # depend on the total numbers of simulation of each node
    def choose_2(self, chessmans):
        best_move = None
        max_simu = 0
        
        for c in chessmans:
            list = c.child
            for node in list:
                simu = node.nums_simu
                if simu > max_simu:
                    max_simu = simu
                    best_move = node
                
        return best_move

    # Evaluate function to balance the exploration and exploitation
    def evaluate(self, node, c = 1.414):
        x = node.ratio()
        y = math.sqrt(math.log(self.total_simu) / node.nums_simu)
        
        return x + c * y
    
    def Selection(self, list):
        if len(list) == 0:
            return None
        
        max_eval = 0
        best_node = None
        for node in list:
            eval = self.evaluate(node)
            if eval > max_eval:
                max_eval = eval
                best_node = node
                
        return best_node
    
    def Expansion(self, node):
        possible_moves = self.cg.move_gen_2(node)
        g = False
        
        for move in possible_moves:
            if move[1]:
                g = True
                break
            
        for move in possible_moves:
            if g:
                if not move[1]:
                    continue
            node.child.append(move[0])
    
    def Simulation(self, node):
        final_step = copy.deepcopy(node)
        
        while not self.cg.end_game(final_step.board):
            self.total_simu += 1

            node.nums_simu += 1     
            prev = node.parent
            while prev != None:
                prev.nums_simu += 1
                prev = prev.parent
            
            final_step = self.cg.random_move(final_step)
            
        if self.player == 1:
            if self.cg.X_win(final_step.board):
                return True
            return False
        else:
            if self.cg.O_win(final_step.board):
                return True
            return False

    def Update(self, node, win):
        if win:
            node.win_simu += 1
            prev = node.parent
            while prev != None:
                prev.win_sime += 1
                prev = prev.parent
        return
    
    def solv(self):
        pos = self.cg.getPosition(self.board, self.player)
        
        chessmans = []
        for p in pos:
            chessmans.append(self.cg.Node_2(p, self.board))
        
        while self.total_simu < self.simu_threshold:
            # First, select chessman
            selected_node = self.Selection(chessmans)
            
            # Selection
            while len(selected_node.child) > 0:
                list = selected_node.child
                selected_node = self.Selection(list)
            
            # Expansion
            self.Expansion(selected_node)
            list = selected_node.child
            
            # Simulation
            res = self.Simulation(selected_node)
            
            # Update
            self.Update(selected_node, res)
            
        best_move = self.choose_1(chessmans)
        start, end = best_move.parent.position, best_move.position
        
        return (start, end)