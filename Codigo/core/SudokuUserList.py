from tkinter import *
from tkinter.ttk import Treeview
from core.SudokuAdministratorEditUser import *
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose
from core.EngineSQL.MySQLEngine import *
from core.EngineSQL.ConfigConnection import *
import os
import re

class SudokuUserList(Frame):

    def __init__(self, parent):
        self.parent = parent
        self.child = Tk()
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.config = ConfigConnection()
        self.db = MySQLEngine(self.config.getConfig())
        super().__init__(self.child)
        self.currentItem = 0
        self.pack()
        self.__initUI()

    def __initUI(self):

        self.width = 960
        self.height = 545
        self.img = PhotoImage(file="core/images/back.png", master=self.child)
        self.backButton= Button(self.child, image=self.img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        self.backButton.pack()
        self.backButton.place(x=850, y=20)

        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.child.title("Lista de Usuarios")
        self.child.resizable(False, False)
        self.child.configure(background = "#171717")
        self.child.geometry("%dx%d"%(self.width, self.height))
        self.child.iconphoto(True, self.logo)

        center = ScreenCenter()
        center.center(self.child, self.width, self.height)

        self.dataView = Treeview(self.child, columns=("#1", "#2"))
        self.dataView.pack()
        self.dataView.place(x=200, y=130)
        
        self.dataView.column("#0", width=100, anchor=CENTER)
        self.dataView.column("#1", width=200, anchor=CENTER)
        self.dataView.column("#2", width=250, anchor=CENTER)

        self.dataView.heading("#0", text="Indice", anchor = CENTER)
        self.dataView.heading("#1", text="Usuario", anchor = CENTER)
        self.dataView.heading("#2", text="Estado", anchor = CENTER)

        self.userEditButton = Button(self.child, text='Editar usuario', command=self.__editUsername)
        self.userEditButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.userEditButton.pack()  #.grid(row=3, column=1, sticky="nsew", )
        self.userEditButton.place(x=170, y=400)

        self.stateEditButton = Button(self.child, text='Editar estado', command=self.__editState)
        self.stateEditButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.stateEditButton.pack()  #.grid(row=3, column=1, sticky="nsew", )
        self.stateEditButton.place(x = 375, y = 400)
        
        self.passwordEditButton = Button(self.child, text='Editar contraseña', command=self.__editPassword)
        self.passwordEditButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.passwordEditButton.pack()  #.grid(row=3, column=1, sticky="nsew", )
        self.passwordEditButton.place(x=575, y=400)
        
        # Muestra el titulo de la seccion
        label1= Label(self.child, text='Lista de Usuarios', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=345,y=50)

        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=280,y=485)
        self.__loadData()
        self.dataView.bind("<ButtonRelease-1>", self.__getSelectedItem)
        

    """
    Función que permite leer los mejores puntajes provenientes de una 
    consulta de la base de datos e insertarlos en una tabla de tkinter.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __getSelectedItem(self, event):
        self.currentItem = self.dataView.focus()
        print(self.dataView.item(self.currentItem))
        self.currentItem = self.dataView.item(self.currentItem)

    def __loadData(self):

        result = self.db.select("SELECT tex_nickname, bit_state FROM User WHERE bit_rol = 0;")
        count  = 1
        for nickname, state in result:
            if(state == 1):
                self.dataView.insert("", index=count, text = count, values=(nickname, "Habilitado"))
            else:
                self.dataView.insert("", index=count, text=count, values=(nickname, "Deshabilitado"))
            count += 1
        
    def __editUsername(self):
        if (self.currentItem):
            self.db.closeConnection()
            SudokuAdministratorEditUser(self.parent, (self.currentItem["values"][0]))

    def __editPassword(self):
        pass

    def __editState(self):
        pass
    
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
        self.dialogClose = DialogClose(self.parent)
        self.parent.wait_window(self.dialogClose)
