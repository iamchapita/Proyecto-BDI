from tkinter import *
from tkinter import ttk
from core.ScreenCenter import ScreenCenter
from core.SudokuAdministratorCreateUser import *
from core.SudokuAdministratorDeleteUser import *
from core.SudokuAdministratorEditUser import *
from core.SudokuUserList import *
from core.DialogClose import DialogClose

"""
Frame que permite visualizar la administración de los usuario registrados
en el juego así mismo como en la BD.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuUserAdministration(Frame):

    """
    Constructor de la clase.
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
    Creación de los widgets.
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

        Button(
            self.child, text='Crear usuario',
            bg="#6ea8d9", font=("Lato", 17),
            command=self.__goCreateUser
            ).grid(row=3, column=1, sticky="nsew", pady=5, padx=80, ipadx=37)
            
        Button(
            self.child, text='Lista de Usuarios',
            bg="#6ea8d9", font=("Lato", 17),
            command=self.__listUsers
            ).grid(row=4,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=18)
        """ Button(
            self.child, text='Editar usuario',
            bg="#6ea8d9", font=("Lato", 17),
            command=self.__goEditUser
            ).grid(row=3,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=18)
        Button(
            self.child, text='Eliminar usuario',
            bg="#6ea8d9", font=("Lato", 17),
            command=self.__goDeleteUser
            ).grid(row=4,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=11)
        """
        Button(
            self.child, text='Atrás',
            image=self.img, bg="#171717",
            borderwidth=0, highlightthickness=0,
            command=self.__goBack
            ).grid(row=0,column=1,sticky = "nsew", pady=10)
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.grid(row=6, column=1, pady=135)
    
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
        SudokuUserList(self.parent)

    """
    Función que permite minimizar o salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __onClosing(self):
        self.dialogClose = DialogClose(self.child)
        #self.child.wait_window(self.dialogClose)
        """ # Bloque try except para manejar la excepción devuelta si el self.parent fue destruido
        try:
            # Confirma si la instancia de dialogClose existe
            if (self.dialogClose.winfo_exists() == False):
                # Si no existe entonces establece de nuevo la función de apertura de dialogClose cuando
                # se intenta cerrar la ventana
                self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        except:
            pass """