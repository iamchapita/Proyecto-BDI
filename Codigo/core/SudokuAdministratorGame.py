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
class SudokuAdministratorGame(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    """
    def __init__(self, parent):
        # Instancia de la ventana padre.
        self.parent = parent
        self.child = Tk()
        # Se captura el evento de cierre de una ventana y se ejecuta la función __onClosing.
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.config = ConfigConnection() #Conexión al archivo de configuración        
        self.db = MySQLEngine( self.config.getConfig() ) #Conexión a la base de datos
        self.idBoard = None #Numero del board seleccionado
        super().__init__(self.child)

        # Creación de variables globales
        self.username = ""
        self.idUsername = None

        # Instancia para obtener el nombre de usuario log
        self.getUsernameLogin()   

        self.__initUI()
        self.master.mainloop()     

    """
    Creación de los widgets que se verán en pantalla.
    """
    def __initUI(self):
        # Se cargan las imagenes que use usarán en la ventana
        self.img = PhotoImage(file="core/images/back.png", master=self.child)
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        # Se crea el botón, sus características y su imagen para la la funcionalidad de regresar a la ventana anterior. 
        self.backButton= Button(self.child, image=self.img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        self.backButton.grid(row=0,column=1,sticky = "nsew", pady=10)
        # Se definen los valores de ancho y alto para la ventana
        self.width = 400
        self.height = 600
        # Se establece las dimensiones de la ventana
        self.child.geometry("%dx%d" % (self.width, self.height))
        # Se establece el titulo de la ventana
        self.child.title('Menú')
        # Se asigna la imagen para el ícono de la ventana
        self.child.iconphoto(True, self.icon)
        # Se establece el color de background de la ventana
        self.child.configure(background = "#171717")
        self.child.resizable(False, False)
        # Se centra la ventana en pantalla
        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)
        # Se define un label para mostrar el titulo de la ventana, se define la fuente a utilizar
        label1= Label(self.child, text='¿Qué deseas hacer?', font=("lato", 20))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 60, padx=70)
        # Se crean los botones y características de los botones
        Button(self.child, text = 'Nuevo juego', bg="#6ea8d9", font=("lato", 17), command= self.__newGame).grid(row=2,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=37)
        Button(self.child, text = 'Continuar juego', bg="#6ea8d9", font=("lato", 17), command= self.__continueGame).grid(row=3,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=18)
        Button(self.child, text = 'Mejores puntajes', bg="#6ea8d9", font=("lato", 17), command= self.__bestScores).grid(row=4,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=11)
        # Se establece un label como contenedor de la imagen de la marca del juego.
        label2 = Label(self.child, image=self.brand, borderwidth=0)
        label2.grid(row=6,column=1,pady = 150)

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
                    tool = ToolConnection()
                    filename = "n00b.sudoku"
                    # Se inserta el board en la bd
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
            self.child.withdraw()
            game = SudokuGame(boardFile)
            game.start()
            root = Tk()
            # Sí hay un tiempo entonces se envía en forma de parámetros a la clase board 
            if(time):
                SudokuBoardUI(root, game, self.child,  "", time[0], time[1], time[2])
            # Si no hay entonces se establece el tiempo por defecto
            else:
                SudokuBoardUI(root, game, self.child,  "")

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
                # Si no hay partidas en pausa, se muestra un mensaje indicándolo.
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

        self.child.withdraw()
        # Se hace el llamado a la ventana de Score
        SudokuScoreboardUI(parent=self.child)

    """
    Función que pregunta al usuario si desea salir del juego.
    """
    def __onClosing(self):
        # Confirmación sobre cerrado de la aplicación
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            sys.exit()
            # Se destruye la ventana actual
            self.child.destroy()
            # Se cierra la conexión a la base de datos
            self.db.closeConnection()
            # Se muestra la ventana de despedida
            SudokuBye()

        else:
            pass

    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()

    """
    Función que asigna los valores de inicio de sesión del usuario 
    logeado (id, username)
    """        
    def getUsernameLogin(self):
        # Retorna la información de id, nombre de usuario y rol del usuario loggeado
        self.idUsername, self.username, self.rol = (ToolConnection()).getLastLoginUser()
