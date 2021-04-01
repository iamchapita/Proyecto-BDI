from tkinter import *
from tkinter import messagebox
from core.screenCenter import ScreenCenter
from core.sudokuGame import SudokuGame
from core.sudokuBoardUI import SudokuBoardUI

class SudokuMainWindowUI(Frame):

    def __init__(self):

        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):

        self.width = 400
        self.height = 600
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.backgroundImage = PhotoImage(file="core/images/WhatDoYouWannaDo.png", master=self.parent)
        self.parent.title("Inicio")
        self.parent.resizable(False, False)
        self.parent.geometry("%dx%d" % (self.backgroundImage.width(), self.backgroundImage.height()))
        self.parent.iconphoto(True, self.logo)

        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)

        canvas = Canvas(self, width=self.backgroundImage.width(), height=self.backgroundImage.height())
        labelLogo = Label(self,image=self.backgroundImage)
        labelLogo.place(x=0, y=0, relwidth=1, relheight=1)
        canvas.grid(row=0, column=0)
        
        canvas.create_window(210, 200, window=Button(self, text="Nuevo Juego", command=self.__newGame))
        canvas.create_window(210, 250, window=Button(self, text="Continuar Juego", command=self.__continueGame))
        canvas.create_window(210, 300, window=Button(self, text="Mejores Puntajes", command=self.__bestScores))
        canvas.create_window(210, 350, window=Button(self, text="Salir", command=self.__logOff))

    def __newGame(self):
        with open('core/sudoku/n00b.sudoku', 'r') as boardFile:
            self.parent.destroy()
            root = Tk()
            game = SudokuGame(boardFile)
            game.start()
            SudokuBoardUI(root, game)

    def __continueGame(self):
        pass

    def __bestScores(self):
        pass

    def __logOff(self):
        messagebox.showinfo(title="Salir",message="¡Vuelve pronto!")
        self.parent.destroy()
