from tkinter import *


MARGIN = 70 # !Se le sumaron 20 y se restaron 20 en los parámetros necesarios (NO HAY OTRA FORMA DE HACERLO)
SIDE = 50
WIDTH = MARGIN * 2 + SIDE * 9
HEIGHT = MARGIN * 2 + SIDE * 9 + 120 # !Se le sumaron 120 para ampliar de forma vertical la ventana

class SudokuUI(Frame):
    
    def __init__(self, parent, game):
        Frame.__init__(self, parent)
        self.parent = parent
        self.game = game
        self.row = -1
        self.col = -1
        self.__initUI(parent)

    def __initUI(self, parent):
        self.parent.title("Sudoku")
        self.parent.resizable(FALSE, FALSE)
        self.parent.configure(background = "white")
        self.pack(fill=BOTH)
        self.canvas = Canvas(parent, width=WIDTH, height= HEIGHT)
        self.canvas.configure(background = "white")
        self.canvas.pack(fill=BOTH, side=TOP)
        """ clearButton = Button(parent, text="Limpiar Tablero", command=self.__clearAnswers)
        clearButton.pack(fill=BOTH, side=BOTTOM)
        pauseButton = Button(parent, text="Pausa", command=self.__pauseGame)
        pauseButton.pack(fill=BOTH, side=BOTTOM) """
        self.__drawGrid()
        self.__drawPuzzle()
        self.canvas.bind("<Button-1>", self.__cellClicked)
        self.canvas.bind("<Key>", self.__keyPressed)
    
    def __pauseGame(self):

        self.game.pause = True
    """
    def __continueGame(self):

        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        oval = self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="continue", fill="green", outline="green"
        )
        
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        text = self.canvas.create_text(
            x, y,
            text="Continuar", tags="continue",
            fill="white", font=("Arial", 24)
        )

    def __showHide(self, buttonHide, buttonShow):

        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        oval = self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="pause", fill="red", outline="red"
        )
        
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        text = self.canvas.create_text(
            x, y,
            text="Juego Pausado", tags="pause",
            fill="white", font=("Arial", 24)
        )

        buttonHide.pack_forget()
        buttonShow.pack(fill = BOTH, side = BOTTOM)
    
    """
    def __drawGrid(self):

        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"
            x0 = MARGIN + i * SIDE - 20 # !Se restaron 20
            y0 = MARGIN
            x1 = MARGIN + i * SIDE - 20 # !Se restaron 20
            y1 = HEIGHT - MARGIN - 120 # !Se restaron 120
            # Lineas Verticales
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
            
            x0 = MARGIN - 20 # !Se restaron 20
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN - 20 # !Se restaron 20
            y1 = MARGIN + i * SIDE
            # Lineas Horizontales
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
    
    def __drawPuzzle(self):

        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.puzzle[i][j]
                if answer != 0:
                    x = MARGIN+ j * SIDE + SIDE / 2  - 20 # !Se restaron 20
                    y = MARGIN + i * SIDE + SIDE / 2
                    original = self.game.startPuzzle[i][j]
                    color = "black" if answer == original else "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )
        
    def __drawCursor(self):
            
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1 - 20 # ! Se restaron 20
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1 - 20 #! Se restaron 20
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )

    def __drawVictory(self):

        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="victory",
            fill="white", font=("Arial", 32)
        )

    def __cellClicked(self, event):

        if (self.game.gameOver):
            return

        if (self.game.pause):
            return

        x, y = event.x + 20, event.y # ! Se restaron 20 al evento x
        if (MARGIN  < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN - 120):
            self.canvas.focus_set()
            row, col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE 
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.game.puzzle[row][col] == 0:
                self.row, self.col = row, col
        else:
            self.row, self.col = -1, -1

        self.__drawCursor()
    
    def __keyPressed(self, event):

        if (self.game.gameOver):
            return
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.game.puzzle[self.row][self.col] = int(event.char)
            self.col, self.row = -1, -1
            self.__drawPuzzle()
            self.__drawCursor()
            if self.game.checkWin():
                self.__drawVictory()

    def __clearAnswers(self):
        self.game.start()
        self.canvas.delete("victory")
        self.__drawPuzzle()

