from tkinter import *
from tkinter import ttk
from core.sudokuBoardUI import SudokuBoardUI
from core.sudokuMainWindowUI import SudokuMainWindowUI
from core.screenCenter import *

class SudokuLoginPageUI(ttk.Frame):

    def __init__(self, parent=None):
        if not parent:
            parent = Tk()
            parent.title("Inicio de Sesión")
            parent.resizable(FALSE, FALSE)

        super().__init__(parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        self.margin = 70 
        self.side = 50
        self.width = self.margin * 2 + self.side * 9
        self.height = self.margin * 2 + self.side * 9 + 120 
        #self.center = ScreenCenter()
        #self.center.center(parent)
        #self.parent.configure(background = "white")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self, width = self.width, height = self.height)
        #self.canvas.configure(background="white")
        self.canvas.pack(fill=BOTH, side=TOP)
        # Investigar como usar un GRID para ubicar objetos
        # en las ventanas
        # Se usa coordenadas para ubicar objetos en la ventana
        ttk.Label(self, text="Nombre de Usuario").place(x=200, y=20)
        ttk.Entry(self).place(x=200, y=50)
        ttk.Label(self, text="Contraseña").place(x=200, y=70)
        ttk.Entry(self).place(x=200, y=90)
        ttk.Button(self, text="Iniciar Sesión", command = self.__onClick).place(x=200, y=120)

    def __onClick(self):
        self.destroy()
        SudokuMainWindowUI(self.master)