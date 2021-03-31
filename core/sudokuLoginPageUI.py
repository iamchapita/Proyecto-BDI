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
        self.pack(fill=BOTH)
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):

        # Investigar como usar un GRID para ubicar objetos
        # en las ventanas
        # Se usa coordenadas para ubicar objetos en la ventana
        
        self.logoImage = PhotoImage(file = "core/images/SudokuLogo.png")
        canvasObject = Canvas(self,height=700, width=400)
        l_logo = Label(self,image=self.logoImage)
        l_logo.place(x=-45, y=150, relwidth=1, relheight=1)
        canvasObject.pack()

        ttk.Label(self, text="Nombre de Usuario",font=("Calibri","20")).place(x=80, y=150)
        ttk.Entry(self).place(x=120, y=190)
        ttk.Label(self, text="Contraseña",font=("Calibri","20")).place(x=120, y=250)
        ttk.Entry(self).place(x=120, y=290)
        ttk.Button(self, text="Iniciar Sesión", command = self.__onClick).place(x=155, y=330)

    def __onClick(self):
        self.destroy()
        SudokuMainWindowUI(self.master)