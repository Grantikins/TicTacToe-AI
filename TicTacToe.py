from enum import Enum
import copy

class Side(Enum):
    X = 1
    O = 4
    NEITHER = 0

class TicTacToeGame:
    def __init__(self, gameState=None):
        if gameState != None:
            self.board = copy.deepcopy(gameState["board"])
            self.pTurn = copy.deepcopy(gameState["turn"])
            self.gameOver = copy.deepcopy(gameState["gameover"])
            self.winner = copy.deepcopy(gameState["winner"])
        else:
            self.board = []
            for i in range(3):
                self.board.append([0, 0, 0])
            self.pTurn = Side.X
            self.gameOver = False
            self.winner = Side.NEITHER
    
    def placeX(self, row: int, col: int):
        if self.pTurn != Side.X or self.gameOver or self.board[row][col] != 0:
            return
        
        self.board[row][col] = 1
        if self.getWinner() != Side.NEITHER: 
            self.gameOver = True
            self.winner = self.getWinner()
        if self.checkTie():
            self.gameOver = True
        self.incTurn()
    
    def placeO(self, row: int, col: int):
        if self.pTurn != Side.O or self.gameOver or self.board[row][col] != 0:
            return
        
        self.board[row][col] = 4
        if self.getWinner() != Side.NEITHER: 
            self.gameOver = True
            self.winner = self.getWinner()
        if self.checkTie():
            self.gameOver = True
        self.incTurn()
        
    def isValidMove(self, row: int, col: int, side: Side):
        if self.board[row][col] != 0 or side != self.pTurn:
            return False
        
        return True   
    
    def getNextStates(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.isValidMove(i, j, self.pTurn):
                    moves.append([i, j])
        
        gameStates = []
        for move in moves:
            newState = copy.deepcopy(self.getGameState())
            newGame = TicTacToeGame(newState)
            if self.pTurn == Side.X:
                newGame.placeX(move[0], move[1])
            if self.pTurn == Side.O:
                newGame.placeO(move[0], move[1])
            gameStates.append(newGame)
        
        return gameStates
        
    def getWinner(self):
        # check rows
        for i in range(3):
            count = 0
            for j in range(3):
                count += self.board[i][j]
            if count == 3: 
                return Side.X
            if count == 12:
                return Side.O
        
        # check cols
        for i in range(3):
            count = 0
            for j in range(3):
                count += self.board[j][i]
            if count == 3: 
                return Side.X
            if count == 12:
                return Side.O
        
        # check diagonals
        count = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if count == 3: 
            return Side.X
        if count == 12:
            return Side.O
        count = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if count == 3: 
            return Side.X
        if count == 12:
            return Side.O
        
        return Side.NEITHER 
    
    def checkTie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False   
        
        return True    
    
    def getStrAtPos(self, row: int, col: int):
        if self.board[row][col] == 1: return "X"
        if self.board[row][col] == 4: return "O"
        return " "
    
    def printBoard(self):
        print(self.getStrAtPos(0, 0) + "  |  " + self.getStrAtPos(0, 1) + "  |  " + self.getStrAtPos(0, 2))
        print("---|-----|---")
        print(self.getStrAtPos(1, 0) + "  |  " + self.getStrAtPos(1, 1) + "  |  " + self.getStrAtPos(1, 2))
        print("---|-----|---")
        print(self.getStrAtPos(2, 0) + "  |  " + self.getStrAtPos(2, 1) + "  |  " + self.getStrAtPos(2, 2))
    
    def incTurn(self):
        if self.pTurn == Side.X: 
            self.pTurn = Side.O
        elif self.pTurn == Side.O:
            self.pTurn = Side.X
    
    def getGameState(self):
        return {"turn": self.pTurn, "board": self.board, "gameover": self.gameOver, "winner": self.winner}

    def printResult(self):
        if self.gameOver != True:
            return
        
        if self.getWinner() == Side.X:
            print("X Player Wins!")
        elif self.getWinner() == Side.O:
            print("O Player Wins!")
        elif self.checkTie():
            print("It's a Tie...")
