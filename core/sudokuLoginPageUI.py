from tkinter import *
from PIL import Image
from core.sudokuMainWindowUI import SudokuMainWindowUI
from core.screenCenter import *

class SudokuLoginPageUI(Frame):

    def __init__(self):
        
        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):

        # Investigar como usar un GRID para ubicar objetos
        # en las ventanas
        # Se usa coordenadas para ubicar objetos en la ventana
        self.width = 400
        self.height = 600
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.parent.title("Inicio de Sesión")
        self.parent.resizable(False, False)
        self.parent.geometry("%dx%d"%(self.width, self.height))
        self.parent.iconphoto(True, self.logo)
        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)
        canvas = Canvas(self, width=self.width, height=self.height)
        canvas.pack(fill=BOTH, expand = True)
        canvas.create_image(200, 300, image=self.logo)
        # NO HAY TRANSPARENCIAS PARA EL BACKGROUND DEL LABEL :) ODIO Tkinter, Amo pyQt5
        canvas.create_window(200, 50, window=Label(self,text="Inicio de Sesión",font=("Calibri","20")))
        canvas.create_window(200, 150, window=Label(self, text="Nombre de Usuario",font=("Calibri","20")))
        canvas.create_window(200, 190, window=Entry(self))
        canvas.create_window(200, 250, window=Label(self, text="Contraseña", font=("Calibri", "20")))
        canvas.create_window(200, 290, window=Entry(self).place(x=120, y=290))
        canvas.create_window(200, 430, window=Button(self, text="Iniciar Sesión", command = self.__onClick))

    def __onClick(self):
        self.destroy()
        SudokuMainWindowUI(self.master)