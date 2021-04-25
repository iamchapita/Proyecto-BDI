# -*- coding: utf-8 -*-
"""
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
from tkinter import *

from core.ScreenCenter import ScreenCenter

"""
Frame que muestra un pequeño mensaje de adios
cuando el usuario se sale por completo del juego.
"""
class SudokuBye(Frame):

    """
    Constructor de la clase.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self):

        self.parent = Tk()
        super().__init__(self.parent)
        self.__initUI()
        self.master.mainloop()

    """
    Creación de los widgets.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):
        # Se cargan las imagenes que use usarán en la ventana
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        self.parent.iconphoto(True, self.icon)
        # Se establece el titulo de la ventana
        self.parent.title('¡Adiós!')
        # Se definen los valores de ancho y alto para la ventana
        self.width = 400
        self.height = 300
        # Se establece las dimensiones de la ventana
        self.parent.geometry("%dx%d" % (self.width, self.height))
        # Se establece el color de background de la ventana
        self.parent.configure(background = "#171717")
        # Se bloquea la opción de cambiar el tamaño a la ventana
        self.parent.resizable(False, False)
        # Se centra la ventana en pantalla
        self.center = ScreenCenter()
        self.center.center(self.parent, self.width, self.height)
        # Se definen un label para mostrar el mensaje de despedida, se define la fuente a utilizar
        label1= Label(self.parent, text='¡Vuelve Pronto!', font=("lato", 25))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80, padx=2)
        # Se establece un label como contenedor de la imagen de la marca del juego.
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.grid(row=2,column=1,sticky = "nsew", padx=2)
        # Se establece la cantidad de tiempo durante la cual debe mostrarse
        self.after(500,self.parent.destroy)
