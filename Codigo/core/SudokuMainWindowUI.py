# -*- coding: utf-8 -*-
"""
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
import os
from tkinter import *
from tkinter import messagebox

from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.ScreenCenter import ScreenCenter
from core.SudokuBoardUI import SudokuBoardUI
from core.SudokuByeUI import SudokuBye
from core.SudokuGame import SudokuGame
from core.SudokuScoreboardUI import SudokuScoreboardUI

"""
Frame que muestra el Main Window y todos sus respectivos widgets de la aplicación
"""
class SudokuMainWindowUI(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    """
    def __init__(self, username= ""):
        self.parent = Tk()
        # Se captura el evento de cierre de una ventana y se ejecuta la función __onClosing.
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.config = ConfigConnection() #Conexión al archivo de configuración        
        self.db = MySQLEngine( self.config.getConfig() ) #Conexión a la base de datos
        self.idBoard = None #Numero del board seleccionado
        super().__init__(self.parent)

        # Creación de variables globales
        self.username = ""
        self.idUsername = None

        # Instancia para obtener el nombre de usuario log
        self.getUsernameLogin()   

        self.__initUI()
        self.master.mainloop()     

    """
    Creación de los widgets que se veran en pantalla.
    """
    def __initUI(self):
        # Se cargan las imagenes que use usarán en la ventana
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        # Se establece el titulo de la ventana
        self.parent.title('Menú')
        # Establece el ícono de la ventana.
        self.parent.iconphoto(True, self.icon)
        # Se definen los valores de ancho y alto para la ventana
        self.width = 400
        self.height = 600

        # Se establece las dimensiones de la ventana
        self.parent.geometry("%dx%d" % (self.width, self.height))
        # Se establece el color de background de la ventana
        self.parent.configure(background = "#171717")
        # Se bloquea la opción de cambiar el tamaño a la ventana
        self.parent.resizable(False, False)

        # Se centra la ventana en pantalla
        self.center = ScreenCenter()
        self.center.center(self.parent, self.width, self.height)

        # Se define un label para mostrar el titulo de la ventana, se define la fuente a utilizar
        label1= Label(self.parent, text='¿Qué deseas hacer?', font=("lato", 20))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80, padx=70)

        # Se crean los botones y características de los botones
        Button(self.parent, text = 'Nuevo juego', bg="#6ea8d9", font=("lato", 17), command= self.__newGame).grid(row=2,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=37)
        Button(self.parent, text = 'Continuar juego', bg="#6ea8d9", font=("lato", 17), command= self.__continueGame).grid(row=3,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=18)
        Button(self.parent, text = 'Mejores puntajes', bg="#6ea8d9", font=("lato", 17), command= self.__bestScores).grid(row=4,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=11)
        Button(self.parent, text = 'Salir', bg="#6ea8d9", font=("lato", 17), command= self.__onClosing).grid(row=5,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=83)
        
        # Se establece un label como contenedor de la imagen de la marca del juego.
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.grid(row=6,column=1,pady = 130)

    """
    Función que inicia el juego cuando se presiona el botón.
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
        # Se ejecuta la query y se asigna a la variable transacción
        transaction = newConnection.select(query=query)
        # Si hay una transacción 
        if transaction: 
            # Se asignan los elementos de la primera posición la objeto transacción
            state, self.idBoard= transaction[0]
        
            #El estado del Board es 'derrota'
            if state == "derrota":
                # Se muestra el message de confirmación si el usuario desea un nuevo board ó el mismo de la partida que se acaba de finalizar
                MsgBox = messagebox.askquestion ('Sudoku','¿Deseas utilizar el mismo tablero de la partida finalizada como derrota?',icon = 'warning')
                # Si la respuesta es si:
                if MsgBox == 'yes':
                    # Se establece la conexión a la base de datos para obtener el board de la última partida
                    tool = ToolConnection()
                    filename = "n00b.sudoku"

                    tool.insertGameBoard(
                                                username=self.username, 
                                                idUsername=self.idUsername, 
                                                idBoard=self.idBoard
                                )
                    # Se llama a la función de mostrar el board.
                    self.openSudokuBoard(filename=filename) 
                else:
                    # Si la respuesta es no se genera un nuevo board
                    self.__generateNewBoard()
            else:
                # Sí el estado del último board no es derrota, entonces se generará un nuevo board.
                self.__generateNewBoard()
        else:
            # Sí no hay transacción, entonces se generará un nuevo board.
            self.__generateNewBoard()

        # Se cierra la conexión de la base de datos. 
        newConnection.closeConnection()

    def __generateNewBoard(self):
        tool = ToolConnection()
        filename = "n00b.sudoku"

        #Carga la información de sudokuBoard al archivo n00b.sudoku
        self.idBoard = tool.processFile(filename=filename)

        #Carga la información de tablero 'nuevo' a la base de datos
        tool.insertGameBoard(
                                    username=self.username, 
                                    idUsername=self.idUsername, 
                                    idBoard=self.idBoard
                    )
        
        # Se llama a la función de mostrar el board.
        self.openSudokuBoard(filename=filename)    
        
    """
        Se lee el contenido del documento .sudoku 
        y se escribe en el Board del puzzle    
    """    
    def openSudokuBoard(self, filename: str, time = []) -> None:
        # Se pinta el board a utilizar
        with open('core/sudoku/{}'.format(filename), 'r') as boardFile:
            self.parent.withdraw()
            game = SudokuGame(boardFile)
            game.start()
            root = Tk()

            # Sí hay un tiempo entonces se envía en forma de parámetros a la clase board 
            if(time):
                SudokuBoardUI(root, game, "", self.parent, time[0], time[1], time[2])
            # Si no hay entonces se establece el tiempo por defecto
            else:
                SudokuBoardUI(root, game, "", self.parent)

            root.mainloop()


    """
    Función que permite continuar un juego pausado.

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
                # Se actualiza el estado
                tool.updateState(idUsername=self.idUsername, state=5) #5 'continuar'
                # Se separa el tiempo por ":", para crear una lista 
                timeStored = str(timeStored).split(":")
                # Se hace el llamado a la función SudokuBoard
                self.openSudokuBoard(filename, list(timeStored))
            else:
                # Si no hay partidas en pausa, se muestra un mensaje indicándolo.
                messagebox.showinfo(message="No hay partidas en Pausa.", title="Información")
        else:
            # Si no hay transacción, se muestra un mensaje indicándolo.
            messagebox.showinfo(message="No hay partidas en Pausa.", title="Información")
        # Se cierra la conexión a la base de datos
        newConnection.closeConnection()

    """
    Función que permite visualizar los mejores puntajes.
    """
    def __bestScores(self):
        
        #Un usuario visualiza la tabla de puntuaciones
        (ToolConnection()).bestScore()
        
        self.parent.withdraw()
        # Se hace el llamado a la ventana de Score
        SudokuScoreboardUI(parent=self.parent)

    """
    Función que pregunta al usuario si desea salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 3.0
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

    """
    Función que asigna los valores de inicio de sesión del usuario 
    logeado (id, username)
    """        
    def getUsernameLogin(self):
        # Retorna la información de id, nombre de usuario y rol del usuario loggeado
        self.idUsername, self.username, self.rol = (ToolConnection()).getLastLoginUser()
