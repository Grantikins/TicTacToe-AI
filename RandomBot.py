import random
from TicTacToe import Side, TicTacToeGame 

class RandomBot:
    def __init__(self, side: Side, game: TicTacToeGame):
        self.side = side
        self.game = game
    
    def takeTurn(self):
        while self.game.getGameState()["turn"] == self.side and not self.game.getGameState()["gameover"]:
            if self.side == Side.X:
                self.game.placeX(random.randint(0, 2), random.randint(0, 2))
            else:
                self.game.placeO(random.randint(0, 2), random.randint(0, 2))
    