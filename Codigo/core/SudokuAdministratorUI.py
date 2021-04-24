# -*- coding: utf-8 -*-
"""
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
import os
from tkinter import *
from tkinter import messagebox

from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.ScreenCenter import ScreenCenter
from core.SudokuAdministratorBinnacle import *
from core.SudokuAdministratorGame import SudokuAdministratorGame
from core.SudokuBoardUI import SudokuBoardUI
from core.SudokuByeUI import SudokuBye
from core.SudokuGame import SudokuGame
from core.SudokuUserAdministration import *

"""
Frame que permite visualizar las opciones de un usuario que tiene como
rol administrador.
"""
class SudokuAdministratorUI(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    """
    def __init__(self):
        # Instancia de la ventana padre.
        self.parent = Tk()
        # Se inicializa un nuevo componente de tkinter
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)
        
        # Creación de variables globales
        self.idBoard = None #Numero del board seleccionado
        self.username = ""
        self.idUsername = None

        # Instancia para obtener el nombre de usuario log
        self.getUsernameLogin()   
        self.__initUI()
        self.master.mainloop()

    """
    Creación de los widgets que se veran en pantalla.
    """
    def __initUI(self):
        # Se cargan las imagenes que use usarán en la ventana
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        # Se establece el titulo de la ventana
        self.parent.title('Opciones Administrador')
        # Establece el ícono de la ventana.
        self.parent.iconphoto(True, self.icon)
        # Se definen los valores de ancho y alto para la ventana
        self.width = 400
        self.height = 600

        # Se establece las dimensiones de la ventana
        self.parent.geometry("%dx%d" % (self.width, self.height))
        # Se establece el color de background de la ventana
        self.parent.configure(background = "#171717")
        # Se bloquea la opción de cambiar el tamaño a la ventana
        self.parent.resizable(False, False)

        # Se establecen tipos y tamaños de letras
        TitleStyles = tkFont.Font(family="Lato", size=20)
        ButtonStyles = tkFont.Font(family="Lato", size=17)

        # Se centra la ventana en pantalla
        self.center = ScreenCenter()
        self.center.center(self.parent, self.width, self.height)

        # Se definen un label para mostrar el titulo de la ventana, se define la fuente a utilizar
        label1= Label(self.parent, text='¿Qué deseas hacer?', font=TitleStyles)
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80,padx=70)

        # Se crea botón y sus caracteristicas para ir a la ventana de administración de usuarios.
        self.manageUsersButton = Button(self.parent, text = 'Administración usuarios', command= self.__goUserAdministration)
        self.manageUsersButton.configure(bg="#6ea8d9", font=ButtonStyles)
        self.manageUsersButton.focus_set()
        self.manageUsersButton.grid(row=2, column=1, sticky="nsew", pady=5, padx=40)
        
        # Se crea botón y sus caracteristicas para ir a las opciones del juego
        self.goToGameButton = Button(self.parent, text = 'Jugar', command= self.__goMainGame)
        self.goToGameButton.configure(bg="#6ea8d9", font=ButtonStyles)
        self.goToGameButton.grid(row=3,column=1,sticky = "nsew", pady = 5, padx=40)

        # Se crea botón y sus caracteristicas para ver la bitácora
        self.binacleButton = Button(self.parent, text='Bitácora', command=self.__goBinnacle)
        self.binacleButton.grid(row=4,column=1,sticky = "nsew", pady = 5, padx=40)
        self.binacleButton.configure(bg="#6ea8d9", font=ButtonStyles)

        # Se crea botón y sus caracteristicas para salir del programa
        self.exitButton = Button(self.parent, text='Salir', command=self.__onClosing)
        self.exitButton.grid(row=5,column=1,sticky = "nsew", pady = 5, padx=40)
        self.exitButton.configure(bg="#6ea8d9", font=ButtonStyles)
        
        # Se establece un label como contenedor de la imagen de la marca del juego.
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.grid(row=6,column=1,pady = 155)

    """
    Función que abre una nueva ventada en donde se pueden administrar los
    usuarios registrados en el juego y la BD.
    """
    def __goUserAdministration(self):
        self.parent.withdraw()
        SudokuUserAdministration(parent=self.parent)

    """
    Función que abre una nueva ventada para visualizar la bitacora.
    """
    def __goBinnacle(self):
        self.parent.withdraw()
        SudokuAdministratorBinnacle(parent=self.parent)

    """
    Función que le permite al administrador jugar.
    """
    def __goMainGame(self):
        self.parent.withdraw()
        SudokuAdministratorGame(parent = self.parent)

    """
    Función que pregunta al usuario si desea salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 3.0
    """
    def __onClosing(self):
        # Confirmación sobre cerrado de la aplicación
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            # Se destruye la ventana actual
            self.parent.destroy()
            # Se termina la ejecución del programa 
            sys.exit()
            # Se muestra la ventana de despedida
            SudokuBye()
        else:
            pass

    
    """
        Función que asigna los valores de inicio de sesión del usuario 
        logeado (id, username)
    """
    def getUsernameLogin(self) -> None:
        # Retorna la información de id, nombre de usuario y rol del usuario loggeado
        self.idUsername, self.username, self.rol = (ToolConnection()).getLastLoginUser()
