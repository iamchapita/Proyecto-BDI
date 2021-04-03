from tkinter import *
from tkinter import ttk
from core.ScreenCenter import ScreenCenter
import os
import re

"""
Frame que permite visualizar todos los scoreboards del juego.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuScoreboardUI(Frame):

    """
    Constructor de la clase.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self):

        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    """
    Creación de widgets de la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):

        self.width = 960
        self.height = 545
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.parent.title("Scoreboard")
        self.parent.resizable(False, False)
        self.parent.geometry("%dx%d"%(self.width, self.height))
        self.parent.iconphoto(True, self.logo)
        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)
        self.dataView = ttk.Treeview(self.parent, columns=("#1","#2","#3"))
        self.dataView.pack()
        self.dataView.heading("#0", text="Indice")
        self.dataView.heading("#1", text="Usuario")
        self.dataView.heading("#2", text="Mejor Tiempo")
        self.dataView.heading("#3", text="Fecha y Hora")
        self.dataView.place(x=40, y=140)
        self.dataView.column("#0", width=100)
        self.dataView.column("#1", width=200)
        self.dataView.column("#2", width=250)
        self.dataView.column("#3", width=300)
        self.loadText()

    """
    Función que permite leer los mejores puntajes provenientes de una 
    consulta de la base de datos e insertarlos en una tabla de tkinter.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def loadText(self):
        os.chdir("../Scripts de Base de Datos")
        with open("scoreboardTest.txt", "r") as file:
            test = list(zip(*map(str.split, map(str.strip, file))))
            for first in test[0]:
                for second in test[1]:
                    for third in test[2]:
                        self.dataView.insert("", 0, text="N° ", values=(first,second,third))

