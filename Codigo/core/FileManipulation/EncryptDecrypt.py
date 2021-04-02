# -*- coding: utf-8 -*-

"""
    @author: kenneth.cruz@unah.hn
    @version: 0.1.0
    @date: 2021/04/01
"""

"""
    Se utilizan las funciones built-in de MySQL para realizar una encriptación 
    del flujo de bytes de los arhichivos .sudoku.
    Devuelve una cadena con los elementos encriptados o desencriptados.
"""


class EncryptDecryptSudokuFile: 

    def __init__(self, engine): 
        self.engine = engine

    
    def processQuery(self, aesOperation):
        
        query = "SELECT {};".format( aesOperation )
        return query

    
    def processSelect(self, result): 
        try:
            return result[0][0]
        except IndexError as e: 
            print("índice fuera de rango: {}".format(e))

    
    def encrypt(self, binarydata, password):
        
        encrypt = "HEX(AES_ENCRYPT(%s, %s))"
        data = (binarydata, password, )
        query = self.processQuery(encrypt)
        select = self.engine.select( query, data )

        return self.processSelect(select)
        
        

    def decrypt(self, encryptData, password):
        
        decrypt = "AES_DECRYPT(UNHEX(%s),%s)"
        data = (encryptData, password, )
        query = self.processQuery(decrypt)

        print( "CONSULTA: {}".format(query) )

        select = self.engine.select( query, data )

        return self.processSelect(select)