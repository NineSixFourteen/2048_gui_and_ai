import tkinter as tk
import time
import random as rnd

frameM,Board,TILE_COLORS = 0,0,0


def init():
    global frameM,Board,TILE_COLORS
    Board = [[0,0,0,8],
         [0,4,0,4],
         [0,0,2,2],
         [0,0,0,2]
         ]

    TILE_COLORS = {2: "#daeddf", 4: "#9ae3ae", 8: "#6ce68d", 16: "#42ed71",
                   32: "#17e650", 64: "#17c246", 128: "#149938",
                   256: "#107d2e", 512: "#0e6325", 1024: "#0b4a1c",
                   2048: "#031f0a", 4096: "#000000", 8192: "#000000"}

    root = tk.Tk()
    h = 600
    w = 600
    root.geometry(f'{w}x{h}')
    
    tk.Grid.rowconfigure(root,0,weight=1)
    tk.Grid.columnconfigure(root,0,weight=1)
    tk.Grid.columnconfigure(root,1,weight=2)
    tk.Grid.columnconfigure(root,2,weight=1)
    
    frameL = tk.Frame(root,bg = 'silver')
    frameM = tk.Frame(root,bg = "#a8927b")
    frameR = tk.Frame(root,bg = 'silver')  
    
    
    frameL.grid(row =0,column = 0,sticky =  "NSEW")
    frameM.grid(row =0,column = 1,sticky =  "NSEW")
    frameR.grid(row =0,column = 2,sticky =  "NSEW")
    
    
    Left = tk.Button(frameR, text ="Left", command =  moveLeft)
    Left.pack()
    Right = tk.Button(frameR, text ="Right", command =  moveRight)
    Right.pack()
    UP = tk.Button(frameR, text ="UP", command =  moveUP)
    UP.pack()
    DOWN = tk.Button(frameR, text ="DOWN", command =  moveDown)
    DOWN.pack()
    

    drawBoard(Board)
    
    
    root.mainloop()


def drawBoard(board):
    global frameM,Board,TILE_COLORS
    for row in range(4):
        tk.Grid.rowconfigure(frameM,row,weight=1)
        for col in range(4):
            text =""
            colour = "#bbada0"
            if board[row][col] != 0:
                text = board[row][col]
                colour = TILE_COLORS[text]
            tk.Grid.columnconfigure(frameM,col,weight=1)
            tk.Label(frameM,text=text,bg=colour,justify=tk.CENTER, font= ("Verdana", 20, "bold")).grid(row = row,padx=5,pady=5,column = col,sticky = "NSEW")

def addPeice():
    run = 1
    while run:
        run = 0
        for x in range(4):
            if 0 in Board[x]:
                run = 1
        col = rnd.randint(0, 3)
        row = rnd.randint(0, 3)
        if Board[col][row] == 0:
             Board[col][row] = 2
             run = 0  
    drawBoard(Board)
    
    
def moveLeft():
    global Board
    newBoard = []
    for row in range(4):
        r = []
        for col in range(4):
            if Board[row][col] != 0:
                r.append(Board[row][col])
                
        if (len(r)>1):
            x = 1
            y = len(r)
            while x < y:
                if r[x-1] == r[x]:
                    r[x-1] = r[x-1] * 2
                    r.pop(x)
                    y-=1
                x+=1 
            
        if len(r) < 4:
            for s in range(4 - len(r)):
                r.append(0)
        newBoard.append(r)
    Board = newBoard
    addPeice()
    drawBoard(Board)
    print(Board)
    
def moveRight():
    global Board
    newBoard = []
    for row in range(4):
        r = []
        for col in range(4):
            if Board[row][col] != 0:
                r.append(Board[row][col])

        if (len(r)>1):
            x = 1
            y = len(r)
            while x < y:
                if r[x-1] == r[x]:
                    r[x-1] = r[x-1] * 2
                    r.pop(x)
                    y-=1
                x+=1 
            
        if len(r) < 4:
            for s in range(4 - len(r)):
                r.insert(0,0)
        newBoard.append(r)
    Board = newBoard
    addPeice()
    drawBoard(Board)
    print(Board)
    
def moveUP():
    rotateBoard()
    moveLeft()
    rotateBoard()
    drawBoard(Board)
    print(Board)

def moveDown():
    rotateBoard()
    moveRight()
    rotateBoard()
    drawBoard(Board)
    print(Board)
    
            
def rotateBoard():
    global Board
    newBoard = []
    for col in range(4):
        c = [] 
        for row in range(4):
            c.append(Board[row][col])
        newBoard.append(c)
    Board = newBoard

init()