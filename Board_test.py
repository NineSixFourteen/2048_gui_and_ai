from Board_class import Boards

class BoardTests():
    
    def __init__(self):
        self.testBoard1 = Boards()
        self.testBoard2 = Boards()
        
        self.gridLRUD = [[2,0,2,0],
                         [4,4,2,2],
                         [2,0,0,0],
                         [2,0,0,0]
                         ]
        self.gridLR   = [[2,2,2,4],
                         [4,4,4,2],
                         [2,2,2,4],
                         [4,4,4,2]
                         ]
        self.gridUD   = [[4,2,4,2],
                         [4,2,4,2],
                         [2,4,2,4],
                         [2,4,2,4]
                         ]
        self.gridUL   = [[0,4,2,4],
                         [4,2,4,2],
                         [2,4,2,4],
                         [4,2,4,2]
                         ]
        self.gridDR   = [[2,4,2,4],
                         [4,2,4,2],
                         [2,4,2,4],
                         [4,2,4,0]
                         ]
        self.gridBug =  [[0,4,2,4],
                         [0,0,0,4],
                         [0,0,2,4],
                         [0,0,0,2]
                         ]
        
        self.gridTestMoveL = [[0,0,0,0],
                             [2,0,0,0],
                             [2,0,2,4],
                             [0,2,4,2]
                             ]
        self.gridTestMoveR = [[0,0,0,0],
                             [0,0,0,2],
                             [4,0,0,4],
                             [4,2,4,0]
                             ]
        self.gridTestMoveR2 = [[0,0,0,0],
                              [0,0,0,0],
                              [0,0,0,0],
                              [4,4,4,8]
                              ]        
    def testInit(self):
        grid = self.testBoard2.grid
        noOfPeices = 0
        for x in range(4):
            for y in range(4):
                if grid[x][y] != 0:
                    noOfPeices += 1
        print("Test - Starting Peices")
        print("Expected Answer - 2\n",
              "Actual Answer  - ",noOfPeices,"\n",
              "Result - ",check(2,noOfPeices)
              )
        

        
    def testAll(self):
        self.testInit()
        self.testFindMoves()
        self.testRowMovable()
        self.testMoves()
        
    def testFindMoves(self):
        self.testBoard1.grid = self.gridLRUD
        self.testBoard1.findMoves()
        print("Test - All Directions")
        print("Expected Answer  - ","['LEFT', 'RIGHT', 'UP', 'DOWN']\n",
              "Actual Answer   - ",self.testBoard1.possibleMoves,"\n",
              "Result - ",check(['LEFT', 'RIGHT', 'UP', 'DOWN'],self.testBoard1.possibleMoves))
        self.testBoard1.grid = self.gridLR
        self.testBoard1.findMoves()
        print("Test - Horizontal")
        print("Expected Answer  - ","['LEFT', 'RIGHT']\n",
              "Actual Answer   - ",self.testBoard1.possibleMoves,"\n",
              "Result - ",check(['LEFT', 'RIGHT'],self.testBoard1.possibleMoves))
        self.testBoard1.grid = self.gridUD
        self.testBoard1.findMoves()       
        print("Test - Vertical")
        print("Expected Answer  - ","['UP', 'DOWN']\n",
              "Actual Answer   - ",self.testBoard1.possibleMoves,"\n",
              "Result - ",check(['UP', 'DOWN'],self.testBoard1.possibleMoves))
        self.testBoard1.grid = self.gridUL
        self.testBoard1.findMoves()    
        print("Test - Left and UP")
        print("Expected Answer  - ","['LEFT', 'UP']\n",
              "Actual Answer   - ",self.testBoard1.possibleMoves,"\n",
              "Result - ",check(['LEFT', 'UP'],self.testBoard1.possibleMoves))
        self.testBoard1.grid = self.gridDR
        self.testBoard1.findMoves()
        print("Test - Right and Down")
        print("Expected Answer  - ","['RIGHT', 'DOWN']\n",
              "Actual Answer   - ",self.testBoard1.possibleMoves,"\n",
              "Result - ",check(['RIGHT', 'DOWN'],self.testBoard1.possibleMoves))

    def testRowMovable(self):
        self.testBoard1.grid =  self.gridTestMoveL
        t1 = self.testBoard1.rowMovable(0,1)
        t2 = self.testBoard1.rowMovable(1,1)
        t3 = self.testBoard1.rowMovable(2,1)
        t4 = self.testBoard1.rowMovable(3,1)
        print("Test - Row Moveable L - [0,0,0,0]")
        print("Expected Answer - ","False\n",
              "Actual Answer  - ",t1,"\n",
              "Result - ",check(False,t1))
        print("Test - Row Moveable L - [2,0,0,0]")
        print("Expected Answer - ","False\n",
              "Actual Answer  - ",t2,"\n",
              "Result - ",check(False,t2))
        print("Test - Row Moveable L - [2,0,2,4]")
        print("Expected Answer - ","True\n",
              "Actual Answer  - ",t3,"\n",
              "Result - ",check(True,t3))        
        print("Test - Row Moveable L - [0,2,4,2]")
        print("Expected Answer - ","True\n",
              "Actual Answer  - ",t4,"\n",
              "Result - ",check(True,t4))        
        self.testBoard1.grid =  self.gridTestMoveR
        t1 = self.testBoard1.rowMovable(1,1)
        print("Test - Row Moveable L - [0,0,0,2]")
        print("Expected Answer - ","Truee\n",
              "Actual Answer  - ",t1,"\n",
              "Result - ",check(True,t1))
        t1 = self.testBoard1.rowMovable(0,0)
        t2 = self.testBoard1.rowMovable(1,0)
        t3 = self.testBoard1.rowMovable(2,0)
        t4 = self.testBoard1.rowMovable(3,0)
        print("Test - Row Moveable R - [0,0,0,0]")
        print("Expected Answer - ","False\n",
              "Actual Answer  - ",t1,"\n",
              "Result - ",check(False,t1))
        print("Test - Row Moveable R - [0,0,0,2]")
        print("Expected Answer - ","False\n",
              "Actual Answer  - ",t2,"\n",
              "Result - ",check(False,t2))
        print("Test - Row Moveable R - [4,0,0,4]")
        print("Expected Answer - ","True\n",
              "Actual Answer  - ",t3,"\n",
              "Result - ",check(True,t3))        
        print("Test - Row Moveable R - [4,2,4,0]")
        print("Expected Answer - ","True\n",
              "Actual Answer  - ",t4,"\n",
              "Result - ",check(True,t4))         
        print("Test - Row Moveable R - [2,0,0,0]")
        self.testBoard1.grid =  self.gridTestMoveL
        t1 = self.testBoard1.rowMovable(1,0)        
        print("Expected Answer - ","True\n",
              "Actual Answer  - ",t1,"\n",
              "Result - ",check(True,t1))     

        
    def testMoves(self):
        self.testBoard1.grid = self.gridLRUD
        self.testBoard1.moveLeft()
        print("Test - MoveLeft")
        print("Expected Answere - [4, 0, 0, 0]\n",
              "                  [8, 4, 0, 0]\n",
              "                  [2, 0, 0, 0]\n",
              "                  [2, 0, 0, 0]\n")
        print("Actual Answer   - ",self.testBoard1.grid[0],"\n",
              "                 ",self.testBoard1.grid[1],"\n",
              "                 ",self.testBoard1.grid[2],"\n",
              "                 ",self.testBoard1.grid[3])
        print("Result - ",check([[4,0,0,0],
                                 [8,4,0,0],
                                 [2,0,0,0],
                                 [2,0,0,0]],self.testBoard1.grid),"\n")
        
        self.testBoard1.grid = self.gridLRUD
        self.testBoard1.moveRight()
        print("Test - MoveRight")
        print("Expected Answere - [0, 0, 0, 4]\n",
              "                  [0, 0, 8, 4]\n",
              "                  [0, 0, 0, 2]\n",
              "                  [0, 0, 0, 2]\n")
        print("Actual Answer   - ",self.testBoard1.grid[0],"\n",
              "                 ",self.testBoard1.grid[1],"\n",
              "                 ",self.testBoard1.grid[2],"\n",
              "                 ",self.testBoard1.grid[3])
        print("Result - ",check([[0,0,0,4],
                                 [0,0,8,4],
                                 [0,0,0,2],
                                 [0,0,0,2]],self.testBoard1.grid),"\n")
        
        self.testBoard1.grid = self.gridLRUD
        self.testBoard1.moveUp()
        print("Test - MoveUp")
        print("Expected Answere - [2, 4, 4, 2]\n",
              "                  [4, 0, 0, 0]\n",
              "                  [4, 0, 0, 0]\n",
              "                  [0, 0, 0, 0]\n")
        print("Actual Answer   - ",self.testBoard1.grid[0],"\n",
              "                 ",self.testBoard1.grid[1],"\n",
              "                 ",self.testBoard1.grid[2],"\n",
              "                 ",self.testBoard1.grid[3])
        print("Result - ",check([[2,4,4,2],
                                 [4,0,0,0],
                                 [4,0,0,0],
                                 [0,0,0,0]],self.testBoard1.grid),"\n")
        
        self.testBoard1.grid = self.gridLRUD
        self.testBoard1.moveDown()
        print("Test - MoveDown")
        print("Expected Answere - [0, 0, 0, 0]\n",
              "                  [2, 0, 0, 0]\n",
              "                  [4, 0, 0, 0]\n",
              "                  [4, 4, 4, 2]\n")
        print("Actual Answer   - ",self.testBoard1.grid[0],"\n",
              "                 ",self.testBoard1.grid[1],"\n",
              "                 ",self.testBoard1.grid[2],"\n",
              "                 ",self.testBoard1.grid[3])
        print("Result - ",check([[0,0,0,0],
                                 [2,0,0,0],
                                 [4,0,0,0],
                                 [4,4,4,2]],self.testBoard1.grid),"\n")
        self.testBoard1.grid = self.gridTestMoveR2
        self.testBoard1.moveRight()
        print("Test - MoveDown")
        print("Expected Answere - [0, 0, 0, 0]\n",
              "                  [0, 0, 0, 0]\n",
              "                  [0, 0, 0, 0]\n",
              "                  [0, 4, 8, 8]\n")
        print("Actual Answer   - ",self.testBoard1.grid[0],"\n",
              "                 ",self.testBoard1.grid[1],"\n",
              "                 ",self.testBoard1.grid[2],"\n",
              "                 ",self.testBoard1.grid[3])
        print("Result - ",check([[0,0,0,0],
                                 [0,0,0,0],
                                 [0,0,0,0],
                                 [0,4,8,8]],self.testBoard1.grid),"\n")
        
    


def check(Expected,Actual):
    if Expected == Actual:
        return "Passed"
    return "Failed"


Test = BoardTests()
Test.testAll()