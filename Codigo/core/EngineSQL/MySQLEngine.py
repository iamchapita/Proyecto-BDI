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
    
    #Realiza inserción  de datos en la base de datos; los pasando como parámetros el nombre de la base de datos
    # los campos en un arreglo al igual que los valores de la tupla 
    def insert(self, table, fields=[], values=[]): 

        query = "INSERT INTO {} ({}) VALUES ({});".format( table, ", ".join(fields), self.prepareQuery(values) )

        print( query )

        self.link.execute(query)
        self.mydb.commit()

    def selectPage(self, query, page=0, count=10): 

        # Limpiar la query y remover el LIMIT que exista
        query = re.sub(r"\s+[Ll][Ii][Mm][Ii][Tt]\s+\d+([, ]\d+)?\s*;\s*", "", query)

        # Crear nuesto propio componente LIMIT usando los parámetros
        query = ("{} LIMIT {},{};".format(query, page, count))

        self.link.execute(query)
        return self.link.fetchall()
    
    # Esta función será borrada y en su sular se usaŕa executeFunction
    def getUserStatus(self, username: str, password) -> list:
        query = "SELECT fn_compareData('{}', '{}');".format(username, password)
        self.link.execute(query)
        return self.link.fetchone()

    # Ejecuta una función SQL.
    # Recibe como parámetros el nombre de la función de SQL y un arreglo donde se 
    # espera se introduzcan los parametros de dicha función
    def executeFunction(self, functionName, parameters):

        query = "SELECT {}".format(functionName)

        if (parameters):
            query += "("
            for value in parameters:
                query += "'{}', ".format(value)
            
            query = re.sub(r",\s$", ");", query)

        else:
            query += "();"

        print(query)

        self.link.execute(query)
        return self.link.fetchone()
    

    def callProc(self, name, args):
        self.link.execute("CALL {}({},{})".format(name, args[0], args[1]))
        self.mydb.commit()
    
    # Ejecuta una instrucción SQL de Actualización
    # Recibe como parámetros:
    # - El nombre de la tabla a actualizar
    # - Los campos a actualizar
    # - Los valores de los campos a actualizar
    # - Una condición WHERE(SQL)
    def update(self, table, fields, values, condition = None):
        
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
        
        print( "UPDATE: {}".format(query) )

        self.link.execute(query)
        self.mydb.commit()


    #Cierra la conexión establecida a la base de datos
    def closeConnection(self):
        self.mydb.close()


    #Agrega comillas para los n valores de los campos de un query
    def prepareQuery(self, values):
        
        data = ""
        
        print( values )

        for value in values: 

            #Evita colocar comillas simples a los tipo de dato entero
            if type(value) == int:  
                data += "{}, ".format(value)
            else: 
                data += "'{}', ".format(value)
        
        print( data )
        data = re.sub(r",\s+?$", "", data)
        print( data )
        
        return data