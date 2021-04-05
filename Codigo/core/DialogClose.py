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
class DialogClose(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self)
        self.parent = parent
        # Obliga al parent a permanecer congelado hasta que la ventana DialogClose se cierre
        self.grab_set()
        self.configure(background = "#171717")
        self.title("Salir")

        self.center= ScreenCenter()
        self.center.center(self, 150, 490)

        label1 = Label(self, text="¿Está seguro?",font =("Lato",15))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=0, column=0, columnspan=2)

        self.button1 = Button(self, text="Si", bg="#6ea8d9", font=("Lato",12), command=self.__getOut)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.button2 = Button(self, text="No", bg="#6ea8d9", font=("Lato",12), command=self.__cancel)
        self.button2.grid(row=1, column=2, padx=5, pady=5)

    """
    Función que muestra una ventana y preguntar si el usuario se quiere
    salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __getOut(self):
        self.destroy()
        self.parent.destroy()
        SudokuBye()
        sys.exit()
    
    def __cancel(self):
        self.destroy()