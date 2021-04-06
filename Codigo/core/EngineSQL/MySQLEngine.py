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
        query = "SELECT fn_compareData('{}', '{}');".format(username, password)
        self.link.execute(query)
        return self.link.fetchone()

    def update(self, table, fields=(), values=(), condition = None):
    
        query = "UPDATE {} SET ".format(table)

        if (len(fields) == len(values)):
            for (field, value) in zip(fields, values):
                query += "{} = {}, ".format(field, value)

            query = re.sub(r"(,)(\s)*$", " ", query)
            condition = re.sub(r"(\s)*([Ww][Hh][Ee][Rr][Ee])+(\s)*", " ", condition)
            query += "WHERE {} ".format(condition)
            query = re.sub(r"(\s)*(;)?(\s)*$", "", query)
            query += ";" 

        else:
            raise Exception("fields and values should has same len()")
        
        print(query)   
        self.link.execute(query)
        self.mydb.commit()

    def delete(self, table, tex_nickname): 
        
        query = "DELETE FROM %s WHERE tex_nickname = %s"
        self.link.execute(query, tex_nickname)
        self.mydb.commit()

    def closeConnection():
        self.mydb.close()