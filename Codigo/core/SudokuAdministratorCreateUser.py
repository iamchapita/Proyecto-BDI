# -*- coding: utf-8 -*-
"""
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
import os
import re
import tkinter.font as tkFont
from tkinter import *

from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.FileManipulation.EncryptDecrypt import EncryptDecryptSudokuFile
from core.ScreenCenter import ScreenCenter
from core.SudokuByeUI import SudokuBye

"""
Frame que permite visualizar los elementos cuando un usuario se crea
y se registra en el juego y la BD.
"""
class SudokuAdministratorCreateUser(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    """
    def __init__(self, parent):
        # Instancia de la ventana padre.
        self.parent = parent
        # Se inicializa un nuevo componente de tkinter
        self.child = Tk()
        # Se captura el evento de cierre de una ventana y se ejecuta la función __onClosing.
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        # Conexión al archivo de configuración
        self.config = ConfigConnection() 
        # Conexión a la base de datos
        self.db = MySQLEngine(self.config.getConfig())
        self.__initUI()

    """
    Creación de los widgets que se veran en pantalla.
    """

    # Creación de los widgets que se veran en pantalla.
    def __initUI(self):
        # Se cargan las imagenes que use usarán en la ventana
        self.img = PhotoImage(file="core/images/back.png", master=self.child)
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        
        # Se crea el botón de regreso y establece la imagen
        self.backButton= Button(self.child, image=self.img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        self.backButton.grid(row=0,column=1,sticky = "nsew", pady=10)

        # Establece el ícono de la ventana.
        self.child.iconphoto(True, self.icon)

        # Se definen los valores de ancho y alto para la ventana
        self.width = 400
        self.height = 600

        # Se centra la ventana en pantalla
        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)

        # Se establece el titulo de la ventana
        self.child.title('Crear Usuarios')
        # Se establece las dimensiones de la ventana
        self.child.geometry("%dx%d" %(self.width, self.height))
        # Se establece el color de background de la ventana
        self.child.configure(background = "#171717")
        # Se bloquea la opción de cambiar el tamaño a la ventana
        self.child.resizable(False, False)

        # Se definen un label para mostrar el titulo de la ventana, se define la fuente a utilizar
        label1= Label(self.child, text='Crear un nuevo usuario', font=("Lato",20))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 50,padx=35)

        # Se define un label para mostrar el titulo del entry, se define la fuente a utilizar
        label2= Label(self.child, text='Introduzca el nombre de usuario:', font =("Lato",15))
        label2.configure(background = "#171717", fg="#6ea8d9")
        label2.grid(row=2,column=1, pady = 20,padx=35)

        # Se define el entry para ingresar el número de usuario.
        self.usernameEntry = Entry(self.child, font=("Lato",13),  justify=CENTER)
        self.usernameEntry.grid(row=3,column=1, padx=35, ipady=6, ipadx=15)
        
        # Se crea el botón con sus configuraciones
        Button(self.child, text = 'Crear', command= self.__save, bg="#6ea8d9", font=("Lato",15)).grid(row=4,column=1, pady = 15,padx=35,ipadx=40)
        
        # Se establece un label como contenedor de la imagen de la marca del juego.
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.grid(row=6,column=1, pady = 155)

    """
    Esta función verifica la existencia de un usuario en la base de datos, sí este usaurio no existe, lo crea, 
    generando una clave cifrada a partir del nombre del usuario. La primera vez que el usuario inicia sesión al 
    sistema, el sistema lo obliga a cambiar de contraseña.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.1
    @date 2021/04/06
    """
    def __save(self):
        
        error = ""

        # Si el campo está vacío
        if (len(self.usernameEntry.get()) == 0):
            error += "El campo de usuario está vacío."

        #Sí el text no está vacío
        else:
            
            # Buscando si el nombre de usuario existe en la BD
            userExist = self.db.select("SELECT tex_nickname FROM User WHERE tex_nickname = %s", (self.usernameEntry.get(),))
            
            # Si el campo no cumple con la expresión regular
            if (re.fullmatch(r"(?=.*[a-zA-Z])[a-zA-Z\d]{4,30}$", self.usernameEntry.get()) is None):
                error += "El nombre de usuario no es válido."

            # Si existe entonces error
            if(userExist):
                error += "El nombre de usuario no está disponible."
        
        # Si la longitud de error es mayor que 0 entonces
        if (len(error) > 0):
            messagebox.showwarning(title="Error", message=error)
            # Limpiando Entry
            self.usernameEntry.delete(0, "end") 
            return
        
        else:
            # Encriptación de la contraseña 
            encryptPassword = (EncryptDecryptSudokuFile(self.db)).encrypt(self.usernameEntry.get(), self.usernameEntry.get())

            # Se inserta en la base de datos
            self.db.insert(
                table="User", 
                fields=["tex_nickname", "tex_password"], 
                values=[
                    self.usernameEntry.get(), 
                    encryptPassword
                    ]
            )
            # Se limpia el entry
            self.usernameEntry.delete(0, "end")
            # Se muestra mensaje de Confirmación
            messagebox.showinfo(title="Éxito", message="El usuario fue creado satisfactoriamente.")

    """
    Función que permite regresar a la ventana anterior al presionar el botón.
    """
    def __goBack(self):
        # Se cierra la conexión a la base de datos.
        self.db.closeConnection() 
        # Se cierra la ventana actual.
        self.child.destroy()
        # Se muestra la ventana "padre" (ventana anterior).
        self.parent.deiconify()

    """
    Función que pregunta al usuario si desea salir del juego y cierra la 
    conexión a la base de datos.
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
            self.child.destroy()        
            # Se cierra la conexión a la base de datos.
            self.db.closeConnection() 
            # Se termina la ejecución del programa 
            sys.exit()
            # Se muestra la ventana de despedida
            SudokuBye()
        else:
            pass
