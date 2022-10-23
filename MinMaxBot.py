import random
from TicTacToe import TicTacToeGame, Side

class GameTree:
    def __init__(self, game: TicTacToeGame, parent=None):
        self.game = game
        self.parent = parent
        self.nextStates = game.getNextStates()
        self.children = []
        self.value = 0
    
    def hasNextChild(self):
        if len(self.nextStates) > 0:
            return True
        
        return False
    
    def getNextChild(self):
        move = self.nextStates.pop()
        child = GameTree(move)
        self.children.append(child)
        return child


class MinMaxBot:
    def __init__(self, side: Side, game: TicTacToeGame):
        self.side = side
        self.game = game
        
    def takeTurn(self):
        game = self.chooseMove(self.game)
        move = game.getGameState()["board"]
        for i in range(3):
            for j in range(3):
                if move[i][j] != self.game.getGameState()["board"][i][j]:
                    if self.side == Side.X:
                        self.game.placeX(i, j)
                    else: 
                        self.game.placeO(i, j)

    def chooseMove(self, tttGame: TicTacToeGame):
        tempGame = TicTacToeGame(tttGame.getGameState())
        
        start = GameTree(tempGame)
        value = 0
        chosenChildren = []
        if tttGame.pTurn == Side.X:
            value = self.findMax(start)
        if tttGame.pTurn == Side.O:
            value = self.findMin(start)
        
        for child in start.children:
            if child.value == value:
                chosenChildren.append(child.game)
        
        return chosenChildren[random.randint(0, len(chosenChildren) - 1)]
    
    def findMax(self, tree: GameTree):
        if tree.game.getGameState()["gameover"]:
            return self.utility(tree.game.getGameState())

        mx = -10
        
        while tree.hasNextChild():
            child = tree.getNextChild()
            child.value = self.findMin(child)
            mx = max(mx, child.value)
            if mx == 1: return mx
        
        return mx
            
    
    def findMin(self, tree: GameTree):
        if tree.game.getGameState()["gameover"]:
            return self.utility(tree.game.getGameState())

        mn = 10
        
        while tree.hasNextChild():
            child = tree.getNextChild()
            child.value = self.findMax(child)
            mn = min(mn, child.value)
            if mn == -1: return mn
        
        return mn
    
    def utility(self, gameState):
        if gameState["gameover"] and gameState["winner"] == Side.X:
            return 1
        if gameState["gameover"] and gameState["winner"] == Side.O:
            return -1
        return 0
    
    
    
    
    