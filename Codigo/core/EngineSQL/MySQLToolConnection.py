# -*- coding: utf-8 -*-
from datetime import time
from random import randint

from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.FileManipulation.EncryptDecrypt import EncryptDecryptSudokuFile

"""
Clase que engloba funciones utilizadas en distintos escenarios
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class ToolConnection: 

    def __init__(self):
        # Conexión al archivo de configuración
        self.config = ConfigConnection() 
        # Conexión a la base de datos
        self.db = MySQLEngine(self.config.getConfig()) 
        # Encripta y desencripta los datos del tablero
        self.encryptDecrypt = EncryptDecryptSudokuFile( self.db ) 

    # Obtiene el nombre del último usuario que inició sesión, retorna una tupla
    def getLastLoginUser(self)-> tuple: 
        
        # Se establece la consulta
        query = "SELECT * FROM vw_GetLastLoginUser;"

        # Se utiliza el método select, encapsulado en la clase MySQLEngine, para hacer la operación select
        transaction = self.db.select(query=query)

        # Se comprueba si la transacción contiene resultados
        if transaction:
            
            # Se generan variables individuales a partir del resultado de la operación select
            self.username = transaction[0][0]
            self.idUsername = transaction[0][1]
            self.rol = transaction[0][2]

            # Se retorna los resultados obtenidos en la operación select
            return (self.username, self.idUsername, self.rol)

    
    # Inserta un registro en la tabla Game
    # Parámetros:
    # - username: Nombre de usuario
    # - idUsername: id del usuario
    # - idBoard: id del tablero
    # - state: Estado del tablero
    # - time: Tiempo transcurrido durante la partida
    def insertGameBoard(self, username: str, idUsername: int, idBoard: int, state=1, time="00:00:00", stack=[]) -> None:
        
        # Se inserta en la tabla Game usando la función select de la clase MySQLEngine
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
    
    # Actualiza el estado y las jugadas de la partida que está jugando un usuario en el Board
    def updateGameBoard(self, username: str, idUsername: int, idBoard: int, state: int, time: str, stack: list) -> None:
        
        # Se realiza la operación de update en la base de datos
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

    # Actualiza el estado del tablero que se encuentra en juego
    def updateState(self, idUsername: int, state: int) -> None:
        
        # Obtiene el id del último juego jugado (y almacenado) del usuario que inició sesión
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

        # Estado de la partida:  1 nuevo, 2 pausado, 3 finalizado, 4 derrota, 5 continuar
        # Realiza la operación de inserción en la base de datos
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
        
    # Registra la salida de un usuario del sistema
    # Inserta en la tabla LogOff cada vez que se cierra el programa y hay un jugador con sesión iniciada
    def logout(self) -> None:

        # Se obtiene la información del último usuario que inició sesión 
        id, username, rol = self.getLastLoginUser()

        # Se inserta en la Base de datos esta información, en la tabla LogOff
        self.db.insert(
                        table="LogOff", 
                        fields=["id_user_fk"], 
                        values=[id]
                    )

    # Obtiene el id del Board que está en juego
    def getIdBoard(self, idUsername: str) -> int: 
        
        # Texto de la consulta que se va a realizar a la base de datos
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

        # Se retorna el resultado obtenido de la consulta select
        return id[0][0]


    # Establece el formato de tiempo a los valores pasados por parámetro
    # Formato hh:mm:ss
    def formatTime(self, hour: int, minute: int, second: int) -> str: 
        dt = time(
                        hour=hour, 
                        minute=minute, 
                        second=second, 
                        microsecond=0
                    )

        # Retorna el resultado de la operación
        return dt.isoformat(timespec="auto")

    # Se escribe un nuevo tablero dentro del archivo .sudoku
    # @idBoard es una bandera que indica a la función sí se debe elegir un Board al azar
    def processFile(self, filename: str, idBoard=0) -> int: 
        
        # Obtiene los tableros desde la base datos
        query = "SELECT id, tex_board FROM SudokuBoard"
        
        # Obtiene la información de todos los boards (tableros iniciales) cargados en la entidad SudokuBoard
        sudokuBoard = self.db.select(query=query)

        # Abre el flujo de datos sobre el archivo
        boardFile = open('core/sudoku/{}'.format(filename), 'w')

        # Borra la información contenida en el documento
        boardFile.truncate()

        board = None

        # Comprueba si la consulta devolvió resultados
        if sudokuBoard:     
            
            # Tablero al azar
            if not idBoard: 
            
                index = randint(0, len(sudokuBoard)-1)

                #Se selecciona un board al azar
                board = sudokuBoard[index][1]

                idBoard = sudokuBoard[index][0]

            else: 
                
                # Obtiene el tablero guardado en la bd, para el juego que está en el estado 'pausa'
                for i in range( len(sudokuBoard) ): 
                    if idBoard in sudokuBoard[i]:
                        board = sudokuBoard[i][1]

            # Escribe el nuevo tablero en el documento .sudoku
            boardFile.write( board )

        # Cierra el flujo de datos hacia el archivo
        boardFile.close()

        # Retorna el id del Board que se va a utilizar
        return idBoard

    
    # Acción de visualizar la mejor puntuación 
    # Registra en la base de datos(Binacle) cada vez que un usuario presione el botón para ver los mejores resultados
    def bestScore(self):
        
        # Obtiene los datos del ultimo usuario que ingreso al programa
        id, username, rol = self.getLastLoginUser()

        # Realiza la inserción en la base de datos
        self.db.insert(
                table="Binacle", 
                fields=[
                            "tex_nickname",
                            "tex_description" 
                        ], 
                values=[
                            username, 
                            "El usuario visualizó la tabla de puntuaciones"
                        ]
            )
    
    # Inserción de registros en la tabla Binacle
    def insertBinacle(self, nickname, description): 

            self.db.insert(
                "Binacle", 
                [
                    "tex_nickname", 
                    "tex_description"
                ], 
                [
                    nickname, 
                    description
                ]
            )
