from tkinter import *
from tkinter import messagebox
from core.ScreenCenter import ScreenCenter
from core.SudokuGame import SudokuGame
from core.SudokuBoardUI import SudokuBoardUI
from core.SudokuScoreboardUI import SudokuScoreboardUI

"""
Frame que muestra el Main Window y todos sus respectivos widgets de la aplicación
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuMainWindowUI(Frame):

    """
    Constructor de la clase.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self):

        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    """
    Creación de widgets de la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
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
        
        canvas.create_window(205, 250, window=Button(self, text="Nuevo Juego", bg="#6ea8d9",width=15, height=2, command=self.__newGame))
        canvas.create_window(205, 310, window=Button(self, text="Continuar Juego", bg="#6ea8d9",width=15, height=2, command=self.__continueGame))
        canvas.create_window(205, 370, window=Button(self, text="Mejores Puntajes", bg="#6ea8d9",width=15, height=2, command=self.__bestScores))
        canvas.create_window(205, 430, window=Button(self, text="Salir", width=15, bg="#6ea8d9",height=2, command=self.__logOff))

    """
    Función que inicia el juego cuando se presiona el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __newGame(self):
        with open('core/sudoku/n00b.sudoku', 'r') as boardFile:
            self.parent.destroy()
            root = Tk()
            game = SudokuGame(boardFile)
            game.start()
            SudokuBoardUI(root, game)

    """
    Función que permite continuar un juego pausado.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __continueGame(self):
        pass

    """
    Función que permite visualizar los mejores puntajes.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __bestScores(self):
        self.parent.destroy()
        SudokuScoreboardUI()

    """
    Función que permite cerrar sesión al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __logOff(self):
        messagebox.showinfo(title="Salir",message="¡Vuelve pronto!")
        self.parent.destroy()
