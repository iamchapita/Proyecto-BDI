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
        textTooltip ="""{} de más de 4 caracteres.\nCaracteres válidos: \n- Mayúsculas\n- Minúsculas\n- Números\n- Simbolos (._-)"""
        self.usernameToolTip = Tooltip(self.usernameEntry, textTooltip.format("Nombre de usuario"))

        label2= Label(self.parent, text='Contraseña', font =("Lato",20))
        label2.configure(background = "#171717", fg="white")
        label2.pack()
        label2.place(x=130,y=145)

        self.passwordEntry = Entry(self.parent,show="*", font=("Lato",15),  justify=CENTER)
        self.passwordEntry.pack()
        self.passwordEntry.place(x=100,y=180, height = 30, width = 200)
        
        self.usernameToolTip = Tooltip(self.passwordEntry, textTooltip.format("Contraseña"))

        self.loginButton = Button(self.parent, command=lambda: self.__loginFn(self.usernameEntry, self.passwordEntry))
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

        if (len(username.get()) > 0):
            pass
        else:
            pass

        if (len(password.get()) > 0):
            pass
        else:
            pass

        # Comprobando si el texto del campo usuario reune los requisitos
        if (re.search(r"[a-zA-Z0-9._-]{4,}", username.get()) is None and len(username.get()) > 0):
            error += "Usuario o Contraseña no válido.\n"

        # Comprobando si el texto del campo contraseña reune los requisitos
        if (re.search(r"[a-zA-Z0-9._-]{4,}", password.get()) is None and len(password.get()) > 0):
            error += "Usuario o Contraseña no válido.\n"
        
        # Comprobando la longitud del texto correspondiente al nombre de usuario
        if (len(username.get()) == 0):
            error += "El campo usuario está vacio.\n"
        
        # Comprobando la longitud del texto correspondiente a la contraseña
        if(len(password.get()) == 0):
            error += "El campo contraseña está vacio.\n"

        #  Bloque Try para evitar que error si el resultado de la consulta de la base de datos
        # está vacia (no se encontró el usuario ingresado)
        try:
            # Se declara una variable por cada elemento de la tupla retornada
            # La variable statusLogin guarda un 1 si el usuario se encontró en la base de datos
            # La variable rol, guarda el rol del usuario y según este muestra la pantalla a continuación
            statusLogin, rol = self.db.getUserStatus(username.get(), password.get())[0]
        # Se define un except donde a cada variable se le pasa un valor "por defecto".
        # Este valor va a devolver error en la interfaz
        except:
            statusLogin, rol = (0,0)
        
        # ---------------Condición provisional para probar el cambio de contraseña
        if(username.get()==password.get() and username.get()!="admin"):
            print("Es primera vez en la plataforma")
            self.parent.destroy()
            SudokuChangeUserPassword()
        # ---------------Condición provisional para probar el cambio de contraseña.
        
        # Comprobando si el valor de la variable es 0
        # Esto ocurre si:
        #   - El usuario no existe
        #   - El usuario existe pero la contraseña no es correcta
        # Se comprueba si la longitud del error es 0 para no emitir el mensaje de error
        # si los campos están vacios.
        if (statusLogin == 0 and len(error) == 0):
            error += "Usuario o contraseña no válidos.\n"
        
        # Comprobando si ocurrio algún error
        if(len(error) > 0):
            messagebox.showerror(title="Error", message=error)
            self.usernameEntry.delete(0, "end")
            self.passwordEntry.delete(0, "end")
            self.usernameEntry.focus()
            return

        if (statusLogin == 1):

            if (rol == 1):
                
                self.parent.destroy()
                SudokuAdministratorUI()

            elif (rol == 0):
                # Se destruye la ventana
                self.parent.destroy()
                # Se instancia una ventana nueva del tipo MainWindow
                SudokuMainWindowUI()

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