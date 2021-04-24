# -*- coding: utf-8 -*-
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk

from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.ScreenCenter import ScreenCenter
from core.SudokuByeUI import SudokuBye

"""
Frame que permite visualizar todos los componentes de la bitacora.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuAdministratorBinnacle(Frame):

    # Constructor de la clase donde si incializan todos los componentes de la ventana.
    def __init__(self, parent=None):
        self.parent = parent
        # Se inicializa un nuevo componente de tkinter
        self.child = Tk()
        # Se captura el evento de cierre de una ventana y se ejecuta la función __onClosing.
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        # Conexión al archivo de configuración
        self.config = ConfigConnection() 
        # Conexión a la base de datos
        self.db = MySQLEngine(self.config.getConfig()) 
        # Se pinta la ventana
        self.pack()
        # Se inicalizan los widgets de la ventana
        self.__initUI()
    
    # Creación de los widgets que se veran en pantalla.
    def __initUI(self):
        # Se cargan las imagenes que use usarán en la ventana
        self.img = PhotoImage(file="core/images/back.png", master=self.child)
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)

        # Se definen los valores de ancho y alto para la ventana
        self.width = 960
        self.height = 540

        # Se establece el titulo de la ventana
        self.child.title('Bitácora')
        # Se establece las dimensiones de la venatan
        self.child.geometry("{}x{}".format(self.width, self.height))
        # Se establece el color de background de la ventana
        self.child.configure(background = "#171717")
        # Se bloquea la opción de cambiar el tamaño a la ventana
        self.child.resizable(False, False)

        # Se crean los botones
        self.backButton= Button(self.child, image=self.img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        # Se pinta el widget en la ventana
        self.backButton.pack()
        # Se ubica el widget utilizando coordenadas
        self.backButton.place(x=880, y=20)
        
        # Se centra la ventana en pantalla
        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)

        # Se crea un treeview para mostrar los datos de la bitácora
        self.dataView = ttk.Treeview(self.child, columns=("#1","#2", "#3"))
        # Se pinta el treview
        self.dataView.pack()

        # Se fijan los encabezados de las columnas y se establece su alineción a central
        self.dataView.heading("#0", text="Indice", anchor = CENTER)
        self.dataView.heading("#1", text="Usuario", anchor = CENTER)
        self.dataView.heading("#2", text="Descripción actividad", anchor = CENTER)
        self.dataView.heading("#3", text="Fecha y Hora", anchor = CENTER)

        # Se establece el número de columnas y se establece su alineción a central
        self.dataView.column("#0", width=50, anchor = CENTER)
        self.dataView.column("#1", width=200, anchor = CENTER)
        self.dataView.column("#2", width=420)
        self.dataView.column("#3", width=180, anchor = CENTER)

        # Se establece la posición del widget en la ventana usando coordenadas
        self.dataView.place(x=45, y=160)
        
        # Se definen un label para mostrar el titulo de la ventana, se define la fuente a utilizar
        label1= Label(self.child, text='Registro de bitácora', font=("Lato",25))
    
        # Se establece un label como contenedor de la imagen del botón de atras
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        
        # Se configura el color de background y el color de la fuente del label
        label1.configure(background = "#171717", fg="white")
        
        # Se pinta los widgets
        label1.pack()
        labelBrand.pack()

        # Se establece su ubicación en la ventana usando coordenadas
        label1.place(x=335,y=90)
        labelBrand.place(x=280,y=485)

        # Se carga la información de la bitácora
        self.loadBinacle()

    # Obtiene todas los registros o actividades de cada uno de los usuarios 
    # (login, log-out, fecha y hora, estado del tablero)
    def loadBinacle(self) -> None: 
        
        # Se prepara la query
        query = """
                SELECT 
                    tex_nickname, 
                    tex_description, 
                    tim_date
                FROM 
                    Binacle 
                ORDER BY 
                    tim_date ASC
                ;
        """
        # Se efectua la query y se guarda el resultado en la variable
        transaction = self.db.select( query=query )

        # Si hay resultados...
        if transaction:
            # Se obtiene la cantidad de elementos obtenidos de la consulta
            count = len(transaction)
            # Se recorre los resultados de la consulta
            for data in transaction:
                # Se establece las entradas en el dataview
                self.dataView.insert("", 0, text="{}".format(count) , values=(data[0], data[1], data[2]))
                count -=1

    # Función que permite regresar a la ventana anterior al presionar el botón.
    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()
    
    # Función que pregunta al usuario si desea salir del juego.
    def __onClosing(self):
        # Se muestra un messagebox solicitando confirmación
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            
            # Se destruye la ventana actual
            self.child.destroy()
            # Se termina la ejecución del programa 
            sys.exit()
            # Se muestra la ventana de despedida
            SudokuBye()
