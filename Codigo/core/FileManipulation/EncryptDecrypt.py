# -*- coding: utf-8 -*-

"""
Se utilizan las funciones built-in de MySQL para realizar una encriptación 
del flujo de bytes de los arhichivos .sudoku.
Devuelve una cadena con los elementos encriptados o desencriptados.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class EncryptDecryptSudokuFile: 

    def __init__(self, engine): 
        self.engine = engine

    
    def processQuery(self, aesOperation: str) -> str:
        
        query = "SELECT {};".format( aesOperation )
        return query

    
    def processSelect(self, result: list) -> str: 
        try:
            return result[0][0]
        except IndexError as e: 
            pass

    """
        Procesa la función built-in de MySQL (AES_ENCRYPT), encriptando la información 
        enviada vía el parámetro @binarydata
    """    
    def encrypt(self, binarydata: str, password: str) -> str:
        
        encrypt = "HEX(AES_ENCRYPT(%s, %s))"
        data = (binarydata, password, )
        query = self.processQuery(encrypt)
        select = self.engine.select( query, data )

        return self.processSelect(select)
        
        
    """
        Procesa la función built-in de MySQL (AES_DECRYPT), haciendo el proceso inverso a encriptar
        dicha información enviada vía el parámetro @encrypData
    """
    def decrypt(self, encryptData: str, password: str) -> str:
        
        decrypt = "AES_DECRYPT(UNHEX(%s),%s)"
        data = (encryptData, password, )
        query = self.processQuery(decrypt)
        select = self.engine.select( query, data )
        
        return self.processSelect(select)