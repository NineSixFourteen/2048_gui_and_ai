import tkinter as tk
from Board_class import Boards
from copy import deepcopy
from PlayerAI import AI



class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.aColour = '#b6baba'

    def on_enter(self, e):
        self['background'] = self.aColour

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        


class application(tk.Frame):

    def __init__(self):
        self.root = tk.Tk() # make window 
        self.root.title("2048") #set title
        
        self.aiP = AI()
        self.aiON = False
    
        self.width = 600
        self.height = 400
        self.root.geometry("1200x600") # set window deafult size

        self.scaleVal = 300
        
        self.root.rowconfigure(0,weight=1)  # make grid elements fill area
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=1) #weight to fill 2 as much area
        self.root.columnconfigure(2,weight=1)
        self.root.columnconfigure(3,weight=1)
        
        #Colour of each tile 
        self.TILE_COLORS = {2: "#daeddf", 4: "#9ae3ae", 8: "#6ce68d", 16: "#42ed71",
                   32: "#17e650", 64: "#17c246", 128: "#149938",
                   256: "#107d2e", 512: "#0e6325", 1024: "#0b4a1c",
                   2048: "#031f0a", 4096: "#031f0a", 8192: "#031f0a"}

        
        self.board = Boards() # make 2048 board
        self.UndoList = [] # List to store previous moves
        self.RedoList = [] # List to store undo moves 
        
        
        #Set up 3 panels 
        self.left_panel = tk.Frame(self.root ,bg = 'silver') 
        self.left_panel.grid(row =0,column = 0,sticky =  "NSEW")
        self.mid_panel = tk.Frame(self.root ,bg = "#a8927b")
        self.mid_panel.grid(row =0,column = 1,columnspan=2,sticky =  "NSEW")
        self.right_panel = tk.Frame(self.root ,bg = 'silver')
        self.right_panel.grid(row =0,column = 3,sticky =  "NSEW")

        # make grid elements fill area
        self.left_panel.rowconfigure(0,weight=1)
        self.left_panel.rowconfigure(1,weight=1)
        self.left_panel.columnconfigure(0,weight=1)
        
        #Split left panel into 2 areas
        self.left_panel_top = tk.Frame(self.left_panel,bg = 'silver')
        self.left_panel_top.grid(row =0,column = 0,sticky =  "NSEW")
        self.left_panel_bottom = tk.Frame(self.left_panel,bg = 'white')
        self.left_panel_bottom.grid(row =1,column = 0,sticky =  "NSEW")
        
        #Make bottom left panel a 5x5 grid
        for x in range(5):
            self.left_panel_bottom.rowconfigure(x,weight=1)
            self.left_panel_bottom.columnconfigure(x,weight=1)
        
        #Split right panel into 2 sections
        self.right_panel.rowconfigure(0,weight=1)
        self.right_panel.rowconfigure(1,weight=1)
        self.right_panel.rowconfigure(2,weight=1)
        self.right_panel.rowconfigure(3,weight=1)
        self.right_panel.columnconfigure(0,weight=1)
        
        
        self.right_panel_top = tk.Frame(self.right_panel,bg = 'white',)
        self.right_panel_top.grid(row =0,column = 0,sticky =  "NSEW")
        self.right_panel_topM = tk.Frame(self.right_panel,bg = 'white')
        self.right_panel_topM.grid(row =1,column = 0,sticky =  "NSEW")
        self.right_panel_bottomM = tk.Frame(self.right_panel,bg = 'silver')
        self.right_panel_bottomM.grid(row =2,column = 0,sticky =  "NSEW")
        self.right_panel_bottom = tk.Frame(self.right_panel,bg = 'silver')
        self.right_panel_bottom.grid(row =3,column = 0,sticky =  "NSEW")
                
        #Stop frame size from changing
        self.mid_panel.grid_propagate(False)
        self.right_panel_bottom.grid_propagate(False)
        self.right_panel_top.grid_propagate(False)
        self.left_panel_bottom.grid_propagate(False)
        self.right_panel_bottomM.grid_propagate(False)
        self.right_panel_topM.grid_propagate(False)
        
        for x in range(2):
            self.right_panel_topM.rowconfigure(x,weight=1)
            self.right_panel_top.rowconfigure(x,weight=1)
            self.right_panel_bottom.rowconfigure(x,weight=1)
        for x in range(3):
            self.right_panel_bottom.rowconfigure(x,weight=1)
            self.right_panel_topM.columnconfigure(x,weight=1)
            self.right_panel_bottom.columnconfigure(x,weight=1)
            self.right_panel_top.columnconfigure(x,weight=1)
            self.right_panel_bottomM.rowconfigure(x,weight=1)
            
        for x in range(5):
            self.right_panel_bottomM.columnconfigure(x,weight=1)
        self.right_panel_bottom.rowconfigure(0,weight=1)
        
        #Bind Keys to functions to move board
        self.root.bind("<Left>",self.moveLeftK)
        self.root.bind("<Right>",self.moveRightK)
        self.root.bind("<Up>",self.moveUPK)
        self.root.bind("<Down>",self.moveDownK)
        

        self.drawRightBottomM()
        #draw screen
        self.root.after(10,self.updateEverything)
        self.root.after(500,self.AI_TURN)
        #Keeps running till closed
        self.root.mainloop()
        
        

    def drawRightTop(self):
        for widget in self.right_panel_top.winfo_children():
           widget.destroy()
        font_size = int(self.height /100) *3
        self.sizeLabel = tk.Label(self.right_panel_top,text="Size Settings",justify = tk.CENTER,font= ("Verdana", font_size))
        self.sizeLabel.grid(row=0,column = 0,columnspan=3,sticky="NSEW")
        self.smallSizeButton = HoverButton(self.right_panel_top, text ="SMALL", command = self.setSizeSmall,bg="grey",font= ("Verdana", font_size))
        self.smallSizeButton.grid(row=1,column = 0, sticky='NSEW')
        self.medSizeButton = HoverButton(self.right_panel_top, text ="MEDIUM", command = self.setSizeMed,bg="grey",font= ("Verdana", font_size))
        self.medSizeButton.grid(row=1,column = 1, sticky='NSEW')
        self.largeSizeButton = HoverButton(self.right_panel_top, text ="LARGE", command = self.setSizeLarge,bg="grey",font= ("Verdana", font_size))
        self.largeSizeButton.grid(row=1,column = 2, sticky='NSEW')

    def drawRightTopM(self):
        for widget in self.right_panel_topM.winfo_children():
           widget.destroy()
        font_size = int(self.height /100) *3
        self.scaleLabel = tk.Label(self.right_panel_topM,text="Height",justify = tk.CENTER,font= ("Verdana", font_size))
        self.scaleLabel.grid(row=0,column = 0,columnspan=3,sticky="NSEW")
        self.sizeScale = tk.Scale(self.right_panel_topM,orient=tk.HORIZONTAL,from_=300, to=1800,font= ("Verdana", font_size),bd =1)
        self.sizeScale.set(self.scaleVal)
        self.sizeScale.grid(row=1,column = 0,columnspan=3, sticky='NSEW')

    def drawRightBottomM(self):
        for widget in self.right_panel_bottomM.winfo_children():
           widget.destroy()
        font_size = int(self.height /100) *3
        self.refresh = tk.PhotoImage(file = r"C:\Users\Aidan\Documents\python side\tkinter prac\images\Refresh.png")
        self.refreshButton = HoverButton(self.right_panel_bottomM, command =  self.AI_TOG, text = "AI",bg="grey")   
        self.refreshButton.grid(row=0, column=0,columnspan=2, sticky='NSEW')      
        self.reSizeButtton = HoverButton(self.right_panel_bottomM, text ="Resize", command =  self.reSizeScale,bg="grey",font= ("Verdana", font_size))   
        self.reSizeButtton.grid(row=0, column=2,columnspan = 3, sticky='NSEW')      
        #Make undoButton see HoverButton class at top of page
        self.undoButton = HoverButton(self.right_panel_bottomM, text ="UNDO", command = self.undoMove,bg="grey",font= ("Verdana", font_size))
        self.undoButton.grid(row=1,column = 0, columnspan = 2, sticky='NSEW')

        self.undoButton5 = HoverButton(self.right_panel_bottomM, text ="x5", command = self.undoMoveX5,bg="grey",font= ("Verdana", font_size))
        self.undoButton5.grid(row=1,column = 2, sticky='NSEW')

        self.undoButton10 = HoverButton(self.right_panel_bottomM, text ="x10", command = self.undoMoveX10,bg="grey",font= ("Verdana", font_size))
        self.undoButton10.grid(row=1,column = 3, sticky='NSEW')

        self.undoButton30 = HoverButton(self.right_panel_bottomM, text ="x30", command = self.undoMoveX30,bg="grey",font= ("Verdana", font_size))
        self.undoButton30.grid(row=1,column = 4, sticky='NSEW')

            
        #Make redoButton see HoverButton class at top of page
        self.redoButton = HoverButton(self.right_panel_bottomM, text ="REDO", command = self.redoMove,bg="grey",font= ("Verdana", font_size),width = 5)
        self.redoButton.grid(row=2,column = 0, columnspan = 2, sticky='NSEW')
        
        self.redoButton5 = HoverButton(self.right_panel_bottomM, text ="x5", command = self.redoMoveX5,bg="grey",font= ("Verdana", font_size))
        self.redoButton5.grid(row=2,column = 2, sticky='NSEW')
        
        self.redoButton10 = HoverButton(self.right_panel_bottomM, text ="x10", command = self.redoMoveX10,bg="grey",font= ("Verdana", font_size))
        self.redoButton10.grid(row=2,column = 3, sticky='NSEW')
        
        self.redoButton10 = HoverButton(self.right_panel_bottomM, text ="x30", command = self.redoMoveX30,bg="grey",font= ("Verdana", font_size))
        self.redoButton10.grid(row=2,column = 4, sticky='NSEW')
    
    def reSizeScale(self):
        self.setSize("scale")
        
    def AI_TURN(self):
        if self.aiON :
            self.aiP.takeBoard(self.board)
            x = self.aiP.nextMove()
            if   x == "LEFT":
                self.moveLeft()
            elif x == "DOWN":
                self.moveDown()
            elif x == "RIGHT":
                self.moveRight()
            else:
                self.moveUP()
        self.root.after(50,self.AI_TURN)
                
    def AI_TOG(self):
        self.aiON = {True:False,False:True}[self.aiON]
                
        
    def setSize(self,size):
        if size == "small":
            self.root.geometry("800x400") 
            self.height = 400
            self.width = 800
            self.scaleVal = 400
        elif size == "medium":
            self.root.geometry("1200x600") 
            self.height = 600
            self.width = 1200
            self.scaleVal = 600
        elif size == "large":
            self.root.geometry("1800x900") 
            self.height = 900
            self.width = 1800
            self.scaleVal = 900
        elif size=="scale":
             h = self.sizeScale.get()
             w = h * 2
             self.scaleVal = h
             self.root.geometry(f"{w}x{h}") 
             self.height = h
             self.width = w
        self.drawBoard()
        self.drawGameStats()
        self.drawControlls()
        self.drawRightTop()
        self.drawRightTopM()
        self.drawRightBottomM()
    
    
    def setSizeSmall(self):
        self.setSize("small")
        
    def setSizeMed(self):
        self.setSize("medium")
    
    def setSizeLarge(self):
        self.setSize("large")

            
        
    #Update Ui
    def updateEverything(self):
        self.height = self.root.winfo_height()
        self.width = self.root.winfo_width()
        self.drawBoard()
        self.drawGameStats()
        self.drawControlls()
        self.drawRightTop()
        self.drawRightTopM()



    
    #Draws the Board
    def drawBoard(self):
        #Clears the middle panel where the board is drawn
        for widget in self.mid_panel.winfo_children():
           widget.destroy()
        #Sets grid
        self.mid_panel.grid(row =0,column = 1,sticky =  "NSEW")
        for row in range(4):
            tk.Grid.rowconfigure(self.mid_panel,
                                 row,weight=1)
            for col in range(4):
                text = ""
                colour = "#bbada0"
                if self.board.grid[row][col] != 0:
                    text = self.board.grid[row][col]
                    colour = self.TILE_COLORS[text]
                tk.Grid.columnconfigure(self.mid_panel,col,weight=1)
                tk.Label(self.mid_panel,height = 10,width = 10,text=text,bg=colour,justify=tk.CENTER, font= ("Verdana", 20, "bold")).grid(row = row,padx=3,pady=3,column = col,sticky = "NSEW")

    def drawGameStats(self):
        for widget in self.left_panel_bottom.winfo_children():
            widget.destroy()
        
        
        font_size = int((self.height /100) * 3)
        ScoreText = "Score : " + str(self.board.score)
        MergeText = "Total Merges : " + str(self.board.noMergers)
        BiggestTileText = "Biggest Tile : " + str(self.board.getBigestTile())
        tk.Label(self.left_panel_bottom,text = "GAME STATS",justify=tk.CENTER,font= ("Verdana", font_size, "bold"),bg='white').grid(row = 0,column=1,columnspan=3)
        tk.Label(self.left_panel_bottom,text = ScoreText,justify=tk.CENTER,font= ("Verdana", font_size, "bold"),bg='white').grid(row = 1,column=0,columnspan=5)
        tk.Label(self.left_panel_bottom,text = MergeText,justify=tk.CENTER,font= ("Verdana", font_size, "bold"),bg='white').grid(row = 2,column=0,columnspan=5)
        tk.Label(self.left_panel_bottom,text = BiggestTileText,justify=tk.CENTER,font= ("Verdana", font_size, "bold"),bg='white').grid(row = 3,column=0,columnspan=5)
        

    def drawControlls(self):
        for widget in self.right_panel_bottom.winfo_children():
            widget.destroy()

        #Make move left button image of arrow pointing left
        self.LeftBPhoto = tk.PhotoImage(file = r"C:\Users\Aidan\Documents\python side\tkinter prac\images\arrowButtons\left.png")
        self.Left_button = HoverButton(self.right_panel_bottom, text ="Left", command =  self.moveLeft,image = self.LeftBPhoto,bg="grey",bd = 5,relief = tk.GROOVE)
        self.Left_button.grid(row=2, column=0, padx=1, pady=1, sticky='NSEW')

        #Make move Right button image of arrow pointing left
        self.RightBPhoto = tk.PhotoImage(file = r"C:\Users\Aidan\Documents\python side\tkinter prac\images\arrowButtons\Right.png")
        self.Right_button = HoverButton(self.right_panel_bottom, text ="Right", command =  self.moveRight,image = self.RightBPhoto,bg="grey",bd = 5,relief = tk.GROOVE)
        self.Right_button.grid(row=2, column=2, padx=1, pady=1, sticky='NSEW')
        
        #Make move Up button image of arrow pointing left
        self.UpBPhoto = tk.PhotoImage(file = r"C:\Users\Aidan\Documents\python side\tkinter prac\images\arrowButtons\UP.png")
        self.Up_button = HoverButton(self.right_panel_bottom, text ="UP", command =  self.moveUP,image = self.UpBPhoto,bg="grey",bd = 5,relief = tk.GROOVE)
        self.Up_button.grid(row=1, column=1, padx=1, pady=1, sticky='NSEW')
        
        #Make move down button image of arrow pointing left
        self.DownBPhoto = tk.PhotoImage(file = r"C:\Users\Aidan\Documents\python side\tkinter prac\images\arrowButtons\Down.png")
        self.Down_button = HoverButton(self.right_panel_bottom, text ="DOWN", command = self.moveDown,image = self.DownBPhoto,bg="grey",bd = 5,relief = tk.GROOVE)
        self.Down_button.grid(row=2, column=1, padx=1, pady=1, sticky='NSEW')
        

        
        
    def undoMove(self):
        if (len(self.UndoList) > 0):
            self.RedoList.append(deepcopy(self.board))
            newBoard = self.UndoList.pop()
            self.board = newBoard            
            self.updateEverything()

    def undoMoveNoDraw(self):
        if (len(self.UndoList) > 0):
            self.RedoList.append(deepcopy(self.board))
            newBoard = self.UndoList.pop()
            self.board = newBoard
            
            
    def undoMoveMult(self,x):
        for z in range(x):
            self.undoMoveNoDraw()
        self.updateEverything()
            
    def undoMoveX5(self):
        self.undoMoveMult(5)
    
    def undoMoveX10(self):
        self.undoMoveMult(10)
    
    def undoMoveX30(self):
        self.undoMoveMult(30)
        
        

    def redoMove(self):
        if (len(self.RedoList) > 0):
            self.UndoList.append(deepcopy(self.board))
            newBoard = self.RedoList.pop()
            self.board = newBoard
            self.updateEverything()

    def redoMoveNoDraw(self):
        if (len(self.RedoList) > 0):
            self.UndoList.append(deepcopy(self.board))
            newBoard = self.RedoList.pop()
            self.board = newBoard            

            
            
    def redoMoveMult(self,x):
        for z in range(x):
            self.redoMoveNoDraw()
        self.updateEverything()
            
    def redoMoveX5(self):
        self.redoMoveMult(5)
            
    def redoMoveX10(self):
        self.redoMoveMult(10)
        
    def redoMoveX30(self):
        self.redoMoveMult(30)
            
    def moveLeft(self):
        if ("LEFT" in self.board.possibleMoves):
            self.UndoList.append(deepcopy(self.board))
            self.RedoList = []
            self.board.doMove("left")
            self.updateEverything()
            
        
    def moveRight(self):
        if ("RIGHT" in self.board.possibleMoves):
            self.UndoList.append(deepcopy(self.board))
            self.RedoList = []
            self.board.doMove("right")
            self.updateEverything()
        
    def moveUP(self):
        if ("UP" in self.board.possibleMoves):
            self.UndoList.append(deepcopy(self.board))
            self.RedoList = []
            self.board.doMove("up")
            self.updateEverything()
        
    def moveDown(self):
        if ("DOWN" in self.board.possibleMoves):
            self.UndoList.append(deepcopy(self.board))
            self.RedoList = []
            self.board.doMove("down")
            self.updateEverything()
            
    def moveLeftK(self,event):
        self.moveLeft()
            
    def moveRightK(self,event):
        self.moveRight()
        
    def moveUPK(self,event):
        self.moveUP()
        
    def moveDownK(self,event):
        self.moveDown()
        
        
application()