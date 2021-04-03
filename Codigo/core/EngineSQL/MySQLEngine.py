# -*- coding: utf-8 -*-

"""
    @author: kenneth.cruz@unah.hn
    @version: 0.1.0
    @date: 2021/04/01
"""

import mysql.connector
import re

class MySQLEngine: 

    def __init__(self, config):

        self.mydb = mysql.connector.connect(**config)
        print("Conexión con éxito: {}".format( self.mydb.is_connected() ))
        self.link = self.mydb.cursor()
        

    def select(self, query, data=()): 
        try:         
            if len(data):
                self.link.execute(query, data)
            else: 
                self.link.execute(query)

            return self.link.fetchall()

        except mysql.connector.Error as e:
            print("Problemas de conexón: {}".format(e))                
        else:
            self.mydb.close()


    def insert(self, query, data): 

        self.link.execute(query, data)
        self.mydb.commit()

    def selectPage(self, query, page=0, count=10): 

        # Limpiar la query y remover el LIMIT que exista
        query = re.sub(r"\s+[Ll][Ii][Mm][Ii][Tt]\s+\d+([, ]\d+)?\s*;\s*", "", query)

        # Crear nuesto propio componente LIMIT usando los parámetros
        query = ("{} LIMIT {},{};".format(query, page, count))

        self.link.execute(query)
        return self.link.fetchall()
    
    def getUserStatus(self, username, password):
        query = """
            SELECT
                (
                    SELECT
                        fn_compareData('{}', '{}')
                ) AS Status,
                IF(bit_rol = 1, 1, 0) AS Rol
            FROM
                User
            WHERE 
                tex_nickname = '{}';
        """.format(username, password, username)
        self.link.execute(query)
        # Se utiliza fetchone porque solo se obtendra una tupla
        # Si la consulta no encuenta el usuario entonces no devuelve nada
        # Para evitar que retorne Nulo o None se emplea el if
        return self.link.fetchall()

    def closeConnection():
        self.mydb.close()