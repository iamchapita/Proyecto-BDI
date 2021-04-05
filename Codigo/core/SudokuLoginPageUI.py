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
import re

"""
Frame que muestra el Login y todos sus respectivos widgets de la aplicación
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuLoginPageUI(Frame):

    """
    Constructor de la clase.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self):

        self.parent = Tk()
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)
        self.pack()
        self.config = ConfigConnection()
        self.db = MySQLEngine(self.config.getConfig())
        self.__initUI()
        self.master.mainloop()

    """
    Creación de widgets de la ventana.
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
        
        # Muestra el titulo de la seccion
        label1= Label(self.parent, text='Nombre de usuario', font=("Lato",20))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=85,y=50)

        self.usernameEntry = Entry(self.parent, font=("Lato",15),  justify=CENTER)
        self.usernameEntry.pack()
        self.usernameEntry.place(x=100, y=90, height=30, width=200)
        textTooltip ="Ingrese {}"
        self.usernameToolTip = Tooltip(self.usernameEntry, textTooltip.format("el nombre de usuario."))

        label2= Label(self.parent, text='Contraseña', font =("Lato",20))
        label2.configure(background = "#171717", fg="white")
        label2.pack()
        label2.place(x=130, y=145)
        
        self.passwordEntry = Entry(self.parent,show="*", font=("Lato",15),  justify=CENTER)
        self.passwordEntry.pack()
        self.passwordEntry.place(x=100,y=180, height = 30, width = 200)
        
        self.usernameToolTip = Tooltip(self.passwordEntry, textTooltip.format("la contraseña."))

        self.loginButton = Button(self.parent, command=lambda: self.__loginFn(self.usernameEntry.get(), self.passwordEntry.get()))
        self.loginButton.configure(text="Iniciar Sesión", bg="#6ea8d9", font=("Lato", 15))
        self.loginButton.place(x=128, y=245)

        labelbackgroundImage = Label(self.parent, image=self.backgroundImage, borderwidth=0)
        labelbackgroundImage.pack()
        labelbackgroundImage.place(x=3,y=335)

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
                self.parent.destroy()
                SudokuChangeUserPassword(username, password)

            elif (usernameStatus == 1 and passwordStatus == 1):
    
                if (rol == 1):
                    self.parent.destroy()
                    SudokuAdministratorUI()

                if(rol == 0):
                    # Se destruye la ventana
                    self.parent.destroy()
                    # Se instancia una ventana nueva del tipo MainWindow
                    SudokuMainWindowUI()

            elif (usernameStatus == 0 or passwordStatus == 0):
                self.errorMessage = messagebox.showerror(title="Error", message="Usuario o Contraseña no válido.")
                self.usernameEntry.delete(0, "end")
                self.passwordEntry.delete(0, "end")
                self.usernameEntry.focus()
                return

    def __onClosing(self):
        self.dialogClose = DialogClose(self.parent)
        self.parent.wait_window(self.dialogClose)
        # Bloque try except para manejar la excepción devuelta si el self.parent fue destruido
        try:
            # Confirma si la instancia de dialogClose existe
            if (self.dialogClose.winfo_exists() == False):
                # Si no existe entonces establece de nuevo la función de apertura de dialogClose cuando
                # se intenta cerrar la ventana
                self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        except:
            pass

    def __extractData(self, username, password):
        # Se hace el llamado a la función getUserStatus de MySQLEngine.
        # Esta función realiza el llamado a fn_compareData, que es una función SQL
        # Se obtiene  el resultado de la operación y se almacena en la variable result
        result = self.db.getUserStatus(username, password)[0]
        # Se separa cada elemento del texto mediante un espacio y se almacena en variables
        usernameStatus, passwordStatus, rol, setNewPassword = result.split(" ")
        return int(usernameStatus), int(passwordStatus), int(rol), int(setNewPassword)