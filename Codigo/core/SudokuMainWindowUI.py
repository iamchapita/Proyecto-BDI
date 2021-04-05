from tkinter import *
from tkinter import messagebox
from core.ScreenCenter import ScreenCenter
from core.SudokuGame import SudokuGame
from core.SudokuBoardUI import SudokuBoardUI
from core.SudokuScoreboardUI import SudokuScoreboardUI
from core.DialogClose import DialogClose

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
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        self.width = 400
        self.height = 600
        self.parent.title('Opciones Usuario')
        self.parent.iconphoto(True, self.icon)

        self.parent.geometry("%dx%d" % (self.width, self.height))
        self.parent.configure(background = "#171717")
        self.parent.resizable(False, False)

        self.center = ScreenCenter()
        self.center.center(self.parent, self.width, self.height)

        label1= Label(self.parent, text='¿Qué deseas hacer?', font=("lato", 25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=60,y=120)

        Button(self.parent, text = 'Nuevo juego', bg="#6ea8d9", font=("lato", 17), command= self.__newGame).place(x=50, y=220, height = 50, width = 310)
        Button(self.parent, text = 'Continuar juego', bg="#6ea8d9", font=("lato", 17), command= self.__continueGame).place(x=50, y=280, height = 50, width =310)
        Button(self.parent, text = 'Mejores puntajes', bg="#6ea8d9", font=("lato", 17), command= self.__bestScores).place(x=50, y=340, height = 50, width =310)
        Button(self.parent, text = 'Salir', bg="#6ea8d9", font=("lato", 17), command= self.__onClosing).place(x=50, y=400, height = 50, width =310)
        
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.pack()
        label2.place(x=8,y=555)
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
        self.parent.withdraw()
        SudokuScoreboardUI(parent=self.parent)

    """
    Función que permite cerrar sesión al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __onClosing(self):
        self.dialogClose = DialogClose(self.parent)
        self.parent.wait_window(self.dialogClose)
