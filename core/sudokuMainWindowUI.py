from tkinter import *
from tkinter import ttk
from core.screenCenter import ScreenCenter
from core.sudokuGame import SudokuGame
from core.sudokuBoardUI import SudokuBoardUI

class SudokuMainWindowUI(ttk.Frame):

    def __init__(self, parent):
        if not parent:
            parent = Tk()
            parent.title("Inicio")
            parent.resizable(FALSE, FALSE)
            
        super().__init__(parent)
        self.pack(fill=BOTH)
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        self.margin = 70 
        self.side = 50
        self.width = self.margin * 2 + self.side * 9
        self.height = self.margin * 2 + self.side * 9 + 120 

        self.canvas = Canvas(self, width=self.width, height= self.height)
        self.canvas.pack(fill=BOTH, side=TOP)
        
        ttk.Button(self, text="Nuevo Juego", command=self.__newGame).place(x=100, y=200)
        ttk.Button(self, text="Continuar Juego", command=self.__continueGame).place(x=100, y=250)
        ttk.Button(self, text="Mejores Puntajes", command=self.__bestScores).place(x=100, y=300)

    def __newGame(self):
        with open('core/sudoku/n00b.sudoku', 'r') as boardFile:
            self.destroy()
            game = SudokuGame(boardFile)
            game.start()
            SudokuBoardUI(self.master, game)

    def __continueGame(self):
        pass

    def __bestScores(self):
        pass