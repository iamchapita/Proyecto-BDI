from tkinter import *
from tkinter import ttk
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose
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
    def __init__(self, parent):
        self.parent = parent
        self.child = Tk()
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        self.pack()
        img = PhotoImage(file="core/images/back.png", master=self.child)
        btnBack= Button(self.child, image=img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        btnBack.pack()
        btnBack.place(x=850, y=20)
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
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.child.title("Scoreboard")
        self.child.resizable(False, False)
        self.child.configure(background = "#171717")
        self.child.geometry("%dx%d"%(self.width, self.height))
        self.child.iconphoto(True, self.logo)
        center = ScreenCenter()
        center.center(self.child, self.width, self.height)
        self.dataView = ttk.Treeview(self.child, columns=("#1","#2","#3"))
        self.dataView.pack()
        self.dataView.heading("#0", text="Indice")
        self.dataView.heading("#1", text="Usuario")
        self.dataView.heading("#2", text="Mejor Tiempo")
        self.dataView.heading("#3", text="Fecha y Hora")
        self.dataView.place(x=40, y=160)
        self.dataView.column("#0", width=100)
        self.dataView.column("#1", width=200)
        self.dataView.column("#2", width=250)
        self.dataView.column("#3", width=300)

        # Muestra el titulo de la seccion
        label1= Label(self.child, text='Score Board', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=380,y=90)

        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=280,y=485)
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
                        os.chdir("../Codigo")

    
    """
    Función que permite regresar a la ventana anterior al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()

    """
    Función que permite minimizar o salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __onClosing(self):
        self.dialogClose = DialogClose(self.parent)
        self.parent.wait_window(self.dialogClose)
