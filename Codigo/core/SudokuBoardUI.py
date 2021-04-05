from tkinter import *
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose

MARGIN = 70 # ! Se le sumaron 20 y se restaron 20 en los parámetros necesarios.
SIDE = 50
WIDTH = MARGIN * 2 + SIDE * 9
HEIGHT = MARGIN * 2 + SIDE * 9 +120# !Se le sumaron 120 para ampliar de forma vertical la ventana

class SudokuBoardUI(Frame):
    
    def __init__(self, parent, game):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.game = game
        self.row = -1
        self.col = -1
        self.__initUI(parent)

    def __initUI(self, parent):
        self.parent.title("Sudoku")
        self.parent.resizable(FALSE, FALSE)
        self.parent.configure(background = "#171717")
        self.parent.geometry("%dx%d" %(550, 750))
        center = ScreenCenter()
        center.center(self.parent, WIDTH, 750)
        self.pack(fill=BOTH)
        self.canvas = Canvas(parent, width=WIDTH, height= 610)
        self.canvas.configure(background = "#171717")
        self.canvas.pack(fill=BOTH, side=TOP)

        self.labelNameUser= Label(self.parent, text='Nombre de usuario', font=("Lato",13))
        self.labelNameUser.configure(background = "#171717", fg="white")
        self.labelNameUser.pack()
        self.labelNameUser.place(x=50,y=20)

        self.labelTime= Label(self.parent, text='Time: 00:00:00', font=("Lato",13))
        self.labelTime.configure(background = "#171717", fg="white")
        self.labelTime.pack()
        self.labelTime.place(x=380,y=560)

        self.clearButton = Button(parent, text="Limpiar Tablero", bg="#6ea8d9", font=("Lato",15), command=self.__clearAnswers)
        self.clearButton.pack(fill=BOTH, side=BOTTOM)
        self.returnButton = Button(parent, text="Deshacer jugada", bg="#6ea8d9", font=("Lato",15))
        self.returnButton.pack(fill=BOTH, side=BOTTOM)
        self.pauseButton = Button(parent, text="Pausa", bg="#6ea8d9", font=("Lato",15), command=self.__pauseGame)
        self.pauseButton.pack(fill=BOTH, side=BOTTOM)
        self.saveButton = Button(parent, text="Guardar partida", bg="#6ea8d9", font=("Lato",15))
        self.saveButton.pack(fill=BOTH, side=BOTTOM)
        
        self.__drawGrid()
        self.__drawPuzzle()
        self.canvas.bind("<Button-1>", self.__cellClicked)
        self.canvas.bind("<Key>", self.__keyPressed)
    
    def __pauseGame(self):

        self.game.pause = True

    def __drawGrid(self):

        for i in range(10):
            color = "#6ea8d9" if i % 3 == 0 else "gray"
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
                    color = "white" if answer == original else "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )
        
    def __drawCursor(self):
            
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            #print(self.row, self.col)
            x0 = MARGIN + self.col * SIDE + 1 - 20 # ! Se restaron 20
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1 - 20 #! Se restaron 20
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            #print("coordenadas: ",x0,x1,y0,y1)
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
            #print(row, col)
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
                #print("posición2",row, col)
                #pass

            # ! Se comprueba si la posición del arreglo es igual a 0, esto significa que es una posición donde
            # ! el usuario debe introducir un valor, o sea, que es "seleccionable".
            # ! Si se cambia el chequeo de posiciones donde se puede escribir por un arreglo de booleanos 
            # ! donde True pertenezca a una posición donde se puede escribir, entonces se puede implementar
            # ! la acción de sobreescribir un cuadro que ya fue escrito por el usuario.
            # ?Si se usa un else pinta todos los cuadros incluidos los que estan definidos
            # ?por el archivo 
            elif self.game.puzzle[row][col] == 0:
                #print("posición3",row, col)
                self.row, self.col = row, col
                #pass
        """
        Setea a -1 (no se pinta el recuadro de selección) los valores de fila y columna
        else:
            self.row, self.col = -1, -1 
        """
        
        self.__drawCursor()
    
    def __keyPressed(self, event):

        if (self.game.gameOver):
            return
            
        if (self.row >= 0 and self.col >= 0 and event.char in "1234567890"):
            try:
                self.game.puzzle[self.row][self.col] = int(event.char)
            except:
                pass
            self.col, self.row = -1, -1
            self.__drawPuzzle()
            self.__drawCursor()
            if self.game.checkWin():
                self.__drawVictory()

    def __clearAnswers(self):
        self.game.start()
        self.canvas.delete("victory")
        self.__drawPuzzle()

    def __onClosing(self):
        self.dialogClose = DialogClose(self.parent)
        self.parent.wait_window(self.dialogClose)
        # Bloque try except para manejar la excepción devuelta si el self.parent fue destruido
        try:
            # Confirma si la instancia de dialogClose existe
            if (self.dialogClose.winfo_exists() == False):
                # Si no existe entonces establece de nuevo la función de apertura de dialogClose cuando
                # se intenta cerrar la ventana
                self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        except:
            pass