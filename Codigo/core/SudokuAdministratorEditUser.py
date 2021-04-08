from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose
from core.EngineSQL.MySQLEngine import *
from core.EngineSQL.ConfigConnection import *

"""
Frame que permite la visualización para editar un usuario.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuAdministratorEditUser(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self, parent, username):
        self.parent = parent
        self.child = Tk()
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        self.config = ConfigConnection()
        self.db = MySQLEngine(self.config.getConfig())
        self.username = username
        self.pack()
        self.__initUI()

    """
    Creación de los widgets que se veran en pantalla.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):

        self.img = PhotoImage(file="core/images/back.png", master=self.child)
        self.buttonBack = Button(self.child, image=self.img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        self.buttonBack.pack()
        self.buttonBack.place(x=315, y=20)
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.width = 400
        self.height = 600
        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)
        self.child.title('Editar nombre de Usuario')
        self.child.iconphoto(True, self.icon)

        self.child.geometry("%dx%d" %(self.width, self.height))
        self.child.configure(background = "#171717")
        self.child.resizable(False, False)
        
        label1= Label(self.child, text='Editar nombre de usuario', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=100,y=100)
    
        label3= Label(self.child, text='Introduzca el nuevo nombre de usuario:', font =("Lato",15))
        label3.configure(background = "#171717", fg="#6ea8d9")
        label3.pack()
        label3.place(x=25,y=270)
        
        self.usernameEdited = ttk.Entry(self.child, font=("Lato",10),  justify=CENTER)
        self.usernameEdited.pack()
        self.usernameEdited.place(x=110,y=310, height = 30, width = 200)
        
        self.editButton = Button(self.child, text='Editar', command=self.__save)
        self.editButton.configure(bg="#6ea8d9", font=("Lato", 15))
        self.editButton.place(x=155, y=380, height = 50, width = 110)
        
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=8,y=555)

    """
    Función que permite guardar los cambios.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __save(self):
        result = self.db.select("SELECT tex_nickname FROM User WHERE bit_rol = 0;")
        for nickname in result:
            if (self.usernameEdited.get() == self.username):
                print("El usuario ya existe")
                return
        ## Falta implementar lógica para actualizar la BD
        self.userText.delete(0, "end")
        self.userTextEdited.delete(0, "end")

    """
    Función que permite regresar a la ventana anterior al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()
    
    """
    Función que pregunta al usuario si desea salir del juego y cierra la 
    conexión a la base de datos.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 2.0
    """
    def __onClosing(self):

        self.db.closeConnection() 

        MsgBox = messagebox.askquestion ('Salir','Estas seguro de que te quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            self.child.destroy()
            sys.exit()
        else:
            pass