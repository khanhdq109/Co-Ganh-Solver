import game

class Solver:
    def __init__(self,
                 board: list = None,
                 player: int = 1,):
        self.board = board
        self.player, self.opponent = player, -1 * player
        self.start = None
        self.end = None
    
    def Selection(self,):
        return
    
    def Expansion(self,):
        return
    
    def Simulation(self,):
        return 

    def Update(self,):
        return
    
    def mcts(self,)