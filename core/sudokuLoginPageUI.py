from tkinter import *
from core.sudokuBoardUI import SudokuBoardUI
from core.screenCenter import *

class SudokuLoginPageUI(Frame):

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
        self.parent.title("Inicio de Sesión")
        self.parent.resizable(FALSE, FALSE)
        self.parent.configure(background = "white")
        self.pack(fill=BOTH)
        self.canvas = Canvas(parent, width = self.width, height = self.height)
        self.canvas.configure(background="white")
        self.canvas.pack(fill=BOTH, side=TOP)
        # Investigar como usar un GRID para ubicar objetos
        # en las ventanas
        # Se usa coordenadas para ubicar objetos en la ventana
        userLabel = Label(parent, text="Nombre de Usuario")
        userLabel.place(x=200, y=20)
        userEntry = Entry(parent)
        userEntry.place(x=200, y=50)
        passwordLabel = Label(parent, text="Contraseña")
        passwordLabel.place(x=200, y=70)
        passwordEntry = Entry(parent)
        passwordLabel.place(x=200, y=90)
        loginButton = Button(parent, text="Iniciar Sesión", command = self.__onClick)
        loginButton.place(x=200, y=120)

    def __onClick(self):
        pass