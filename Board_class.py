import random as rd 

class Boards():
    
    def __init__(self):
        
        self.grid = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]
                      ]
        
        self.possibleMoves = []
        self.score = 0
        self.noMergers = 0
        self.noMoves = 0
        self.addPeice()
        self.addPeice()
        self.findMoves()
    
    def printDeets(self):
        print("GRID")
        for x in range(4):
            print(self.grid[x])
        print("Score            - ",self.score)
        print("Number of Merges - ",self.noMergers)
        print("Number of Moves  - ",self.noMoves)
        print("MOVES            - ",self.possibleMoves)
        print("Max Tile         - ",self.getBigestTile())
    
    def getBigestTile(self):
        grid = self.grid
        biggestNumber = 0
        for x in range(4):
            for y in range(4):
                if grid[x][y] > biggestNumber:
                    biggestNumber = grid[x][y]
        return biggestNumber
    
    def is_empty(self,col,row):
        if self.grid[col][row] == 0:
            return True
        else:
            return False

    def rowMovable(self,row,Left):
        if Left == 1:
            if self.grid[row][1] == 0 and self.grid[row][2] ==  0 and self.grid[row][3] == 0:
                return False
            for x in range(1,4):
                if self.grid[row][x-1] == 0 and self.grid[row][x] != 0:
                    return True
                if(self.grid[row][x-1] == self.grid[row][x] and self.grid[row][x-1] != 0 ):
                    return True
        else:
            if self.grid[row][0] == 0 and self.grid[row][1] ==  0 and self.grid[row][2] == 0:
                return False
            for x in range(0,3):
                if self.grid[row][x] != 0 and self.grid[row][x+1] == 0:
                    return True
                if(self.grid[row][x] == self.grid[row][x+1]  and self.grid[row][x] != 0 ):
                    return True
        return False
    

    def possibleMove(self,L):
        for x in range(4):
            if (self.rowMovable(x,L)):
                return True
        return False
    
    def findMoves(self):
        moves = []

        if self.possibleMove(1):
            moves.append("LEFT")
            
        if self.possibleMove(0):
            moves.append("RIGHT")
            
        self.rotateBoard()
        
        if self.possibleMove(1):
            moves.append("UP")
            
        if self.possibleMove(0):
            moves.append("DOWN")

        self.rotateBoard()
        self.possibleMoves = moves

    def addPeice(self):
        run = 1
        tile = rd.randint(0, 9)
        if tile > 0:
            tile = 2
        else:
            tile = 4
        while run:
            x = rd.randint(0, 3)
            y = rd.randint(0, 3)
            if self.is_empty(x, y):
                self.grid[x][y] = tile
                run = 0
            
    def afterMove(self):
        self.noMoves += 1
        self.addPeice()
        self.findMoves()
        
    def doMove(self,Move):
        if Move.lower() == "left" and "LEFT" in self.possibleMoves:
            self.moveLeft()
            self.afterMove()
        elif Move.lower() == "right" and "RIGHT" in self.possibleMoves:
            self.moveRight()
            self.afterMove()
        elif Move.lower() == "up" and "UP" in self.possibleMoves:
            self.moveUp()
            self.afterMove()
        elif Move.lower() == "down" and "DOWN" in self.possibleMoves:
            self.moveDown()
            self.afterMove()
                
    def doMoveWOAdd(self,Move):
        if Move.lower() == "left" and "LEFT" in self.possibleMoves:
            self.moveLeft()
        elif Move.lower() == "right" and "RIGHT" in self.possibleMoves:
            self.moveRight()
        elif Move.lower() == "up" and "UP" in self.possibleMoves:
            self.moveUp()
        elif Move.lower() == "down" and "DOWN" in self.possibleMoves:
            self.moveDown()
            
    def moveLeft(self):
        self.removeZero()
        self.combine()
        self.addZero()

    
    def moveRight(self):
        self.removeZero()
        self.flip()
        self.combine()
        self.addZero()    
        self.flip()

    def moveUp(self):
        self.rotateBoard()
        self.moveLeft()
        self.rotateBoard()

        
    def moveDown(self):
        self.rotateBoard()
        self.moveRight()
        self.rotateBoard()

        
    def rotateBoard(self):
        newBoard = []
        for col in range(4):
            c = [] 
            for row in range(4):
                c.append(self.grid[row][col])
            newBoard.append(c)
        self.grid = newBoard


    def removeZero(self):
        newBoard = []
        for row in range(4):
            r = []
            for col in range(4):
                if self.grid[row][col] != 0:
                    r.append(self.grid[row][col])
            newBoard.append(r)
        self.grid = newBoard

    def flip(self):
        for z in range(4):
            new_row = []
            size = len(self.grid[z])
            for x in range(size):
                new_row.append(self.grid[z][(size-1) - x])
            self.grid[z] = new_row
        
    def combine(self):               
        for row in range(4):
            r = self.grid[row]
            if (len(r)>1):
                x = 1
                y = len(r)
                while x < y:
                    if r[x-1] == r[x]:
                        r[x-1] = r[x-1] * 2
                        self.score += (r[x] *2)
                        self.noMergers += 1
                        r.pop(x)
                        y-=1
                    x+=1          

    
    def addZero(self):
        for x in range(4):
            if len(self.grid[x]) < 4:
                for y in range(4 - (len(self.grid[x]))):
                    self.grid[x].append(0)

                        
