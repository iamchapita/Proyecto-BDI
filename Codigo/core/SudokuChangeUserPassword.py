from tkinter import *
from core.SudokuMainWindowUI import SudokuMainWindowUI
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose
from core.Tooltip import Tooltip
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
import re

"""
Frame que muestra el Login y todos sus respectivos widgets de la aplicación
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuChangeUserPassword(Frame):

    def __init__(self, username, password):

        self.parent = Tk()
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)
        self.pack()
        self.username = username
        self.password = password
        self.config = ConfigConnection()
        self.db = MySQLEngine(self.config.getConfig())
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):

        self.width = 400
        self.height = 600
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        self.parent.title("Cambio de contraseña")
        self.parent.resizable(False, False)
        self.parent.geometry("%dx%d"%(self.width, self.height))
        self.parent.iconphoto(True, self.logo)
        self.parent.configure(background = "#171717")
        
        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)
        
        # Muestra el titulo de la seccion
        label1 = Label(
            self.parent,
            text='¡Bienvenido {}!\n Este es su primer\n ingreso a SUDOKU, \ndebe cambiar obligatoriamente\n su contraseña.'.format(self.username),
            font=("Lato", 15)
            )
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=50,y=50)
    
        label3= Label(self.parent, text='Ingrese su nueva contraseña', font =("Lato",13))
        label3.configure(background = "#171717", fg="#6ea8d9")
        label3.pack()
        label3.place(x=80,y=270)

        textTooltip ="""{} de más de 4 caracteres.\nCaracteres válidos: \n- Mayúsculas\n- Minúsculas\n- Números\n- Simbolos (._-)"""
        self.newPasswordEntry = Entry(self.parent,show="*", font=("Lato",13),  justify=CENTER)
        self.newPasswordEntry.pack()
        self.newPasswordEntry.place(x=110, y=310, height=30, width=200)
        self.passwordToolTip = Tooltip(self.newPasswordEntry, textTooltip.format("Contraseña"))
        
        self.loginButton = Button(self.parent, command=lambda: self.__changePassword(self.newPasswordEntry.get()))
        self.loginButton.configure(text="Confirmar contraseña", bg="#6ea8d9", font=("Lato", 15))
        self.loginButton.place(x=90, y=445)

        labelBrand = Label(self.parent, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=8,y=555)

    def __changePassword(self, password):

        error = ""

        if (len(password) > 0):
            
            if (re.search(r"[a-zA-Z0-9._-]{4,}", password) is None):
                error += "Usuario o Contraseña no válido.\n"    

            elif (password == self.password):
                error += "Debe cambiar la contraseña.\nIntroduzca una nueva contraseña."

        elif(len(password) == 0):
            error += "El campo contraseña está vacio."
        
        if (len(error) > 0):
            # Se realizo una instancia de messagebox
            self.errorMessage = messagebox.showerror(title="Error", message=error)
            # Se establecen los Entry a vacios
            self.newPasswordEntry.delete(0, "end")
            # Se retorna el foco al Entry del username
            self.newPasswordEntry.focus()
            return
        
        else:

            obj = self.db.update(
                "User",
                ("tex_password",),
                ("HEX(AES_ENCRYPT('{}', '{}'))".format(password, self.username),),
                "tex_nickname = '{}'".format(self.username)
                )
            print(obj)
            
            self.parent.destroy()
            SudokuMainWindowUI()
    
    """
    Función que permite minimizar o salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
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