# -*- coding: utf-8 -*-
import re

import mysql.connector

"""
Clase que engloba funciones para realizar operaciones sobre la base de datos
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class MySQLEngine: 

    def __init__(self, config: dict):
        
        # Se genera la conexión con la base de datos
        # @param: config es una instancia de dict que contiene los parámetros necesarios para realizar 
        # la conexión a la base de datos
        self.mydb = mysql.connector.connect(**config)
        print("Conexión con éxito: {}".format( self.mydb.is_connected() ))
        # Se obtiene el cursor 
        self.link = self.mydb.cursor()
    
    # Función que encapsula la operación de select 
    def select(self, query: str, data=()): 

        try:         
            # Se comprueba si se recibió un parámetro data
            if len(data):
                self.link.execute(query, data)
            else: 
                self.link.execute(query)

            # Retorna los elementos que se obtuvieron al hacer la operación de select
            return self.link.fetchall()

        except mysql.connector.Error as e:
            print("Problemas de conexón: {}".format(e))                
    
    # Realiza la operación de insert en la base de datos
    def insert(self, table: str, fields=[], values=[]): 

        # Se prepara la query a realizar
        query = "INSERT INTO {} ({}) VALUES ({});".format( table, ", ".join(fields), self.prepareQuery(values) )

        print( query )

        # Se ejecuta la query
        self.link.execute(query)
        # Se hacen permanentes los cambios en la Base de datos
        self.mydb.commit()

    # Utilizada para realizar consultas select con LIMIT
    def selectPage(self, query: str, page=0, count=10): 

        # Limpiar la query y remover el LIMIT que exista
        query = re.sub(r"\s+[Ll][Ii][Mm][Ii][Tt]\s+\d+([, ]\d+)?\s*;\s*", "", query)

        # Crear nuesto propio componente LIMIT usando los parámetros
        query = ("{} LIMIT {},{};".format(query, page, count))

        # Ejecuta la query
        self.link.execute(query)
        # Se retorna todos los resultados obtenidos al ejecutar la query
        return self.link.fetchall()
    
    # Ejecuta la función fn_compareData, que es una función SQL
    def getUserStatus(self, username: str, password: str) -> list:

        # Se prepara la query
        query = "SELECT fn_compareData('{}', '{}');".format(username, password)
        # Se ejecuta la query
        self.link.execute(query)
        # Se retorna el resultado obtenido
        return self.link.fetchone()

    # Sujeto a borrado
    """ def executeFunction(self, functionName: str, parameters: list):

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
    
    """
    # Utilizada para ejecutar un Procedimiento Almacenado en la base de datos
    def callProc(self, name: str, args: list):
        # Se ejecuta el llamado del Procedimiento Almacenado
        self.link.execute("CALL {}({},{})".format(name, args[0], args[1]))
        # Se hacen permanentes los cambios en la base de datos
        self.mydb.commit()
    

    # Ejecuta una operación Update en la base de datos
    def update(self, table: str, fields: list, values: list, condition = None):
        
        # Se prepara la query
        query = "UPDATE {} SET ".format(table)

        # Se comprueba que los campos (fields) y los valores (values) tengan el mismo número de elementos
        if (len(fields) == len(values)):
            # Se recorren los list y se agregan en la query
            for (field, value) in zip(fields, values):
                query += "{} = {}, ".format(field, value)

            # Se elimina la ultima coma agregada por el ciclo
            query = re.sub(r"(,)(\s)*$", " ", query)

            # Se prepara la condición para agregarla a la query
            condition = re.sub(r"(\s)*([Ww][Hh][Ee][Rr][Ee])+(\s)*", " ", condition)
            query += "WHERE {} ".format(condition)
            # Se eliminan puntos y comas y espacios innecesarios de la query
            query = re.sub(r"(\s)*(;)?(\s)*$", "", query)
            # Se agrega punto y coma al final de la query
            query += ";"

        else:
            raise Exception("fields and values should has same len()")
        
        print( "UPDATE: {}".format(query) )

        # Se ejecuta la query
        self.link.execute(query)
        # Se hacen permanentes los cambios en la base de datos
        self.mydb.commit()

    #Cierra la conexión establecida a la base de datos
    def closeConnection(self):
        self.mydb.close()

    #Agrega comillas para los n valores de los campos de un query
    def prepareQuery(self, values: list):
        
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
        
        # Retorna el valor en forma de cadena
        return data
