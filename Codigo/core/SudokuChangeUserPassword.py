from tkinter import *
from core.SudokuMainWindowUI import SudokuMainWindowUI
from core.ScreenCenter import ScreenCenter
from core.Close import DialogClose
from core.Tooltip import Tooltip
import re

"""
Frame que muestra el Login y todos sus respectivos widgets de la aplicación
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuChangeUserPassword(Frame):

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
        self.Brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        self.parent.title("Cambio de contraseña")
        self.parent.resizable(False, False)
        self.parent.geometry("%dx%d"%(self.width, self.height))
        self.parent.iconphoto(True, self.logo)
        self.parent.configure(background = "#171717")
        
        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)
        
        # Muestra el titulo de la seccion
        label1= Label(self.parent, text='¡Bienvenido!\n Este es su primer\n ingreso a SUDOKU, \ndebe cambiar obligatoriamente\n su contraseña.', font=("Lato",20))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=20,y=50)
        
        label2= Label(self.parent, text='Ingrese su contraseña actual', font=("Lato",15))
        label2.configure(background = "#171717", fg="#6ea8d9")
        label2.pack()
        label2.place(x=80,y=230)

        self.passwordEntry = Entry(self.parent, show="*", font=("Lato",15),  justify=CENTER)
        self.passwordEntry.pack()
        self.passwordEntry.place(x=110, y=275, height=30, width=200)

        label3= Label(self.parent, text='Ingrese su nueva contraseña', font =("Lato",15))
        label3.configure(background = "#171717", fg="#6ea8d9")
        label3.pack()
        label3.place(x=80,y=330)

        self.newPasswordEntry = Entry(self.parent,show="*", font=("Lato",15),  justify=CENTER)
        self.newPasswordEntry.pack()
        self.newPasswordEntry.place(x=110,y=370, height = 30, width = 200)
        
        textTooltip ="""{} de más de 4 caracteres.\nCaracteres válidos: \n- Mayúsculas\n- Minúsculas\n- Números\n- Simbolos (._-)"""
        self.usernameToolTip = Tooltip(self.newPasswordEntry, textTooltip.format("Contraseña"))

        self.loginButton = Button(self.parent, command=lambda: self.__loginChangePassword(self.passwordEntry, self.newPasswordEntry))
        self.loginButton.configure(text="Confirmar contraseña", bg="#6ea8d9", font=("Lato", 15))
        self.loginButton.place(x=100, y=445)

        labelBrand = Label(self.parent, image=self.Brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=8,y=555)

    def __loginChangePassword(self, userName, newPassword):
        # !Nota: Aquí se debe verificar que se ha cambiado la contraseña correctamente.
        print(userName.get())
        print(newPassword.get())
        userName.delete(0, "end")
        newPassword.delete(0, "end")
        userName.focus()
        #!---------------------------------------------------------------------------
        self.parent.destroy()
        SudokuMainWindowUI()
    
    """
    Función que permite minimizar o salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __onClosing(self):
        d = DialogClose(self.parent)
        self.parent.wait_window(d.top)