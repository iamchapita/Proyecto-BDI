from tkinter import *
from tkinter import messagebox
from core.SudokuChangeUserPassword import SudokuChangeUserPassword
from core.SudokuMainWindowUI import SudokuMainWindowUI
from core.SudokuAdministratorUI import SudokuAdministratorUI
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose
from core.Tooltip import Tooltip
from core.SudokuByeUI import SudokuBye
import re

"""
Frame que muestra el Login y todos sus respectivos widgets de la aplicación
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuLoginPageUI(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self):

        self.parent = Tk()
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)
        self.config = ConfigConnection()
        self.db = MySQLEngine(self.config.getConfig())
        self.__initUI()

    """
    Creación de los widgets que se veran en pantalla.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):

        self.width = 400
        self.height = 600
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.backgroundImage = PhotoImage(file="core/images/LoginScreen.png", master=self.parent)
        self.parent.title("Inicio de Sesión")
        self.parent.resizable(False, False)
        self.parent.geometry("%dx%d"%(self.width, self.height))
        self.parent.iconphoto(True, self.logo)
        self.parent.configure(background = "#171717")
        
        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)
        
        label1= Label(self.parent, text='Nombre de usuario', font=("Lato",20))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 20, padx=75)

        self.usernameEntry = Entry(self.parent, font=("Lato",15),  justify=CENTER)
        self.usernameEntry.grid(row=2,column=1,sticky = "nsew", padx=70)
        textTooltip ="Ingrese {}"
        self.usernameToolTip = Tooltip(self.usernameEntry, textTooltip.format("el nombre de usuario."))
        self.usernameEntry.focus()

        label2= Label(self.parent, text='Contraseña', font =("Lato",20))
        label2.configure(background = "#171717", fg="white")
        label2.grid(row=3,column=1,sticky = "nsew", pady = 20, padx=120)
        
        self.passwordEntry = Entry(self.parent,show="*", font=("Lato",15),  justify=CENTER)
        self.passwordEntry.grid(row=4,column=1,sticky = "nsew", padx=70)
        
        self.usernameToolTip = Tooltip(self.passwordEntry, textTooltip.format("la contraseña."))

        self.loginButton = Button(self.parent, command=lambda: self.__loginFn(self.usernameEntry.get(), self.passwordEntry.get()))
        self.loginButton.configure(text="Iniciar Sesión", bg="#6ea8d9", font=("Lato", 15))
        self.loginButton.grid(row=5,column=1,sticky = "nsew", pady = 20, padx=120)

        labelbackgroundImage = Label(self.parent, image=self.backgroundImage, borderwidth=0)
        labelbackgroundImage.grid(row=6,column=1,sticky = "nsew", pady = 50, padx=4)

    """
    Función que verifica la existencia y conexión a la BD.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __loginFn(self, username, password):

        # Variable de texto donde se almacenará el texto de error que corresponda
        # para después mostrarlo en un messagebox
        error = ""

        # Caso 1
        # La longitud del texto de los Entry es mayor que 0
        if (len(username) > 0 and len(password) > 0):

            # Comprobando si el texto del campo usuario reune los requisitos
            if (re.search(r"[a-zA-Z0-9._-]{4,}", username) is None):
                error += "Usuario o Contraseña no válido.\n"

            # Comprobando si el texto del campo contraseña reune los requisitos
            elif (re.search(r"[a-zA-Z0-9._-]{4,}", password) is None):
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

            usernameStatus, passwordStatus, rol, setNewPassword = self.__extractData(username, password)    
            
            if (usernameStatus == 1 and passwordStatus == 1 and rol == 0 and setNewPassword == 1):
                
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
                
                self.parent.destroy()
                self.db.closeConnection()
                SudokuChangeUserPassword(username, password)

            elif (usernameStatus == 1 and passwordStatus == 1):

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
    
                if (rol == 1):
                    self.parent.destroy()
                    self.db.closeConnection()
                    SudokuAdministratorUI()

                if(rol == 0):
                    # Se destruye la ventana
                    self.parent.destroy()
                    self.db.closeConnection()
                    # Se instancia una ventana nueva del tipo MainWindow
                    SudokuMainWindowUI()

            elif (usernameStatus == 0 or passwordStatus == 0):
                self.errorMessage = messagebox.showerror(title="Error", message="Usuario o Contraseña no válido.")
                self.usernameEntry.delete(0, "end")
                self.passwordEntry.delete(0, "end")
                self.usernameEntry.focus()
                return

    """
    Función que pregunta al usuario si desea salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 3.0
    """
    def __onClosing(self):
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            self.parent.destroy()
            SudokuBye()
            self.db.closeConnection()
        else:
            pass

    """
    Función que extrae el username y password de la base de datos.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __extractData(self, username, password):
        # Se hace el llamado a la función getUserStatus de MySQLEngine.
        # Esta función realiza el llamado a fn_compareData, que es una función SQL
        # Se obtiene  el resultado de la operación y se almacena en la variable result
        result = self.db.getUserStatus(username, password)[0]
        # Se separa cada elemento del texto mediante un espacio y se almacena en variables
        usernameStatus, passwordStatus, rol, setNewPassword = result.split(" ")
        return int(usernameStatus), int(passwordStatus), int(rol), int(setNewPassword)