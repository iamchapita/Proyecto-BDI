from tkinter import *
from tkinter import ttk
from core.ScreenCenter import ScreenCenter
from core.SudokuByeUI import SudokuBye
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.FileManipulation.EncryptDecrypt import EncryptDecryptSudokuFile
import os
import re

"""
Frame que permite visualizar todos los scoreboards del juego.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuScoreboardUI(Frame):

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
        img = PhotoImage(file="core/images/back.png", master=self.child)
        btnBack= Button(self.child, image=img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        btnBack.pack()
        btnBack.place(x=850, y=20)
        self.config = ConfigConnection() #Conexión al archivo de configuración
        self.db = MySQLEngine(self.config.getConfig()) #Conexión a la base de datos
        self.username = ""
        self.idUsername = None
        self.idBoard = None #Numero del board seleccionado
        self.getUsernameLogin()
        self.__initUI()
        self.master.mainloop()

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):

        self.width = 960
        self.height = 545
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.child.title("Scoreboard")
        self.child.resizable(False, False)
        self.child.configure(background = "#171717")
        self.child.geometry("%dx%d"%(self.width, self.height))
        self.child.iconphoto(True, self.logo)
        center = ScreenCenter()
        center.center(self.child, self.width, self.height)
        self.dataView = ttk.Treeview(self.child, columns=("#1","#2","#3"))
        self.dataView.pack()
        self.dataView.heading("#0", text="Indice")
        self.dataView.heading("#1", text="Usuario")
        self.dataView.heading("#2", text="Mejor Tiempo")
        self.dataView.heading("#3", text="Fecha y Hora")
        self.dataView.place(x=40, y=160)
        self.dataView.column("#0", width=100)
        self.dataView.column("#1", width=200)
        self.dataView.column("#2", width=250)
        self.dataView.column("#3", width=300)

        # Muestra el titulo de la seccion
        label1= Label(self.child, text='Scoreboard', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=380,y=90)

        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=280,y=485)
        self.loadText()

    """
        Asigna los valores de inicio de sesión del usuario 
        logeado (id, username)
    """        
    def getUsernameLogin(self):
        
        tool = ToolConnection()

        self.idUsername, self.username, self.rol = tool.getLastLoginUser()



    """
    Función que permite leer los mejores puntajes provenientes de una 
    consulta de la base de datos e insertarlos en una tabla de tkinter.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.1
    """
    def loadText(self):
        #Las mejores 10 puntuaciones de todos los juegos jugados por un usuario (siendo estas 'finalizadas')
        #Esta consulta se realiza de está forma debido a la naturaleza del data view
        query = """
                    SELECT 
                        Result.time AS time,
                        Result.date AS date
                    FROM
                    (
                        SELECT 
                            Game.tim_time AS time, 
                            Game.tim_date AS date
                        FROM 
                            Game
                        INNER JOIN 
                        (
                            SELECT 
                                id_game_fk
                            FROM 
                                State
                            WHERE 
                                cod_state=4 -- DERROTAS, CAMBIAR ESTE ESTADO DESPUES
                        ) BoardState ON Game.id = BoardState.id_game_fk
                        WHERE 
                            Game.id_user_fk={}
                        ORDER BY 
                            Game.tim_time DESC
                        LIMIT 10
                    ) Result
                    ORDER BY 
                        Result.time ASC;
                """.format( self.idUsername )

        transaction = self.db.select( query=query )

        if transaction:
            count = len(transaction)
            for data in transaction:
                self.dataView.insert("", 0, text="{}".format(count) , values=(self.username, data[0], data[1]))
                count -=1
        else: 
            print("El jugador no tiene juegos finalizados")

   
    """
    Función que permite regresar a la ventana anterior al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goBack(self):
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
            #Cierra la conexión a la base de datos
            self.db.closeConnection()

            self.child.destroy()
            sys.exit()
            SudokuBye()
        else:
            pass
