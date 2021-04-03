from tkinter import *
from tkinter import messagebox
from core.SudokuMainWindowUI import SudokuMainWindowUI
from core.SudokuAdministratorUI import SudokuAdministratorUI
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.ScreenCenter import ScreenCenter
from core.Close import DialogClose

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
        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)
        canvas = Canvas(self, width=self.backgroundImage.width(), height=self.backgroundImage.height())
        labelLogo = Label(self,image=self.backgroundImage)
        labelLogo.place(x=0, y=0, relwidth=1, relheight=1)
        canvas.grid(row=0, column=0)
        usernameText = StringVar()
        usernameEntry = Entry(self, textvariable = usernameText, font=("Lato",15),  justify=CENTER)
        passwordText = StringVar()
        passwordEntry = Entry(self, textvariable = passwordText, show = "*", font=("Lato",15),  justify=CENTER)
        canvas.create_window(200, 120, window=usernameEntry)
        canvas.create_window(200, 210, window=passwordEntry)
        loginButton = Button(self, text="Iniciar Sesión", bg="#6ea8d9",width=10, height=2,font=("Lato",15), command = lambda: self.__loginFn(usernameText, passwordText))
        canvas.create_window(200, 280, window=loginButton)

    """
    Función que verifica la existencia y conexión a la BD.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __loginFn(self, username, password):

        # Variable de texto donde se almacenará el texto de error que corresponda
        # para después mostrarlo en un messagebox
        error = ""
        
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
        d = DialogClose(self.parent)
        self.parent.wait_window(d.top)