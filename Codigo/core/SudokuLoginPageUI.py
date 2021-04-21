# -*- coding: utf-8 -*-
import re
from tkinter import *
from tkinter import messagebox

from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.ScreenCenter import ScreenCenter
from core.SudokuAdministratorUI import SudokuAdministratorUI
from core.SudokuByeUI import SudokuBye
from core.SudokuChangeUserPassword import SudokuChangeUserPassword
from core.SudokuMainWindowUI import SudokuMainWindowUI
from core.Tooltip import Tooltip

"""
Clase que contiene la definición de todos los componentes correspondiente al apartado de Login
de la aplicación, ya sea backend y frontend. 
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuLoginPageUI(Frame):

    # Constructor de la clase
    def __init__(self):

        # Se inicializa un componente del Framework Tkinter.
        self.parent = Tk()
        # Se captura el evento de cierre de una ventana y se ejecuta la función __onClosing.
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        # Se inicialiaza la clase Padre (Frame) y se le pasa como parámetro el parent.
        super().__init__(self.parent)
        # Se genera una instancia de la clase que contiene los métodos para obtener
        # los parámetros necesarios para realizar la conexión a la base de datos.
        self.config = ConfigConnection()
        # Se genera una instancia de la clase que contiene los métodos para realizar operaciones
        # sobre la base de datos, se le envía como parámetro la configuración .
        self.db = MySQLEngine(self.config.getConfig())
        # Se llama a la función en donde se crean los widgets.
        self.__initUI()

    # Creación de los widgets que se veran en pantalla.
    def __initUI(self):

        # Se establece el alto y ancho de la ventana.
        self.width = 400
        self.height = 600
        # Se cargan las imagenes a mostrar en el background de la ventana.
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.backgroundImage = PhotoImage(file="core/images/LoginScreen.png", master=self.parent)
        # Se establece el titulo de la ventana.
        self.parent.title("Inicio de Sesión")
        # Se bloquea la opción de cambiar de tamaño la ventana.
        self.parent.resizable(False, False)
        # Se establece la dimensión de la ventana.
        self.parent.geometry("%dx%d"%(self.width, self.height))
        # Se establece el icono de la ventana, mostrado en la barra de la ventana.
        self.parent.iconphoto(True, self.logo)
        # Se establece un color fijo para el background de la ventana.
        self.parent.configure(background = "#171717")
        
        center = ScreenCenter()
        # Se utiliza el método center para ubicar la ventana en el centro de la pantalla.
        center.center(self.parent, self.width, self.height)
        
        # Se instancian los Label necesarios
        # Se envía como parámetros:
        # - El componente donde va a aparecer el widget.
        # - El texto que contendrá el label.
        # - Fuente de texto utilizada para mostrar el texto.
        label1= Label(self.parent, text='Nombre de usuario', font=("Lato",20))
        label2= Label(self.parent, text='Contraseña', font =("Lato",20))

        # Se configura el color del background del label
        # Se configura el color del texto del label.
        label1.configure(background = "#171717", fg="white")
        label2.configure(background = "#171717", fg="white")

        # Se utiliza grid para ubicar los label en el espacio de la ventana.
        label1.grid(row=1,column=1,sticky = "nsew", pady = 20, padx=75)
        label2.grid(row=3,column=1,sticky = "nsew", pady = 20, padx=120)

        # Se generá un Entry para el nombre de usuario y la contraseña.
        # Se envían como parámetros:
        # - El componente donde va a pintarse el Entry.
        # - La fuente y el tamaño de la fuente.
        # - La alineación del texto dentro del entry.
        self.usernameEntry = Entry(self.parent, font=("Lato",15),  justify=CENTER)
        # Se envía el parámetro show = "*" para ofuscar el texto que pertenece a la contraseña.
        self.passwordEntry = Entry(self.parent, show="*", font=("Lato",15),  justify=CENTER)

        # Se declara una varible que se usará como parte del tooltip.
        textTooltip ="Ingrese {}"

        # Se genera el respectivo tooltip apra cada entry.
        self.usernameToolTip = Tooltip(self.usernameEntry, textTooltip.format("el nombre de usuario."))
        self.usernameToolTip = Tooltip(self.passwordEntry, textTooltip.format("la contraseña."))

        # Se establece el foco al Entry que pertecene al nombre del usuario.
        self.usernameEntry.focus()

        # Se ubican los Entry en la ventana, utilizando el grid proporcionado por tkinter.
        self.usernameEntry.grid(row=2,column=1,sticky = "nsew", padx=70)
        self.passwordEntry.grid(row=4,column=1,sticky = "nsew", padx=70)
        
        # Se crea el botón para realizar la operación de Inicio de Sesión.
        # Se envía como parámetro:
        # - El componente donde se mostrará el botón.
        # - La función a ejecutar cuando se presione el botón, recibe como parámetro:
        #       - El texto del Entry que corresponde al nombre de usuario.
        #       - El texto del Entry que corresponde a la contraseña.
        self.loginButton = Button(self.parent, command=lambda: self.__loginFn(self.usernameEntry.get(), self.passwordEntry.get()))

        # Se configura el botón:
        # - Se establece el texto del botón.
        # - Se establece el color del background del botón.
        # - Se establece la fuente del texto del botón.
        self.loginButton.configure(text="Iniciar Sesión", bg="#6ea8d9", font=("Lato", 15))

        # Se usa grid de Tkinter para ubicar el botón en el espacio de la ventana.
        self.loginButton.grid(row=5,column=1,sticky = "nsew", pady = 20, padx=120)

        # Se utiliza un label para mostrar y ubicar una imagen en el background de la ventana.
        labelbackgroundImage = Label(self.parent, image=self.backgroundImage, borderwidth=0)
        labelbackgroundImage.grid(row=6,column=1,sticky = "nsew", pady = 50, padx=4)

    
    # Se encarga de la comprobación del texto de los Entry, comprobación de credenciales y 
    # llevar el usuario a la respectiva ventana principal.
    # Recibe como parámetros:
    # - Nombre de usuario
    # - Contraseña
    def __loginFn(self, username, password):

        # Variable de texto donde se almacenará el texto de error que corresponda
        # para después mostrarlo en un messagebox
        error = ""

        # Caso 1
        # La longitud del texto de los Entry es mayor que 0
        if (len(username) > 0 and len(password) > 0):

            # Comprobando si el texto del campo usuario reune los requisitos
            if (re.fullmatch(r"(?=.*[a-zA-Z])[a-zA-Z\d]{4,30}$", username) is None):
                error += "Usuario o Contraseña no válido.\n"

            # Comprobando si el texto del campo contraseña reune los requisitos
            elif (re.fullmatch(r"^(?=\w*\d*)(?=\w*[a-z]*)(?=\w*[A-Z]*)(?=\w*[a-zA-Z]*)[a-zA-Z\*\_\d]{4,32}$", password) is None):
                error += "Usuario o Contraseña no válido.\n"
        
        # Caso 2
        # La longitud del texto de los Entry es igual a 0
        else:
            # Si el texto del campo username es igual a 0
            if(len(username) == 0):
                error += "El campo usuario está vacio.\n"

            # Si el texto del campo password es igual a 0
            if(len(password) == 0):
                error += "El campo contraseña está vacio.\n"

        # Si ocurrió al menos un errror, esta condición de cumple y muestra el error en un message box
        if (len(error) > 0):

            # Se realizo una instancia de messagebox
            self.errorMessage = messagebox.showerror(title="Error", message=error)
            # Se establecen los Entry a vacios
            self.usernameEntry.delete(0, "end")
            self.passwordEntry.delete(0, "end")
            # Se retorna el foco al Entry del username
            self.usernameEntry.focus()
            return

        # Si no ocurrieron errores se procede a realizar la consulta a la base de datos y comprobar lo campos
        # introducidos (username, password)
        else:

            usernameStatus, passwordStatus, rol, setNewPassword, userState = self.__extractData(username, password)
    
            # Si el usuario:
            # - Se encontró en la BD
            # - Si la contraseña está correcta
            # - Si el rol es de jugardor
            # - Si se debe establecer una nueva contraseña
            # - Si el usuario está habilitado
            if (usernameStatus == 1 and passwordStatus == 1 and rol == 0 and setNewPassword == 1 and userState == 1):
                
                # Inserta cada usuario que ingresa al sistema
                self.db.insert(
                        table="Login", 
                        fields=["id_user_fk"],
                        values=[
                                int(
                                    self.db.select(
                                        query="SELECT id FROM User WHERE tex_nickname=%s", 
                                        data=(username, )
                                    )[0][0]
                                )
                        ]
                )
                
                # Se destruye la ventana de login.
                self.parent.destroy()
                # Se cierra la conexión con la Base de Datos.
                self.db.closeConnection()
                # Se genera una instancia de la ventana para cambio de contraseña.
                # Recibe como parámetro:
                # - El nombre de usuario.
                # - La contraseña ingresada.
                SudokuChangeUserPassword(username, password)


            # Si el usuario:
            # - Se encuentra en la Base de datos 
            # - La contraseña es correcta
            # - El usurio está habilitado
            elif (usernameStatus == 1 and passwordStatus == 1 and userState == 1):

                #Inserta cada usuario que ingresa al sistema
                self.db.insert(
                        table="Login", 
                        fields=["id_user_fk"],
                        values=[
                                int(
                                    self.db.select(
                                        query="SELECT id FROM User WHERE tex_nickname=%s", 
                                        data=(username, )
                                    )[0][0]
                                )
                        ]
                )

                # Si el usuario tiene rol de administrador
                if (rol == 1):
                    # Se destruye la ventana de login.
                    self.parent.destroy()
                    # Se cierra la conexión con la Base de Datos.
                    self.db.closeConnection()
                    # Se crea una isntancia de la ventana principal que corresponde a un usuario administrador
                    SudokuAdministratorUI()

                # Si el usuario tiene rol de jugador
                if(rol == 0):
                    # Se destruye la ventana
                    self.parent.destroy()
                    # Se cierra la conexión con la base de datos.
                    self.db.closeConnection()
                    # Se instancia la ventana principal que corresponde con un usuario que tiene el rol de jugador.
                    SudokuMainWindowUI()

            # Si no se encuentra el usuario o contraseña en la Base de Datos
            elif (usernameStatus == 0 or passwordStatus == 0):
                # Se genera un ventana de error.
                self.errorMessage = messagebox.showerror(title="Error", message="Usuario o Contraseña no válido.")
                # Se borra el contenido del Entry.
                self.usernameEntry.delete(0, "end")
                self.passwordEntry.delete(0, "end")
                # Se establece el foco al entry del nombre de usuario.
                self.usernameEntry.focus()
                return
            
            # Si el estado del usuario es deshabilitado
            elif (userState == 0):
                # Se genera una ventana de información.
                self.errorMessage = messagebox.showinfo(
                    title="Información",
                    message="Su acceso ha sido deshabilitado.\nPongase en contacto con el administrador."
                )
                # Se borra el contenido del Entry.
                self.usernameEntry.delete(0, "end")
                self.passwordEntry.delete(0, "end")
                # Se establece el foco al entry del nombre de usuario.
                self.usernameEntry.focus()
                return

    
    # Función ejecutada cada vez que se intenta cerrar la ventana. 
    # Se muestra una ventana que solicita al usuario confirmación de cierre.
    def __onClosing(self):
        # Se muestra una ventana de confirmación
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            # Se destruye la ventana actual.
            self.parent.destroy()
            # Se muestra una ventana de despedida.
            SudokuBye()
            # Se cierra la conexión a la base de datos.
            self.db.closeConnection()
        else:
            pass

    
    # Obtiene el estado del usuario (las credenciales) desde la base de datos y las retorna
    # Recibe como parámetros:
    # - El nombre de usuario.
    # - Contraseña.
    def __extractData(self, username, password):
        # Se hace el llamado a la función getUserStatus de MySQLEngine.
        # Esta función realiza el llamado a fn_compareData, que es una función SQL
        # Se obtiene  el resultado de la operación y se almacena en la variable result
        result = self.db.getUserStatus(username, password)[0]
        # Se separa cada elemento del texto mediante un espacio y se almacena en variables
        usernameStatus, passwordStatus, rol, setNewPassword, userState = result.split(" ")
        return int(usernameStatus), int(passwordStatus), int(rol), int(setNewPassword), int(userState)
