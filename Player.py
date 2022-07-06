class Player():
    
    def __init__ (self):
        self.Username = ""
        self.totalMoves = 0
        self.totalGames = 0
        self.totalWins = 0
        self.highestTile  = 0
        
    def winrate(self):
        return self.totalWins/self.totalGames
        