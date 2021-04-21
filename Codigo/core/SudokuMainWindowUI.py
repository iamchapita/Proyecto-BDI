# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from core.ScreenCenter import ScreenCenter
from core.SudokuGame import SudokuGame
from core.SudokuBoardUI import SudokuBoardUI
from core.SudokuScoreboardUI import SudokuScoreboardUI
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.SudokuByeUI import SudokuBye

import os


"""
Frame que muestra el Main Window y todos sus respectivos widgets de la aplicación
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuMainWindowUI(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self, username= ""):
        self.parent = Tk()
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.config = ConfigConnection() #Conexión al archivo de configuración        
        self.db = MySQLEngine( self.config.getConfig() ) #Conexión a la base de datos
        self.idBoard = None #Numero del board seleccionado
        super().__init__(self.parent)

        self.username = ""
        self.idUsername = None
        self.getUsernameLogin()   

        self.__initUI()
        self.master.mainloop()     

    """
    Creación de los widgets que se veran en pantalla.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        self.width = 400
        self.height = 600
        self.parent.title('Menu')
        self.parent.iconphoto(True, self.icon)

        self.parent.geometry("%dx%d" % (self.width, self.height))
        self.parent.configure(background = "#171717")
        self.parent.resizable(False, False)

        self.center = ScreenCenter()
        self.center.center(self.parent, self.width, self.height)

        label1= Label(self.parent, text='¿Qué deseas hacer?', font=("lato", 20))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80, padx=70)

        Button(self.parent, text = 'Nuevo juego', bg="#6ea8d9", font=("lato", 17), command= self.__newGame).grid(row=2,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=37)
        Button(self.parent, text = 'Continuar juego', bg="#6ea8d9", font=("lato", 17), command= self.__continueGame).grid(row=3,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=18)
        Button(self.parent, text = 'Mejores puntajes', bg="#6ea8d9", font=("lato", 17), command= self.__bestScores).grid(row=4,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=11)
        Button(self.parent, text = 'Salir', bg="#6ea8d9", font=("lato", 17), command= self.__onClosing).grid(row=5,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=83)
        
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.grid(row=6,column=1,pady = 130)

    """
    Función que inicia el juego cuando se presiona el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __newGame(self):
        #Estado del último juego jugado
        query = """
                SELECT 
                    State.cod_state AS state, 
                    Board.idboard AS idboard
                FROM 
                    State
                INNER JOIN 
                    (
                        SELECT
                            id, 
                            id_sudokuboard_fk AS idboard,
                            tim_time AS time
                        FROM 
                            Game
                        WHERE 
                            id_user_fk={}
                        ORDER BY 
                            tim_date DESC
                        LIMIT 1
                    ) Board ON State.id_game_fk = Board.id
                ORDER BY 
                    State.tim_date DESC
                LIMIT 1
                """.format( self.idUsername )

        #Nueva conexión a la bd
        newConnection = MySQLEngine(self.config.getConfig())
        transaction = newConnection.select(query=query)

        if transaction: 
            state, self.idBoard= transaction[0]
        
            #El estado del Board es 'derrota'
            if state == "derrota":
                MsgBox = messagebox.askquestion ('Sudoku','¿Deseas utilizar el mismo tablero de la partida finalizada como derrota?',icon = 'warning')
                if MsgBox == 'yes':
                    tool = ToolConnection()
                    filename = "n00b.sudoku"

                    tool.insertGameBoard(
                                                username=self.username, 
                                                idUsername=self.idUsername, 
                                                idBoard=self.idBoard
                                )
                    
                    self.openSudokuBoard(filename=filename) 
                else:
                    self.__generateNewBoard()
            else:
                self.__generateNewBoard()
        else:
                self.__generateNewBoard()
                
        newConnection.closeConnection()

    def __generateNewBoard(self):
        tool = ToolConnection()
        filename = "n00b.sudoku"

        #Carga la información de sudokuBoard al archivo n00b.sudoku
        self.idBoard = tool.processFile(filename=filename)

        #Carga la información de tablero 'nuevo' a la base de datos
        #self.__createNewGame()
        tool.insertGameBoard(
                                    username=self.username, 
                                    idUsername=self.idUsername, 
                                    idBoard=self.idBoard
                    )
        
        self.openSudokuBoard(filename=filename)    
        
    """
        Se lee el contenido del documento .sudoku 
        y se escribe en el Board del puzzle    
    """    
    def openSudokuBoard(self, filename: str, time = []) -> None:
        with open('core/sudoku/{}'.format(filename), 'r') as boardFile:
            self.parent.withdraw()
            game = SudokuGame(boardFile)
            game.start()
            root = Tk()

            if(time):
                SudokuBoardUI(root, game, "", self.parent, time[0], time[1], time[2])
            else:
                SudokuBoardUI(root, game, "", self.parent)

            root.mainloop()


    """
    Función que permite continuar un juego pausado.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0

        - Verificar el último tablero creado en la base de datos, que este sea igual a 'pausado'
        - Sí el archivo es 'pausado'
            - obtener el identificador del Board
            - Buscar este identificador en la entidad SudokuBoard
            - Cargarlo en el archivo.sudoku
            - Traer la pila, desencriptarla 
            - Cargar la pila al Tablero
    """
    def __continueGame(self):

        #Estado del último juego jugado
        query = """
                SELECT 
                    State.cod_state AS state, 
                    Board.idboard AS idboard,
                    Board.time AS time
                FROM 
                    State
                INNER JOIN 
                    (
                        SELECT
                            id, 
                            id_sudokuboard_fk AS idboard,
                            tim_time AS time
                        FROM 
                            Game
                        WHERE 
                            id_user_fk={}
                        ORDER BY 
                            tim_date DESC
                        LIMIT 1
                    ) Board ON State.id_game_fk = Board.id
                ORDER BY 
                    State.tim_date DESC
                LIMIT 1
                """.format( self.idUsername )

        #Nueva conexión a la bd
        newConnection = MySQLEngine(self.config.getConfig())
        transaction = newConnection.select(query=query)

        if transaction: 
            state, self.idBoard, timeStored = transaction[0]
        
            #El estado del Board es 'pausado'
            if state == "pausado":

                tool = ToolConnection()
                filename = "n00b.sudoku"

                #Carga la información de sudokuBoard al archivo n00b.sudoku
                tool.processFile(filename=filename, idBoard=self.idBoard)

                tool.updateState(idUsername=self.idUsername, state=5) #5 'continuar'
                
                timeStored = str(timeStored).split(":")

                self.openSudokuBoard(filename, list(timeStored))
            else:
                messagebox.showinfo(message="No hay partidas en Pausa.", title="Información")
                return

        newConnection.closeConnection()

    """
    Función que permite visualizar los mejores puntajes.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __bestScores(self):
        
        #Un usuario visualiza la tabla de puntuaciones
        (ToolConnection()).bestScore()
        
        self.parent.withdraw()
        SudokuScoreboardUI(parent=self.parent)

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
            
            self.parent.destroy()
            self.db.closeConnection()
            SudokuBye()

        else:
            pass

    """
    Función que asigna los valores de inicio de sesión del usuario 
    logeado (id, username)
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """        
    def getUsernameLogin(self):

        self.idUsername, self.username, self.rol = (ToolConnection()).getLastLoginUser()

        print( "A VER id: {}, username: {}".format(self.idUsername, self.username) )