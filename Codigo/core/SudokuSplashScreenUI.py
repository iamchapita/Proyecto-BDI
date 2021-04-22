# -*- coding: utf-8 -*-
from tkinter import *

from core.ScreenCenter import ScreenCenter
from core.SudokuLoginPageUI import SudokuLoginPageUI

"""
Frame que da la bienvenida al usuario.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuSplashScreenUI(Frame):

    
    # Constructor de la clase.
    def __init__(self):
        
        # Se declara un componente de tkinter.
        self.parent = Tk()
        # Se inicializa el Frame
        super().__init__(self.parent)
        self.pack()
        # Se inicializa los componente de la ventana.
        self.__initUI()
        # Se inicia el loop para mostrar la ventana.
        self.master.mainloop()

    # Creación de widgets de la ventana.
    def __initUI(self):

        # Se cargan imagenes a utilizar en la ventana.
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.backgroundImage = PhotoImage(file="core/images/WelcomeScreen.png", master=self.parent)
        # Se establece el titulo de la ventana.
        self.parent.title("Bienvenido")
        # Se bloquea la opción de cambiar de tamaño la ventana.
        self.parent.resizable(False, False)
        # Se establece el icono de la ventana.
        self.parent.iconphoto(True, self.icon)
        # Se Establece las dimensiones de la ventana utilizando las dimensiones de la imagen
        self.parent.geometry("%dx%d" % (self.backgroundImage.width(), self.backgroundImage.height()))
        # Se centra la ventana en la pantalla
        center = ScreenCenter()
        center.center(self.parent, self.backgroundImage.width(), self.backgroundImage.height())
        # Se crea un elemento canvas para colocar la imagen en la ventana
        canvas = Canvas(self, width=self.backgroundImage.width(), height=self.backgroundImage.height())
        # Se crea el lable que contiene la imagen de background
        labelLogo = Label(self,image=self.backgroundImage)
        # Se ubica el label en la ventana
        labelLogo.place(x=0, y=0, relwidth=1, relheight=1)
        # Se ubica el objeto canvas con el grid de tkinter
        canvas.grid(row=0, column=0)
        # Permite destruir la ventana y mostrar la ventana de inicio de sesión despues de 1 segundo.
        self.after(1000, self.goToLoginPage)
    
    # Función que permite continuar a la ventana de Login.
    def goToLoginPage(self):
        # Destruye la ventana actual
        self.parent.destroy()
        # Muestra la ventana de Login
        SudokuLoginPageUI()
        
    