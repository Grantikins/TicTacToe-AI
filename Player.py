from TicTacToe import Side, TicTacToeGame 

class Player:
    def __init__(self, side: Side, game: TicTacToeGame):
        self.side = side
        self.game = game
    
    def takeTurn(self):
        move = input("Give your move in format: row column. Example: 1 1\n")
        move.strip()
        if len(move) != 3 or int(move[0]) > 2 or int(move[0]) < 0 or int(move[2]) > 2 or int(move[2]) < 0 or move[1] != " ":
            print("not a valid move")
        else:
            self.game.placeX(int(move[0]), int(move[2]))
            self.game.placeO(int(move[0]), int(move[2]))
    