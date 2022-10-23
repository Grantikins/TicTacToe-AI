from Player import Player
from RandomBot import RandomBot
from MinMaxBot import MinMaxBot
from TicTacToe import Side, TicTacToeGame


game = TicTacToeGame()

xPlayer = Player(Side.X, game)
oPlayer = MinMaxBot(Side.O, game)

while not game.getGameState()["gameover"]:
    if game.getGameState()["turn"] == Side.X:
        xPlayer.takeTurn()
        print("The X Player played: ")
        game.printBoard()
    if game.getGameState()["turn"] == Side.O and not game.getGameState()["gameover"]:
        oPlayer.takeTurn()
        print("The O Player played: ")
        game.printBoard()
    
    game.printResult()
    
    


