from tkinter import *
import sys
from core.ScreenCenter import ScreenCenter
from core.SudokuByeUI import SudokuBye

"""
Clase DialogClose genera una caja de texto de confirmación con las 
opciones de  de salida de la aplicación y minimizar pantalla.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class DialogClose:

    """
    Constructor de la clase.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.parent = parent
        self.top.configure(background = "#171717")
        self.top.title("Salir")

        self.center= ScreenCenter()
        self.center.center(self.top, 150, 490)

        label1 = Label(self.top, text="¿Está seguro?",font =("Lato",15))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=0, column=0, columnspan=2)

        self.button1 = Button(self.top, text="Si, salir del juego.", bg="#6ea8d9", font=("Lato",12), command=self.__salir)
        self.button1.grid(row=1, column=0, padx=5, pady=5)

    """
    Función que muestra una ventana y preguntar si el usuario se quiere
    salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __salir(self):
        self.top.destroy()
        self.parent.destroy()
        SudokuBye()
        sys.exit()