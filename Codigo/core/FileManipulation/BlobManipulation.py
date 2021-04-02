# -*- coding: utf-8 -*-

"""
    @author: kenneth.cruz@unah.hn
    @version: 0.1.0
    @date: 2021/04/01
"""

import os 
import sys
import base64

"""
    Manipula el flujo de bits de un arhivo .sudoku
    Transforma un flujo de bits en un archivo .sudoku
"""

class BlobManipulation: 
    
    def __init__(self, filename): 
        
        # Directorio del archivo .sudoku
        self.path = (os.getcwd()).replace(os.getcwd().split("/").pop(), "sudoku")

        # Nombre de los archivos .sudoku
        self.filename = filename.strip()

        """
        self.filename =  [ 
                    file
                    for root, dirs, files in os.walk( self.path ) 
                    for file in files 
                    if ".sudoku" in file
                ] 
        """
        
    # .sudoku a Blob
    def convertToBinaryData(self):
        
        try: 
            # Convert digital data to binary format
            with open(self.filename, 'rb') as file:
                binaryData = base64.b64encode( file.read() )

            return binaryData

        except OSError as e: 
            print("No se ha encontrado archivo: {}".format(e))

        except:
            print("Ni idea uwu:", sys.exc_info()[0])
            
    
    # Blob a .sudoku
    def convertToSudokuFile(self, binarydata): 
        
        self.filename = ("{}{}".format(self.filename, ".sudoku"))

        with open(self.filename, 'wb') as file: 
            file.write( base64.b64decode(binarydata) )
