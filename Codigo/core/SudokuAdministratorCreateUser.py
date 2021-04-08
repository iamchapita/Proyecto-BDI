import os
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
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
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
    Creación de los widgets que se veran en pantalla.
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
        self.child.configure(background = "#171717")
        self.child.resizable(False, False)

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
    Esta función verifica la existencia de un usuario en la base de datos, sí este usaurio no existe, lo crea, 
    generando una clave cifrada a partir del nombre del usuario. La primera vez que el usuario inicia sesión al 
    sistema, el sistema lo obliga a cambiar de contraseña.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.1
    @date 2021/04/06
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
                messagebox.showwarning(title="Usuario existente", message="El usuario existe en la base de datos.")

        else: 
            messagebox.showerror(title="Campo vacio", message="Por favor ingrese algo valido.")

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