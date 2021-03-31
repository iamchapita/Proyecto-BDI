from tkinter import *
from core.screenCenter import ScreenCenter

class SudokuMainWindowUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.__initUI(parent)

    def __initUI(self, parent):
        self.margin = 70 
        self.side = 50
        self.width = self.margin * 2 + self.side * 9
        self.height = self.margin * 2 + self.side * 9 + 120 
        self.center = ScreenCenter()
        self.center.center(parent)
        self.parent.title("Inicio")
        self.parent.resizable(FALSE, FALSE)
        self.parent.configure(background = "white")
        self.pack(fill=BOTH)
        self.canvas = Canvas(parent, width=self.width, height= self.height)
        self.canvas.configure(background = "white")
        self.canvas.pack(fill=BOTH, side=TOP)
        newGameButton = Button(parent, text="Nuevo Juego", command=self.__newGame)
        continueGameButton = Button(parent, text="Continuar Juego", command=self.__continueGame)
        bestScoresButton = Button(parent, text="Mejores Puntajes", command=self.__bestScores)
        newGameButton.place(x=100, y=200)
        continueGameButton.place(x=100, y=250)
        bestScoresButton.place(x=100, y=300)

    def __newGame(self):
        pass

    def __continueGame(self):
        pass

    def __bestScores(self):
        pass