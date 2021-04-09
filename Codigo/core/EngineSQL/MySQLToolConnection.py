# -*- coding: utf-8 -*-

"""
    @author: kenneth.cruz@unah.hn
    @version: 0.1.0
    @date: 2021/04/08
"""

from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection

class ToolConnection: 

    def __init__(self):
        self.config = ConfigConnection() #Conexión al archivo de configuración
        self.db = MySQLEngine(self.config.getConfig()) #Conexión a la base de datos


    """ 
        Obtiene el nombre del usuario que inició sesión
    """
    #def getUsernameLogin(self): 
    def getLastLoginUser(self): 
    
        query = "SELECT * FROM GetLastLoginUser;"

        transaction = self.db.select(query=query)

        self.username = transaction[0][0]
        self.idUsername = transaction[0][1]

        print(  "username: {}, id: {}".format(self.username, self.idUsername) )

        self.db.closeConnection()

        #(id, name)
        return (transaction[0][0], transaction[0][1])


    """
        Creación de una partida dentro del Board
        @param: idUsername, idBoard, cod_state, time, stack
    """
    def insertGameBoard(self, idUsername, idBoard, state=1, time="00:00:00", stack=[]):
        
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
                            "{}".format( stack ), 
                            time
                ]
            )
            
        query = """
                    SELECT 
                        id
                    FROM 
                        Game 
                    WHERE 
                        id_user_fk={} AND tim_time='00:00:00'
                    ORDER BY 
                        tim_date DESC
                    LIMIT 1
                    ;
                """.format( idUsername )

        #Estado de la partida:  1 nuevo, 2 pausado, 3 finalizado, 4 derrota 
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
        
        self.db.closeConnection()