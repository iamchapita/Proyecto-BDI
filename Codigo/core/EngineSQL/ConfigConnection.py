# -*- coding: utf-8 -*-

"""
    @author: kenneth.cruz@unah.hn
    @author: lamorales@unah.hn
    @version: 0.1.1
    @date: 2021/04/01
"""

import configparser
import re
import os 

"""
    Obtiene y parsea los datos del archivo de configuración 
    en una estructura de tipo diccionario
"""
class ConfigConnection: 

    def __init__(self): 
        try: 
            #Ruta del archivo de configuración
            #self.path = ( "{}/config.ini".format(os.getcwd()) )
            self.path = re.sub(r"(Codigo)", "Scripts de Base de Datos/config.ini", os.getcwd())
            #Instancia del objeto configparser
            self.parser = configparser.ConfigParser()
            #Lectura el archivo config.ini
            self.parser.read(self.path)

        except os.error as e:
            print("El archivo no existe: {}".format( e ))
        
    #Toma los valores del archivo de configuración; retorna un diccionario
    def getConfig(self): 
        
        #Sección por defecto dentro del archivo de configuración (config.ini)
        config = self.parser["DEFAULT"]
        
        #Configuración de la conexión a la base de datos
        config = dict(zip(config.keys(), config.values()))

        #CHAR, VARCHAR y TEXT se devuelven como cadenas Unicode,
        #config['use_unicode'] = True
        
        #Habilita (o deshabilita) advertencias para que estas generen excepciones de existir error
        #config['raise_on_warnings'] = True

        #Las filas se obtienen inmediatamente después de ejecutar la consulta; de lo contrario, las filas se obtienen a pedido. Por defecto es Falso
        #config['buffered'] = True

        #Los resultados de MySQL se devuelven tal cual, en lugar de convertirse a tipos de Python. 
        #config['raw'] = True

        return config