# -*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter import ttk
from core.ScreenCenter import ScreenCenter
from core.SudokuAdministratorCreateUser import *
from core.SudokuAdministratorDeleteUser import *
from core.SudokuUserList import *
from core.SudokuByeUI import SudokuBye
from core.EngineSQL.MySQLToolConnection import ToolConnection


"""
Frame que permite visualizar la administración de los usuario registrados
en el juego así mismo como en la BD.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuUserAdministration(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self, parent):
        self.parent=parent
        self.child = Tk()
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        self.__initUI()

    """
    Creación de los widgets que se veran en pantalla.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):

        self.img = PhotoImage(file="core/images/back.png", master=self.child)
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.width = 400
        self.height = 600
        self.child.title('Administración de usuarios')
        self.child.iconphoto(True, self.icon)
        # Tamaño de la ventana
        self.child.geometry("%dx%d" % (self.width, self.height))

        self.child.configure(background = "#171717")
        self.child.resizable(False, False)
        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)
        
        label1= Label(self.child, text='Administrar usuarios', font=("Lato",20))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80, padx=70)

        self.createUserButton = Button(self.child, text='Crear usuario', command=self.__goCreateUser)
        self.createUserButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.createUserButton.focus_set()
        self.createUserButton.grid(row=3, column=1, sticky="nsew", pady=5, padx=80, ipadx=37)
            
        self.listUsersButton = Button(self.child, text='Lista de Usuarios', command=self.__listUsers)
        self.listUsersButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.listUsersButton.grid(row=4,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=18)
        
        self.backButton = Button(self.child, text='Atrás', command=self.__goBack)
        self.backButton.configure(image=self.img, bg="#171717", borderwidth=0, highlightthickness=0)
        self.backButton.grid(row=0, column=1, sticky="nsew", pady=10)
        
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.grid(row=8, column=1, pady=180)
    
    """
    Función que permite abrir una ventana para crear un usuario y registrarlo
    en la base de datos.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goCreateUser(self):
        self.child.withdraw()
        SudokuAdministratorCreateUser(parent=self.child)
    """
    Función que permite regresar a la ventana anterior al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()

    def __listUsers(self):
        self.child.withdraw()
        SudokuUserList(self.child)

    """
    Función que pregunta al usuario si desea salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 3.0
    """
    def __onClosing(self):
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            
            self.child.destroy()
            sys.exit()
            SudokuBye()
        else:
            pass