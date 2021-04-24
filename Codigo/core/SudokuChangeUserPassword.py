# -*- coding: utf-8 -*-
"""
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
import re
from tkinter import *

from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.FileManipulation.EncryptDecrypt import EncryptDecryptSudokuFile
from core.ScreenCenter import ScreenCenter
from core.SudokuByeUI import SudokuBye
from core.SudokuMainWindowUI import SudokuMainWindowUI
from core.Tooltip import Tooltip

"""
Frame que muestra el Login y todos sus respectivos widgets de la aplicación
"""
class SudokuChangeUserPassword(Frame):

    def __init__(self, username, password):
        # Instancia de la ventana padre.
        self.parent = Tk()
        # Se captura el evento de cierre de una ventana y se ejecuta la función __onClosing.
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)

        # Se asignan a variables globales las variables recibidas
        self.username = username
        self.password = password

        # Conección al archivo de configuración
        self.config = ConfigConnection()
        #Conexión a la base de datos
        self.db = MySQLEngine(self.config.getConfig())

        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        # Se cargan las imagenes que use usarán en la ventana
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        
        self.parent.iconphoto(True, self.logo)
        # Se definen los valores de ancho y alto para la ventana
        self.width = 400
        self.height = 600

        # Se establece las dimensiones de la ventana
        self.parent.geometry("%dx%d"%(self.width, self.height))
        # Se establece el titulo de la ventana
        self.parent.title("Cambio de contraseña")
        # Se bloquea la opción de cambiar el tamaño a la ventana
        self.parent.resizable(False, False)
        # Se establece el color de background de la ventana
        self.parent.configure(background = "#171717")
        
        # Se centra la ventana en pantalla
        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)
        
        # Muestra el titulo de la sección
        label1 = Label(
            self.parent,
            text='¡Bienvenido {}!\n Este es su primer\n ingreso a SUDOKU, \ndebe cambiar obligatoriamente\n su contraseña.'.format(self.username),
            font=("Lato", 15)
            )
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 50, padx=50)
    
        # Muestra el título del entry
        label3= Label(self.parent, text='Ingrese su nueva contraseña', font =("Lato",13))
        label3.configure(background = "#171717", fg="#6ea8d9")
        label3.grid(row=2,column=1,sticky = "nsew", padx=77)

        # Instancia del tooltip y características que se muestran al pasar el cursor sobre el entry de contraseña 
        textTooltip ="""{} de más de 4 caracteres.\nCaracteres válidos: \n- Mayúsculas\n- Minúsculas\n- Números\n- Simbolos (._-)"""
        self.newPasswordEntry = Entry(self.parent,show="*", font=("Lato",13),  justify=CENTER)
        self.newPasswordEntry.grid(row=3,column=1,sticky = "nsew",pady=20 ,padx=77,ipady=1, ipadx=1)
        self.passwordToolTip = Tooltip(self.newPasswordEntry, textTooltip.format("Contraseña"))
        
        # Creación de botón y definición de características del botón de confirmar contraseña.
        self.loginButton = Button(self.parent, command=lambda: self.__changePassword(self.newPasswordEntry.get()))
        self.loginButton.configure(text="Confirmar contraseña", bg="#6ea8d9", font=("Lato", 15))
        self.loginButton.grid(row=6,column=1,sticky = "nsew", pady = 15, padx=77,ipady=1, ipadx=10)

        # Se establece un label como contenedor de la imagen de la marca del juego.
        labelBrand = Label(self.parent, image=self.brand, borderwidth=0)
        labelBrand.grid(row=7,column=1,sticky = "nsew", pady = 150, padx=10)

    def __changePassword(self, password):
        error = ""
        #objeto para encriptar los datos de la contraseña
        data = EncryptDecryptSudokuFile(self.db)

        if (len(password) > 0):
            # Condicional de definición de la regex para el campo de password
            if (re.fullmatch(r"^(?=\w*\d*)(?=\w*[a-z]*)(?=\w*[A-Z]*)(?=\w*[a-zA-Z]*)[a-zA-Z\*\_\d]{4,32}$", password) is None):
                error += "Usuario o Contraseña no válido.\n"    
            # Sí la nueva password es igual a la anterior, se retorna un mensaje de error.
            elif (password == self.password):
                error += "Debe cambiar la contraseña.\nIntroduzca una nueva contraseña."

        # Sí el campo está vacío se retorna el msj indicándolo
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
            # Sí no hay ningún error entonces se guarda la nueva contraseña en la base de datos.
            obj = self.db.update(
                    table="User",
                    fields=("tex_password",),
                    values=( "'{}'".format( data.encrypt(password, self.username) ), ), # (data, password)
                    condition="tex_nickname = '{}'".format(self.username)
                )
            # Se cierra la conexión a la base de datos
            self.db.closeConnection()
            # Se destruye la ventana de cambio de contraseña
            self.parent.destroy()
            # Se ejecuta la ventana main del juego para el usuario.
            SudokuMainWindowUI()
    
    """
    Función que pregunta al usuario si desea salir del juego.
    """
    def __onClosing(self):
        # Confirmación sobre cerrado de la aplicación
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            # Se destruye la ventana actual
            self.parent.destroy()
            # Se cierra la conexión a la base de datos
            self.db.closeConnection()
            # Se muestra la ventana de despedida
            SudokuBye()
        else:
            pass
