# -*- coding: utf-8 -*-
import os
import re
from tkinter import *
from tkinter.ttk import Treeview

from core.EngineSQL.ConfigConnection import *
from core.EngineSQL.MySQLEngine import *
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.FileManipulation.EncryptDecrypt import *
from core.ScreenCenter import ScreenCenter

"""
Clase que contiene la definición de los componentes donde se permite 
visualizar la lista de todos los usuarios registrados y realizar operaciones
de modifición por parte del usuario administrador.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuUserList(Frame):

    
    #Constructor de la clase donde si incializan todos los componentes de la ventana.
    # Parámetros:
    # - Componente de ventana donde se pintaran los widgets.
    def __init__(self, parent):
        self.parent = parent
        # Se crea otro componente de ventana,
        self.child = Tk()
        # Se captura el evento de cierre de una ventana y se ejecuta la función __onClosing.
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        # Se genera una instancia de la clase que contiene los métodos para obtener
        # los parámetros necesarios para realizar la conexión a la base de datos.
        self.config = ConfigConnection()
        # Se genera una instancia de la clase que contiene los métodos para realizar operaciones
        # sobre la base de datos, se le envía como parámetro la configuración .
        self.db = MySQLEngine(self.config.getConfig())
        # Se inicialiaza la clase Padre (Frame) y se le pasa como parámetro el parent.
        super().__init__(self.child)
        # Se instancia una variable en el constructor para usarla posteriormente,
        self.currentItem = ""
        # Se muestra la ventana,
        self.pack()
        # Se inicializa los widgets que pertenecen a esta ventana.
        self.__initUI()

    
    #Constructor de la clase donde si incializan todos los componentes (widgets) de la ventana.
    def __initUI(self):
        
        # Se establecen las variables de ancho y alto de la ventana.
        self.width = 960
        self.height = 600

        # Se crean instancias de imagenes utilizadas en la Interfáz.
        self.img = PhotoImage(file="core/images/back.png", master=self.child)
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)

        # Se establece el titulo de la ventana.
        self.child.title("Lista de Usuarios")
        # Se bloquea la opción de cambiar de tamaño la ventana.
        self.child.resizable(False, False)
        # Se configura un color de background de la ventana.
        self.child.configure(background = "#171717")
        # Se establece la dimensión de la ventana.
        self.child.geometry("%dx%d"%(self.width, self.height))
        # Se establece el logo de la ventana.
        self.child.iconphoto(True, self.logo)
        
        center = ScreenCenter()
        # Se centra la ventana en la pantalla.
        center.center(self.child, self.width, self.height)

        # Se generan instancias de los botones necesarios en la interfaz
        # Parámetros:
        # - Componente donde se pintará el widget.
        # - Texto a mostrar.
        # - Función a ejectuar al presionar el botón.
        self.userEditButton = Button(self.child, text='Editar usuario', command=self.__editUsername)
        self.stateEditButton = Button(self.child, text='Editar estado', command=self.__editState)
        self.passwordEditButton = Button(self.child, text='Editar contraseña', command=self.__editPassword)

        # Se genera una instancia particular para el botón de "atrás".
        # Parámetros:
        # - Componente donde se pintará el widget.
        # - Imagen a mostrar en el botón
        # - Función a ejectuar al presionar el botón.
        self.backButton= Button(self.child, image=self.img, command= self.__goBack)
        
        # Se configuran diferentes parámetros de los botones
        # Parámetros:
        # - Color de botón.
        # - Fuente para el texto del botón.
        self.userEditButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.stateEditButton.configure(bg="#6ea8d9", font=("Lato", 17))
        self.passwordEditButton.configure(bg="#6ea8d9", font=("Lato", 17))

        # Se configura el botón de "atrás".
        # Parámetros:
        # - Color de botón
        # - Ancho de borde del botón
        # - Acentuación del botón 
        self.backButton.configure(bg="#171717", borderwidth=0, highlightthickness=0)

        # Se ubica en la ventana cada botón utilizando coordenadas
        self.backButton.pack()
        self.backButton.place(x=850, y=20)
        self.userEditButton.pack()  
        self.userEditButton.place(x=170, y=470)
        self.stateEditButton.pack() 
        self.stateEditButton.place(x = 375, y = 470)
        self.passwordEditButton.pack()
        self.passwordEditButton.place(x=575, y=470)

        # Se genera una instancia de TreeView para visualizar a los usuarios.
        # Parámetros:
        # - Componente donde se va a ubicar le widget.
        # - Se definen las columnas a utilizar.
        self.dataView = Treeview(self.child, columns=("#1", "#2"))
        
        # Se definen los encabezados de cada columna.
        # Parámetros:
        # - Número de columna.
        # - Texto del encabezado
        # - Alineación del texto. 
        self.dataView.heading("#0", text="Indice", anchor = CENTER)
        self.dataView.heading("#1", text="Usuario", anchor = CENTER)
        self.dataView.heading("#2", text="Estado", anchor = CENTER)

        # Se definen los parámetros para las columnas a utilzar
        # Parámetros:
        # - Número de columna.
        # - Ancho  columna en pixeles.
        # - Alineación del texto.
        self.dataView.column("#0", width=100, anchor=CENTER)
        self.dataView.column("#1", width=200, anchor=CENTER)
        self.dataView.column("#2", width=250, anchor=CENTER)

        # Se pinta el widget
        self.dataView.pack()
        # Se ubica en la ventana el widget con coordenadas.
        self.dataView.place(x=200, y=120)
        
        # Se definen Labels para titulo y etiquetas en Entry.
        # Parámetros:
        # - Componente donde se va a pintar el widget.
        # - Texto.
        # - Fuente del texto.
        labelUsername= Label(self.child, text='Usuario', font=("Lato",13))
        labelState= Label(self.child, text='Estado', font=("Lato",13))
        labelPassword= Label(self.child, text='Contraseña', font=("Lato",13))
        label1= Label(self.child, text='Lista de Usuarios', font=("Lato",25))

        # Se define instancia singular de label
        # Parámetros:
        # - Componente donde se va a pintar el widget.
        # - Imagen
        # - Ancho del borde.
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        
        # Se configura un color de background y el color de la fuente.
        labelPassword.configure(background = "#171717", fg="white")
        labelUsername.configure(background = "#171717", fg="white")
        labelState.configure(background = "#171717", fg="white")
        label1.configure(background = "#171717", fg="white")

        # Se ubican los Labels usando coordenadas.
        labelUsername.pack()
        labelUsername.place(x=230,y=370)
        labelState.pack()
        labelState.place(x=430,y=370)
        labelPassword.pack()
        labelPassword.place(x=640,y=370)
        label1.pack()
        label1.place(x=345,y=40)
        labelBrand.pack()
        labelBrand.place(x=280,y=550)

        # Se crean Entry que corresponden al nombre de usuario y contraseña respectivamente
        # Parámetros:
        # - Componente donde se pintará el widget.
        # - Fuente .
        # - Alineación de texto.
        self.usernameEdited = Entry(self.child, font=("Lato", 10), justify=CENTER)
        self.passwordEdited = Entry(self.child, font=("Lato", 10), justify=CENTER)
        
        # Se ubican en la ventana usando coordenadas    .
        self.usernameEdited.pack()
        self.usernameEdited.place(x=170, y=400, height=30, width=178)
        self.passwordEdited.pack()
        self.passwordEdited.place(x=575, y=400, height=30, width=217)
        
        # Se crea un ComboBox para el cambio de estado del usuario.
        self.stateCombobox = ttk.Combobox(self.child, state="readonly")

        # Se establecen las opciones del combobox.
        self.stateCombobox["values"] = ["--Seleccione--","Habilitado", "Deshabilitado"]

        # Se configura el combobox.
        self.stateCombobox.configure(width = 19, height = 10, justify=CENTER)
        
        # Se ubica en la ventana con coordenadas.
        self.stateCombobox.place(x=375, y=400)

        # Se establece un elemento por defecto en el combobox.
        self.stateCombobox.current(0)
        
        # Se captura el evento de click en el treeView y cada vez que se cumpla se ejecuta la función
        # __getSelectedItem.
        self.dataView.bind("<ButtonRelease-1>", self.__getSelectedItem)

        # Se carga el contenido del treeView.
        self.__loadDataView()

    # Se obtiene el elemento seleccionado en el treeView para despues obtener los valores de ese
    # elemento seleccionado.
    # Se hace el llamado a las funciones para que se cargue en los Entry  la información del 
    # usuario seleccionado en el TreeView.
    def __getSelectedItem(self, event):
        self.currentItem = self.dataView.focus()
        self.currentItem = self.dataView.item(self.currentItem)
        if(self.currentItem["values"]):
            self.currentItem = self.currentItem["values"]
            self.__informationUser()
            self.__loadComboboxData()

    # Obtiene la información (nombre de usuario y contraseña) desde la base de datos y la inserta
    # en los Entry.
    def __informationUser(self):
        # Realiza la consulta utilizando el nombre de usuario como condición en el WHERE.
        result = self.db.select("SELECT tex_nickname, tex_password FROM User WHERE tex_nickname = '{}';".format(self.currentItem[0]))
        # Obtiene el primer elemento de la tupla retornada.
        dataUser = result[0]
        # Genera una instancia de la herramienta para encriptar/desencriptar.
        # Recibe como parámetro la instancia de la conexión a la base de datos
        data = EncryptDecryptSudokuFile(self.db)
        # Desencripta la contraseña guardada en la base de datos usando el nombre de usuario
        newResult = data.decrypt(dataUser[1], self.currentItem[0])

        # Limpia el texto de los Entry.
        self.__clearEntries()
        self.usernameEdited.insert(1, self.currentItem[0])
        self.passwordEdited.insert(1, newResult)

    # Limpia el texto de los Entry que corrsponde con el nombre de usuario y contraseña.
    def __clearEntries(self):
        self.usernameEdited.delete(0, "end")
        self.passwordEdited.delete(0, "end")
        self.stateCombobox.current(0)

    # Obtiene los nombres de usuario y el estado de los mismos y los posiciona
    # en el dataView.
    def __loadDataView(self):
        # Realiza la consulta utilizando el el rol (administrador, jugador) como condición
        result = self.db.select("SELECT tex_nickname, bit_state FROM User WHERE bit_rol = 0;")
        # Se crea un contador para establecer el indice
        count  = 1
        # Se recorre la tupla obtenida en la consulta a la Base de datos
        for nickname, state in result:
            # Se comprueba si el estado del usuario es "Habilitado"
            if(state == 1):
                # Se inserta en el treeView
                self.dataView.insert("", index=count, text = count, values=(nickname, "Habilitado"))
                # Se comprueba si el estado del usuario es "Deshabilitado"
            else:
                # Se inserta en el treeView
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
        
    # Función encargada de evaluar si se cumplen las condiciones con el *Nombre de Usuario* ingresado en el Entry
    # y con el nombre del usuario seleccionado en el dataView para postetiormente realizar la actualización del campo
    # tex_nickname en la tabla User de la Base de datos.
    def __editUsername(self):

        self.__clearDataView()
        self.__loadDataView()

        # Variable usada para guardar el texto del error.
        error = ""

        # Si hay un elemento seleccionado en el treeView.
        if (self.currentItem):
            
            # Se  comprueba si el Entry del nombre de usuario está vacío.
            if (self.usernameEdited.get() != ""):

                # Se obtienen los nombres de usuarios registrados en la base de datos.
                result = self.db.select("SELECT tex_nickname FROM User;")    

                # Se recorren esos nombres de usuarios y se comprueba que el nombre de usuario este disponible.
                for nickname in result:
                    if (self.usernameEdited.get() == nickname[0]):
                        error += "El nombre de usuario introducido ya está en uso."
                
                # Se comprueba si el nombre de usuario cumple con las restricciones de un nombre de usuario.
                if (re.fullmatch(r"(?=.*[a-zA-Z])[a-zA-Z\d]{4,30}$", self.usernameEdited.get()) is None):
                    error += "El nombre de usuario no es válido."

            # Si el Entry del nombre de usuario está vacío.
            else:
                error += "Debe introducir un nombre de usuario."

        # Si no hay un elemento seleccionado en el treeView.
        else:
            error += "Debe seleccionar un usuario."

        # Si se presentó un error esta condición se cumple y se ejecuta el bloque de código.
        if (len(error) > 0):

            # Se muestra un messageBox con el mensaje de error.
            MsgBox = messagebox.showerror(title = 'Error', message = error)
            # Se limpia el texto en los Entry.
            self.__clearEntries()
            if MsgBox == 'ok':
                # Se establece a cadena vacía la variable donde se almacena los datos del 
                # objeto seleccionado en el treeView.
                self.currentItem = ""
                # Se limpie el treeview.
                self.__clearDataView()
                # Se cargan los datos en el treeview.
                self.__loadDataView()           
            return

        # Si no ocurrió ningún error se ejecuta este bloque de código.
        else:
            
            # Se utiliza un procedimiento almacenado para cambiar el nombre de usuario con el que se encriptará la contraseña.
            self.db.callProc("sp_updatePassword", ["'{}'".format(self.currentItem[0]), "'{}'".format(self.usernameEdited.get())])
            # Se hace commit de los cambios hechos(por el procedimiento almacenado) en la base de datos.
            self.db.mydb.commit()
            
            # Se ejecuta una actualización a la tabla User, se actualiza el campo tex_nickname.
            # Se actualiza el nombre de usuario.
            self.db.update(
                "User",
                ["tex_nickname"],
                ["'{}'".format(self.usernameEdited.get())],
                "tex_nickname = '{}'".format(self.currentItem[0])
                )

            #Inserción de actualización de usuario
            (ToolConnection()).insertBinacle(
                    nickname="admin", 
                    description="El nombre de usuario de {} ha sido actualizado".format(self.currentItem[0])
                )

            # Se muestra un mensaje de operación exitosa.
            MsgBox = messagebox.showinfo(title = 'Éxito', message = "EL nombre de usuario fue cambiado exitosamente.")
            # Se limpia el texto en los Entry.
            self.__clearEntries()
            if MsgBox == 'ok':
                # Se establece a cadena vacía la variable donde se almacena los datos del 
                # objeto seleccionado en el treeView.
                self.currentItem = ""
                # Se limpia el treeView.
                self.__clearDataView()
                # Se cargan los datos al treeView.
                self.__loadDataView()
                return

    # Función encargada de validar el cambio de contraseña que el adminstrador desea hacer sobre el usuario
    # seleccionado en el dataView, posteriormente si las validaciones son correctas, se procede a actualizar el campo
    # tex_password en la tabla User de la Base de datos.
    def __editPassword(self):
        # Se limpia el treeView.
        self.__clearDataView()
        # Se cargan los datos al treeView.
        self.__loadDataView()

        # Variable usada para guardar el texto del error.
        error = ""

        # Se comprueba si hay un elemento seleccionado en el treeView.
        if (self.currentItem):
            
            # Se comprueba si el Entry de contraseña está vacío.
            if (not self.passwordEdited.get()):
                error += "El campo Contraseña está vacío."

            # Si el Entry no está vacío 
            else:
                # Se comprueba que la contraseña cumpla con las restricciones.
                if (re.fullmatch(r"^(?=\w*\d*)(?=\w*[a-z]*)(?=\w*[A-Z]*)(?=\w*[a-zA-Z]*)[a-zA-Z\*\_\d]{4,32}$", self.passwordEdited.get()) is None):
                    error += "Contraseña no válida."

        # Si no hay un elemento seleccionado en el treeView.
        else:
            error += "Debe seleccionar un usuario."            
        
        # Si se presentó al menos un error.
        if (error):
            # Se muestra un messageBox de Error con el texto del error que ocurrió.
            MsgBox = messagebox.showerror(title = 'Error', message = error)
            # Se limpia el texto en los Entry
            self.__clearEntries()
            if MsgBox == 'ok':
                # Se establece a cadena vacía la variable donde se almacena los datos del 
                # objeto seleccionado en el treeView.
                self.currentItem = ""
                # Se limpia el treeView.
                self.__clearDataView()
                # Se cargan los datos al treeView.
                self.__loadDataView()
                return

        # Si no ocurrió ningún error se ejecutan las operaciones sobre la base de datos.
        else:
            # Objeto para encriptar la contraseña.
            data = EncryptDecryptSudokuFile(self.db)

            # Función que ejecuta la operación de UPDATE en la Base de Datos
            # Se actualiza el campo tex_password en la tabla User usando el nombre 
            # de usuario como condición.
            self.db.update(
                "User",
                ["tex_password"],
                ["'{}'".format(data.encrypt(self.passwordEdited.get(), self.currentItem[0]))],
                "tex_nickname = '{}'".format(self.currentItem[0])
                )
            
            #Inserción de actualización de contraseña
            (ToolConnection()).insertBinacle(
                    nickname="admin", 
                    description="La contraseña del usuario {} ha sido actualizada".format(self.currentItem[0])
                )

            # Se mustra un messageBox de éxito.
            MsgBox = messagebox.showinfo(title = 'Operación Éxitosa', message = "Cambio de contraseña Éxitoso.")
            # Se limpia el texto en los Entry
            self.__clearEntries()
            if MsgBox == 'ok':
                # Se establece a cadena vacía la variable donde se almacena los datos del 
                # objeto seleccionado en el treeView.
                self.currentItem = ""
                # Se limpia el treeView.
                self.__clearDataView()
                # Se cargan los datos al treeView.
                self.__loadDataView()
                return

    # Función que permite al administrador hacer el cambio de estado de un usuario.
    # Los posibles estados(Habilitado, Deshabilitaoo) le permiten a un usuario hacer uso del juego.
    def __editState(self):
        
        #C Comprueba si hay un usuario seleccionado en el dataView
        if (self.currentItem):
            
            # Se comprueba si el usuario ya cuenta con el estado que está precargado en el Combobox
            if (self.currentItem[1] == self.stateCombobox.get()):
                # Se muestra un messageBox con la información.
                MsgBox = messagebox.showinfo(
                    title='Información',
                    message="El usuario seleccionado ya está {}.".format(self.stateCombobox.get())
                )
                if MsgBox == 'ok':
                    # Se establece a cadena vacía la variable donde se almacena los datos del 
                    # objeto seleccionado en el treeView.
                    self.currentItem = ""
                    # Se limpia el treeView.
                    self.__clearDataView()
                    # Se cargan los datos al treeView.
                    self.__loadDataView()
                    return
            
            # Si no cuenta con el estado precargado en el combobox.
            else:
                # Se actualiza el estado del usuario según la opción seleccionada en el combobox.
                if (self.stateCombobox.get() == "Habilitado"):
                    self.db.update("User", ["bit_state"], [1], "tex_nickname = '{}'".format(self.currentItem[0]))

                    #Recuperación de estado de usuario
                    (ToolConnection()).insertBinacle(
                                    nickname="admin", 
                                    description="El acceso del usuario {} ha sido habilitado".format(self.currentItem[0])
                                )
                                
                else:
                    self.db.update("User", ["bit_state"], [0], "tex_nickname = '{}'".format(self.currentItem[0]))
                    
                    #Eliminación de usuario del sistema
                    (ToolConnection()).insertBinacle(
                                    nickname="admin", 
                                    description="El acceso del usuario {} ha sido deshabilitado".format(self.currentItem[0])
                                )

                # Se muestra un meesagebox de éxtio.
                MsgBox = messagebox.showinfo(
                    title='Éxito',
                    message="Actualización de estado completada."
                )

                # Se limpia el texto de los Entry.
                self.__clearEntries()

                if MsgBox == 'ok':
                    # Se establece a cadena vacía la variable donde se almacena los datos del 
                    # objeto seleccionado en el treeView.
                    self.currentItem = ""
                    # Se limpia el treeView.
                    self.__clearDataView()
                    # Se cargan los datos al treeView.
                    self.__loadDataView()
                    return
                
        # Si no hay un usuario seleccionado en el treeView
        else:
            # Se muestra un messagebox de Error.
            MsgBox = messagebox.showerror(
                    title='Error',
                    message="Debe seleccionar un usuario."
                )
            if MsgBox == 'ok':
                # Se establece a cadena vacía la variable donde se almacena los datos del 
                # objeto seleccionado en el treeView.
                self.currentItem = ""
                # Se limpia el treeView.
                self.__clearDataView()
                # Se cargan los datos al treeView.
                self.__loadDataView()
                return
    
    
    # Permite regresar a la ventana anterior al presionar el botón.
    def __goBack(self):
        # Cierra la conexión de Base de datos
        self.db.closeConnection()
        # Destruye la ventana actual
        self.child.destroy()
        # Muestra la ventana Anterior
        self.parent.deiconify()

    
    # Función ejecutada cada vez que se intenta cerrar la ventana. 
    # Se muestra una ventana que solicita al usuario confirmación de cierre.
    def __onClosing(self):
        # Se muestra una ventana de confirmación
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            # Se cierra la conexión a la base de datos.
            self.db.closeConnection()
            # Se destruye la ventana actual.
            self.child.destroy()
            # Se cierra la ejecución de la aplicación
            sys.exit()
            # Se muestra una ventana de despedida.
            SudokuBye()
        else:
            pass
