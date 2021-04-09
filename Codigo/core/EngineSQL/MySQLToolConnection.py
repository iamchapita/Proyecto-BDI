# -*- coding: utf-8 -*-

"""
    @author: kenneth.cruz@unah.hn
    @version: 0.1.0
    @date: 2021/04/08
"""

from MySQLEngine import MySQLEngine
from ConfigConnection import ConfigConnection

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