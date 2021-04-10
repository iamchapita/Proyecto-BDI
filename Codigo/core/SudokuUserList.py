from tkinter import *
from tkinter.ttk import Treeview
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose
from core.EngineSQL.MySQLEngine import *
from core.EngineSQL.ConfigConnection import *
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.FileManipulation.EncryptDecrypt import *
from core.EntryPlaceholder import *
import os
import re

"""
Frame que permite visualizar la lista de todos los usuarios registrados
en el juego y en la BD.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuUserList(Frame):

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
        self.config = ConfigConnection()
        self.db = MySQLEngine(self.config.getConfig())
        super().__init__(self.child)
        self.currentItem = ""
        self.pack()
        self.__initUI()

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):

        self.width = 960
        self.height = 600
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
        self.dataView.place(x=200, y=120)
        
        self.dataView.column("#0", width=100, anchor=CENTER)
        self.dataView.column("#1", width=200, anchor=CENTER)
        self.dataView.column("#2", width=250, anchor=CENTER)

        self.dataView.heading("#0", text="Indice", anchor = CENTER)
        self.dataView.heading("#1", text="Usuario", anchor = CENTER)
        self.dataView.heading("#2", text="Estado", anchor = CENTER)

        self.userEditButton = Button(self.child, text='Editar usuario', command=self.__editUsername)
        self.userEditButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.userEditButton.pack()  #.grid(row=3, column=1, sticky="nsew", )
        self.userEditButton.place(x=170, y=470)

        self.stateEditButton = Button(self.child, text='Editar estado', command=self.__editState)
        self.stateEditButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.stateEditButton.pack()  #.grid(row=3, column=1, sticky="nsew", )
        self.stateEditButton.place(x = 375, y = 470)
        
        self.passwordEditButton = Button(self.child, text='Editar contraseña', command=self.__editPassword)
        self.passwordEditButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.passwordEditButton.pack()  #.grid(row=3, column=1, sticky="nsew", )
        self.passwordEditButton.place(x=575, y=470)

        self.usernameEdited = Entry(self.child, font=("Lato", 10), justify=CENTER)
        EntryPlaceholder(self.usernameEdited, "Nombre de Usuario")
        self.usernameEdited.pack()
        self.usernameEdited.place(x=170, y=400, height=30, width=178)

        self.stateCombobox = ttk.Combobox(self.child, state="readonly")
        self.stateCombobox["values"] = ["--Seleccione--","Habilitado", "Deshabilitado"]
        self.stateCombobox.configure(width = 19, height = 10, justify=CENTER)
        self.stateCombobox.place(x=375, y=400)
        self.stateCombobox.current(0)
        
        self.passwordEdited = Entry(self.child, font=("Lato", 10), justify=CENTER)
        EntryPlaceholder(self.passwordEdited, "Contraseña")
        self.passwordEdited.pack()
        self.passwordEdited.place(x=575, y=400, height=30, width=217)
        
        # Muestra el titulo de la seccion
        label1= Label(self.child, text='Lista de Usuarios', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=345,y=40)

        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=280,y=550)
        self.dataView.bind("<ButtonRelease-1>", self.__getSelectedItem)
        self.__loadDataView()
        #self.child.after()

    # Obtiene el elemento seleccionado del dataView (TreeView)
    def __getSelectedItem(self, event):
        self.currentItem = self.dataView.focus()
        self.currentItem = self.dataView.item(self.currentItem)
        if(self.currentItem["values"]):
            self.currentItem = self.currentItem["values"]
            self.__loadComboboxData()

    # Obtiene los nombres de usuario y el estado de los mismos y los posiciona
    # en el dataView
    def __loadDataView(self):

        #self.dataView.delete(*self.dataView.get_children())
        result = self.db.select("SELECT tex_nickname, bit_state FROM User WHERE bit_rol = 0;")
        count  = 1
        for nickname, state in result:
            if(state == 1):
                self.dataView.insert("", index=count, text = count, values=(nickname, "Habilitado"))
            else:
                self.dataView.insert("", index=count, text=count, values=(nickname, "Deshabilitado"))
            count += 1

    # Obtiene el estado del usuario seleccionado y lo establece como opción en el ComboBox
    def __loadComboboxData(self):
        
            if(self.currentItem[1] == "Habilitado"):
                self.stateCombobox.current(1)
            else:
                self.stateCombobox.current(2)

    # Elimina todas las opciones (usuarios) del dataView
    def __clearDataView(self):
        for i in self.dataView.get_children():
            self.dataView.delete(i)
        
    # Función encargada de evaluar si se cumplen las condiciones para editar el *Nombre de Usuario* 
    # del usuario seleccionado en el dataView
    def __editUsername(self):
        self.__clearDataView()
        self.__loadDataView()
        error = ""

        if (len(self.currentItem) > 0):

            if (self.usernameEdited.get() != "Nombre de Usuario" and self.usernameEdited.get() != ""):
                result = self.db.select("SELECT tex_nickname FROM User;")    
            
                for nickname in result:
                    if (self.usernameEdited.get() == nickname[0]):
                        error += "El nombre de usuario introducido ya está en uso."
                
                if (re.search(r"[a-zA-Z0-9._-]{4,}", self.usernameEdited.get()) is None):
                    error += "El nombre de usuario no es válido."

            else:
                error += "Debe introducir un nombre de usuario."
        
        else:
            error += "Debe seleccionar un usuario."

        if (len(error) > 0):
            MsgBox = messagebox.showerror(title = 'Error', message = error)
            if MsgBox == 'ok':
                self.currentItem = ""
                self.__clearDataView()
                self.__loadDataView()           
            return

        else:
            
            #result = self.db.select("CALL fn_updatePassword('{}','{}');".format(self.currentItem[0], self.usernameEdited.get()))
            self.db.executeFunction("fn_updatePassword", [self.currentItem[0], self.usernameEdited.get()])

            self.db.update(
                "User",
                ["tex_nickname"],
                ["'{}'".format(self.usernameEdited.get())],
                "tex_nickname = '{}'".format(self.currentItem[0])
                )

            self.usernameEdited.delete("0", "end")
            self.__clearDataView()
            self.__loadDataView()
            MsgBox = messagebox.showinfo(title = 'Éxito', message = "EL nombre de usuario fue cambiado exitosamente.")
            if MsgBox == 'ok':
                self.currentItem = ""
                self.__clearDataView()
                self.__loadDataView()           
                return

    def __editPassword(self):
        self.__clearDataView()
        self.__loadDataView()

        error = ""

        if (self.currentItem):

            if (self.passwordEdited.get() == "Contraseña" or not self.passwordEdited.get()):
                error += "El campo Contraseña está vacío."

            else:
                if (re.search(r"[a-zA-Z0-9._-]{4,}", self.passwordEdited.get()) is None):
                    error += "Contraseña no válida."

        else:
            error += "Debe seleccionar un usuario."            
        
        if (error):
            MsgBox = messagebox.showerror(title = 'Error', message = error)
            if MsgBox == 'ok':
                self.currentItem = ""
                self.__clearDataView()
                self.__loadDataView()           
                return

        else:
            # Objeto para encriptar la contraseña
            data = EncryptDecryptSudokuFile(self.db)
            # Función que ejecuta la operación de UPDATE en la Base de Datos
            self.db.update(
                "User",
                ["tex_password"],
                ["'{}'".format(data.encrypt(self.passwordEdited.get(), self.currentItem[0]))],
                "tex_nickname = '{}'".format(self.currentItem[0])
                )
            MsgBox = messagebox.showinfo(title = 'Operación Éxitosa', message = "Cambio de contraseña Éxitoso.")
            if MsgBox == 'ok':
                self.currentItem = ""
                self.__clearDataView()
                self.__loadDataView()           
                return

    def __editState(self):
        pass
    
    """
    Función que permite regresar a la ventana anterior al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goBack(self):
        self.db.closeConnection()
        self.child.destroy()
        self.parent.deiconify()

    """
    Función que pregunta al usuario si desea salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 3.0
    """
    def __onClosing(self):
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            
            self.db.closeConnection() 
            self.child.destroy()
            sys.exit()
            SudokuBye()
        else:
            pass
