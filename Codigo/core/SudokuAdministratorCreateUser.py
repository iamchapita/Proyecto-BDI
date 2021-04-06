from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.FileManipulation.EncryptDecrypt import EncryptDecryptSudokuFile


"""
Frame que permite visualizar los elementos cuando un usuario se crea
y se registra en el juego y la BD.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuAdministratorCreateUser(Frame):

    """
    Constructor de la clase.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self, parent):
        self.parent = parent
        self.child = Tk()
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        self.__initUI()
        self.config = ConfigConnection() 
        self.db = MySQLEngine(self.config.getConfig())
        img = PhotoImage(file="core/images/back.png", master=self.child)
        btnBack= Button(self.child, image=img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        btnBack.grid(row=0,column=1,sticky = "nsew", pady=10)
        self.master.mainloop()

    """
    Creación de los widgets.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.child.iconphoto(True, self.icon)
        self.width = 400
        self.height = 600

        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)

        self.child.title('Crear Usuarios')
        self.child.geometry("%dx%d" %(self.width, self.height))

        # Tamaño de la ventana
        self.child.configure(background = "#171717")

        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.child.resizable(False, False)

        # Muestra el titulo de la seccion
        label1= Label(self.child, text='Crear un nuevo usuario', font=("Lato",20))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80,padx=35)

        label2= Label(self.child, text='Introduzca el nombre de usuario:', font =("Lato",15))
        label2.configure(background = "#171717", fg="#6ea8d9")
        label2.grid(row=2,column=1, pady = 20,padx=35)

        input_text = StringVar()
        self.userText = ttk.Entry(self.child, textvariable = input_text, font=("Lato",10),  justify=CENTER)
        self.userText.grid(row=3,column=1, padx=35)
        
        Button(self.child, text = 'Crear', command= self.__save, bg="#6ea8d9", font=("Lato",15)).grid(row=4,column=1, pady = 15,padx=35,ipadx=40)
        
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.grid(row=6,column=1, pady = 125)

    """
        @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
        @version 1.1
        @date 2021/04/06

        Esta función verifica la existencia de un usuario en la base de datos, sí este usaurio no existe, lo crea, 
        generando una clave cifrada a partir del nombre del usuario. 
        La primera vez que el usuario inicia sesión al sistema, el sistema lo obliga a cambiar de contraseña.
    """
    def __save(self):

         # delete(self, table, tex_nickname): 
        username = self.userText.get()
        print(username)
        
        #Sí el text no está vacío
        if username: 
            #Existencia del usuario en la base de datos | sin importar que este este de baja (bit_state=0)
            userExist = self.db.select("SELECT tex_nickname FROM User WHERE tex_nickname = %s", (username, ))

            #El usuario no existe en la base de datos
            if not userExist: 

                encryptPassword = (EncryptDecryptSudokuFile(self.db)).encrypt(username, username)

                self.db.insert(
                    table="User", 
                    fields=["tex_nickname", "tex_password"], 
                    values=[
                        username, 
                        encryptPassword
                        ]
                )

                self.userText.delete(0, "end") 

            else: 
                print("El usuario existe en la base de datos, hacer algo aquí porfis uwu")

        else: 
            print("El TEXT está vacío, hacer algo aquí porfis uwu")

    """
    Función que permite regresar a la ventana anterior al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()

    """
    Función que permite minimizar o salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __onClosing(self):

        #Cierra la conexión a la base de datos
        self.db.closeConnection() 

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