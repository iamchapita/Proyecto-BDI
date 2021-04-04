"""
    @author: gehernandezc@unah.hn
    @version: 1.0
    @date 2021/04/03
"""

from tkinter import *
import sys
from core.ScreenCenter import ScreenCenter

"""
    Clase DialogClose genera una caja de texto de confirmación con las opciones de  de salida de la aplicación y minimizar pantalla.
"""
class DialogClose:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.parent = parent
        self.top.configure(background = "#171717")
        self.top.title("Salir")

        self.center= ScreenCenter()
        self.center.center(self.top, 330, 400)

        label1 = Label(self.top, text="¿Está seguro?",font =("Lato",15))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=0, column=0, columnspan=2)

        self.button1 = Button(self.top, text="Si, salir del juego.", bg="#6ea8d9", font=("Lato",12), command=self.__salir)
        self.button2 = Button(self.top, text="No, solo minimizar.", bg="#6ea8d9", font=("Lato",12), command=self.__minimizar)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.button2.grid(row=1, column=1, padx=5, pady=5)

    def __salir(self):
        self.top.destroy()
        self.parent.destroy()
        sys.exit()

    def __minimizar(self):
        self.top.destroy()
        self.parent.iconify()