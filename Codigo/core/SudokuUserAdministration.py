# -*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter import ttk

from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.ScreenCenter import ScreenCenter
from core.SudokuAdministratorCreateUser import *
from core.SudokuByeUI import SudokuBye
from core.SudokuUserList import *

"""
Frame que permite visualizar la administración de los usuario registrados
en el juego así mismo como en la BD.
Se incluye la opción de crear un usuario.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuUserAdministration(Frame):

    # Constructor de la clase donde si incializan todos los componentes de la ventana.
    def __init__(self, parent):
        self.parent=parent
        # Se crea otro componente Tk
        self.child = Tk()
        # Se captura el evento de cerrado de la venana y se redirige hacia la función
        # __onClosing
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        self.__initUI()

    # Creación de los widgets que se veran en pantalla.
    def __initUI(self):

        # Se cargan las imagenes a usar en la interfaz
        self.img = PhotoImage(file="core/images/back.png", master=self.child)
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)

        # Se establecen los valores de ancho y alto de la ventana
        self.width = 400
        self.height = 600

        # Se establece el titulo y le icono de la ventana
        self.child.title('Administración de usuarios')
        self.child.iconphoto(True, self.icon)

        # Se establecen las dimensiones de la ventana
        self.child.geometry("%dx%d" % (self.width, self.height))

        # Se configura el color del background de la ventana
        self.child.configure(background = "#171717")

        # Se elimina la opción de cambiar el tamaño a la ventana
        self.child.resizable(False, False)

        # Se centra la ventana
        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)

        # Se crean label para dar contexto a la vetana
        label1= Label(self.child, text='Administrar usuarios', font=("Lato",20))
        
        # Se configura un label para contenedor de una imagen
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)

        # Se agrega configuracion de color al label
        label1.configure(background = "#171717", fg="white")

        # Se ubica los labels en la ventana utilizando el grid de tkinter
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80, padx=70)
        labelBrand.grid(row=8, column=1, pady=180)
        
        # Se crean botones
        self.createUserButton = Button(self.child, text='Crear usuario', command=self.__goCreateUser)
        self.listUsersButton = Button(self.child, text='Lista de Usuarios', command=self.__listUsers)
        self.backButton = Button(self.child, text='Atrás', command=self.__goBack)

        # Se configura el color de fondo y fuente de los botones
        self.listUsersButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.createUserButton.configure(bg="#6ea8d9", font=("Lato", 17))

        # Se configura la imagen, el color de fondo, ancho del borde en el botón 
        self.backButton.configure(image=self.img, bg="#171717", borderwidth=0, highlightthickness=0)
        
        # Se establece el foco al botón
        self.createUserButton.focus_set()
        
        # Se ubica los botones en la ventana usando el grid de tkinter
        self.createUserButton.grid(row=3, column=1, sticky="nsew", pady=5, padx=80, ipadx=37)
        self.listUsersButton.grid(row=4,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=18)
        self.backButton.grid(row=0, column=1, sticky="nsew", pady=10)

    
    # Muestra la ventana para crear un usuario y registrarlo en la base de datos.
    def __goCreateUser(self):
        # Se oculta la ventana actual
        self.child.withdraw()
        # Se instancia la nueva ventana
        SudokuAdministratorCreateUser(parent=self.child)
    
    # Función que permite regresar a la ventana anterior al presionar el botón.
    def __goBack(self):
        # Destruye la ventana actuak
        self.child.destroy()
        # Muestra la ventana anterior
        self.parent.deiconify()

    # Muestra la ventana de administración de usuarios
    def __listUsers(self):
        # Se oculta la ventana actual
        self.child.withdraw()
        # Se instancia la nueva ventana
        SudokuUserList(self.child)

    # Función ejecutada cada vez que se intenta cerrar la ventana. 
    # Se muestra una ventana que solicita al usuario confirmación de cierre.
    def __onClosing(self):
        # Se muestra una ventana de confirmación
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            # Se destruye la ventana actual.
            self.child.destroy()
            # Se cierra la ejecución de la aplicación
            sys.exit()
            # Se muestra una ventana de despedida.
            SudokuBye()
        else:
            pass
