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
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        self.width = 400
        self.height = 600
        self.parent.title('Menu')
        self.parent.iconphoto(True, self.icon)

        self.parent.geometry("%dx%d" % (self.width, self.height))
        self.parent.configure(background = "#171717")
        self.parent.resizable(False, False)

        self.center = ScreenCenter()
        self.center.center(self.parent, self.width, self.height)

        label1= Label(self.parent, text='¿Qué deseas hacer?', font=("lato", 20))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80, padx=70)

        Button(self.parent, text = 'Nuevo juego', bg="#6ea8d9", font=("lato", 17), command= self.__newGame).grid(row=2,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=37)
        Button(self.parent, text = 'Continuar juego', bg="#6ea8d9", font=("lato", 17), command= self.__continueGame).grid(row=3,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=18)
        Button(self.parent, text = 'Mejores puntajes', bg="#6ea8d9", font=("lato", 17), command= self.__bestScores).grid(row=4,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=11)
        Button(self.parent, text = 'Salir', bg="#6ea8d9", font=("lato", 17), command= self.__onClosing).grid(row=5,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=83)
        
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.grid(row=6,column=1,pady = 130)
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
        # Bloque try except para manejar la excepción devuelta si el self.parent fue destruido
        try:
            # Confirma si la instancia de dialogClose existe
            if (self.dialogClose.winfo_exists() == False):
                # Si no existe entonces establece de nuevo la función de apertura de dialogClose cuando
                # se intenta cerrar la ventana
                self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        except:
            pass
