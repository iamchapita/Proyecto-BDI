# -*- coding: utf-8 -*-

"""
    @author: kenneth.cruz@unah.hn
    @version: 0.1.7
    @date: 2021/04/08
"""

from datetime import time
from random import randint
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.FileManipulation.EncryptDecrypt import EncryptDecryptSudokuFile

class ToolConnection: 

    def __init__(self):
        self.config = ConfigConnection() #Conexión al archivo de configuración
        self.db = MySQLEngine(self.config.getConfig()) #Conexión a la base de datos
        self.encryptDecrypt = EncryptDecryptSudokuFile( self.db ) #Encripta y desencripta los datos del tablero


    """ 
        Obtiene el nombre del usuario que inició sesión
    """
    #def getUsernameLogin(self): 
    def getLastLoginUser(self)-> tuple: 
    
        query = "SELECT * FROM vw_GetLastLoginUser;"

        transaction = self.db.select(query=query)

        self.username = transaction[0][0]
        self.idUsername = transaction[0][1]
        self.rol = transaction[0][2]
        print(  "username: {}, id: {}, rol:{}".format(self.username, self.idUsername, self.rol) )
        #self.db.closeConnection()

        #(id, name)
        #return (transaction[0][0], transaction[0][1], transaction[0][2])
        return (self.username, self.idUsername, self.rol)


    """
        Crea una partida dentro del Board
        @param: idUsername, idBoard, cod_state, time, stack
    """
    def insertGameBoard(self, username: str, idUsername: int, idBoard: int, state=1, time="00:00:00", stack=[]) -> None:
        
        self.db.insert(
                table="Game", 
                fields=[
                            "id_user_fk",
                            "id_sudokuboard_fk", 
                            "blo_file", 
                            "tim_time"
                        ], 
                values=[
                            idUsername, 
                            idBoard, 
                            self.encryptDecrypt.encrypt(binarydata="{}".format(stack), password=username), 
                            time
                ]
            )
        
        self.updateState(idUsername=idUsername, state=state)
        
        #self.db.closeConnection()


    """
        Actualiza el estado y las jugadas de la partida que está jugando un usuario en el Board
    """
    def updateGameBoard(self, username: str, idUsername: int, idBoard: int, state: int, time: str, stack: list) -> None:
        
        self.db.update(
                table="Game", 
                fields=[
                            "blo_file", 
                            "tim_time"
                        ], 
                values=[
                            "'{}'".format( self.encryptDecrypt.encrypt(binarydata="{}".format(stack), password=username) ), 
                            "'{}'".format( time )
                ],
                condition="""
                            WHERE 
                                id_sudokuboard_fk = {} 
                            """.format( idBoard )
                )
                
        self.updateState(idUsername=idUsername, state=state)

    """
        Actualiza el estado del tablero que se encuentra en juego
    """
    def updateState(self, idUsername: int, state: int) -> None:
        
        #Obtiene el id del último juego jugado (y almacenado) del usuario que inició sesión
        query = """
                    SELECT 
                        id
                    FROM 
                        Game 
                    WHERE 
                        id_user_fk={} 
                    ORDER BY 
                        tim_date DESC
                    LIMIT 1
                    ;
                """.format( idUsername )

        #Estado de la partida:  1 nuevo, 2 pausado, 3 finalizado, 4 derrota, 5 continuar
        self.db.insert(
                table="State", 
                fields=[
                            "id_game_fk",
                            "cod_state"
                        ], 
                values=[
                            self.db.select(query=query)[0][0], 
                            state
                        ]
            )
        

    """
        Registra la salida de un usuario del sistema
    """
    def logout(self) -> None:
        id, username, rol = self.getLastLoginUser()

        self.db.insert(
                        table="LogOff", 
                        fields=["id_user_fk"], 
                        values=[id]
                    )
        
        #self.db.closeConnection()


    """
        Obtiene el id del Board que está en juego
    """
    def getIdBoard(self, idUsername: str) -> int: 
        
        query = """
                SELECT 
                    id_sudokuboard_fk
                FROM 
                    Game 
                WHERE 
                    id_user_fk=%s
                ORDER BY 
                    tim_date DESC
                LIMIT 1;
                """
        id = self.db.select(query=query, data=( idUsername, ))
        return id[0][0]


    """
        Formato hh:mm:ss
    """
    def formatTime(self, hour: int, minute: int, second: int) -> str: 
        dt = time(
                        hour=hour, 
                        minute=minute, 
                        second=second, 
                        microsecond=0
                    )

        return dt.isoformat(timespec="auto")


    """
        Se escribe un nuevo tablero dentro del archivo .sudoku
        @idBoard es una bandera que indica a la función sí se debe elegir un Board al azar
    """
    def processFile(self, filename: str, idBoard=0) -> int: 
        
        query = "SELECT id, tex_board FROM SudokuBoard WHERE id=6"
        
        #Obtiene la información de todos los boards (tableros iniciales) cargados en la entidad SudokuBoard
        sudokuBoard = self.db.select(query=query)

        boardFile = open('core/sudoku/{}'.format(filename), 'w')
        #Borra la información contenida en el documento
        boardFile.truncate()

        board = None

        if sudokuBoard:     
            
            #tablero al azar
            if not idBoard: 
            
                index = randint(0, len(sudokuBoard)-1)

                #Se selecciona un board al azar
                board = sudokuBoard[index][1]

                idBoard = sudokuBoard[index][0]

            else: 
                
                #Obtiene el tablero guardado en la bd, para el juego que está en el estado 'pausa'
                
                for i in range( len(sudokuBoard) ): 

                    if idBoard in sudokuBoard[i]:

                        board = sudokuBoard[i][1]

            #Escribe el nuevo tablero en el documento .sudoku
            boardFile.write( board )

        boardFile.close()

        return idBoard

    """
        Acción de visualizar la mejor puntuación 
    """
    def bestScore(self):
        
        username, idUsername, rol = self.getLastLoginUser()

        self.db.insert(
                table="Binacle", 
                fields=[
                            "tex_nickname",
                            "tex_description" 
                        ], 
                values=[
                            username, 
                            "el usuario # ha visualizado la tabla de puntuaciones"
                        ]
            )