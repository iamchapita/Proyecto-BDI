# -*- coding: utf-8 -*-
import tkinter.font as tkFont
from tkinter import *

from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.ScreenCenter import ScreenCenter
from core.SudokuByeUI import SudokuBye

"""
Frame que permite visualizar los elementos cuando se elimina un usuario
del juego y la BD.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuAdministratorDeleteUser(Frame):

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
        self.pack()
        self.__initUI()
        self.config = ConfigConnection() 
        self.db = MySQLEngine(self.config.getConfig())
        img = PhotoImage(file="core/images/back.png", master=self.child)
        btnBack= Button(self.child, image=img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        btnBack.pack()
        btnBack.place(x=315, y=20)
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
        self.child.title('Eliminar Usuarios')
        self.child.geometry("%dx%d" %(self.width, self.height))
        self.child.configure(background = "#171717")
        self.child.resizable(False, False)

        label1= Label(self.child, text='Eliminar usuario', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=80,y=120)

        label2= Label(self.child, text='Introduzca el nombre de usuario a eliminar:', font =("Lato",15))
        label2.configure(background = "#171717", fg="#6ea8d9")
        label2.pack()
        label2.place(x=10,y=200)

        input_text = StringVar()
        self.userText = ttk.Entry(self.child, textvariable = input_text, font=("Lato",10),  justify=CENTER)
        self.userText.pack()
        self.userText.place(x=110,y=250, height = 30, width = 200)

        Button(self.child, text = 'Eliminar', command= self.__save, bg="#6ea8d9", font=("Lato",15)).place(x=155, y=340, height = 50, width = 110)

        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=8,y=555)

    """
    Función que permite guardar los cambios.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __save(self):
        # delete(self, table, tex_nickname): 
        username = self.userText.get()
        print(username)
        
        #Sí el text no está vacío
        if username: 

            userExist = self.db.select("SELECT tex_nickname FROM User WHERE tex_nickname = %s AND bit_state = 1", (username, ))
            print( userExist )

            #Consulta hacia la base de datos sobre el nickname del usuario
            if userExist: 
                #Sí el usuario existe se valida coincidencia con el usuario buscado
                if userExist[0][0] == username: 
                    #Se modifica el estado del usuario de " (1) activo" a (0) "inactivo"
                    self.db.update(
                            table="User", 
                            fields=("bit_state", ), 
                            values=(0,),
                            condition="tex_nickname = '{}' AND bit_state = 1".format(username)
                        )
                    
                    self.userText.delete(0, "end") 

                    print( "Se cambió el estado de {}".format(username) )

            else: 
                messagebox.showerror(title="Usuario inexistente", message="El usuario no existe en la base de datos.")

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
    @version 3.0
    """
    def __onClosing(self):


        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            
            self.child.destroy()
            self.db.closeConnection() 
            sys.exit()
            SudokuBye()
        else:
            pass
