from Board_class import Boards
from copy import deepcopy
import time
from math import inf
import random


tableMax = {}
tableAvg = {}


testBoard = Boards()
testBoard.grid = [[0,2,2,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]
                 ]

def createRandomBoards(Board):
    BoardList = []
    for x in range(4):
        for y in range(4):
                if(Board.grid[x][y] == 0):
                    tBoard = deepcopy(Board)
                    tBoard.grid[x][y] = 2
                    BoardList.append((tBoard,2))
                    tBoard1 = deepcopy(Board)
                    tBoard1.grid[x][y] = 4
                    BoardList.append((tBoard1,4))
    return BoardList


def printBoardsList(BoardList):
    i = 0
    for board in BoardList:
        print(board[0].grid," - ",board[1])
        print(i)
        i+=1

def expectMax(Board,Depth,player):
    if Depth == 0:
        return heur(Board)
    Board.findMoves()
    if len(Board.possibleMoves) == 0:
        return -1000
    score = 0
    if player is True:
        bestScore = -inf
        if  (repr(Board.grid),Depth) in tableMax:
            return tableMax[ (repr(Board.grid),Depth)]
        for move in Board.possibleMoves:
            tBoard = deepcopy(Board)
            tBoard.doMoveWOAdd(move)
            score = expectMax(tBoard,Depth-1,not player)
            if bestScore < score:
                bestScore = score
        tableMax[ (repr(Board.grid),Depth)] = bestScore
        return bestScore
    else:
        i = 0
        if (repr(Board.grid),Depth) in tableAvg:
            return tableAvg[ (repr(Board.grid),Depth)]
        for board in createRandomBoards(Board):
            i +=1
            if(board[1] == 1):
                score += expectMax(board[0], Depth-1, not player)*0.8
            else:
                score += expectMax(board[0], Depth-1, not player)*0.2
        score = score /i
        tableAvg[ (repr(Board.grid),Depth)] = score
        return score

#
def smooth(Board):
    smooth = 0
    for x in range(3):
        for y in range(4):
            if Board.grid[x][y] != 0 and Board.grid[x+1][y] != 0:
                s = abs(Board.grid[x][y] - Board.grid[x+1][y])
                smooth += s
                    
    for x in range(4):
        for y in range(3):
            if Board.grid[x][y] != 0 and Board.grid[x][y+1] != 0:
                s = abs(Board.grid[x][y] - Board.grid[x][y+1])
                smooth += s
                    
    return 0-smooth
                    
def weighted(Board):
    score = 0
    total = 0
    weight = [[0.135,0.121,0.102,0.0999],
              [0.0997,0.088,0.076,0.0724],
              [0.0606,0.0562,0.0371,0.0161],
              [0.0125,0.0099,0.0057,0.0033]]

    for x in range(4):
        for y in range(4):
            if Board.grid[x][y] != 0:
                tile = Board.grid[x][y]
                score += tile * weight[x][y]
                total += tile
    return score + total
                    


def heur(Board):
    score = weighted(Board)
    return score
    

class AI():
    def __init__(self):
        self.board = Boards()
        
    def nextMove(self):
        bestScore = -inf
        ind = 0
        score = 0
        self.board.findMoves()
        moves =  self.board.possibleMoves
        for x in range(len(moves)):
            tBoard = deepcopy(self.board)
            tBoard.doMoveWOAdd(moves[x])
            if self.board.score < 10000:
                depth = 2
            else:
                depth = 4
            score = expectMax(tBoard, depth, False)
            if score > bestScore:
                bestScore = score
                ind = moves[x]
        return ind
    
    def takeBoard(self,newBoard):
        self.board = newBoard
