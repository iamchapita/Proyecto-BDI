# -*- coding: utf-8 -*-

import base64
import os
import sys

"""
Manipula el flujo de bits de un arhivo .sudoku
Transforma un flujo de bits en un archivo .sudoku
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class BlobManipulation: 
    
    def __init__(self, filename): 
        
        # Directorio del archivo .sudoku
        self.path = (os.getcwd()).replace(os.getcwd().split("/").pop(), "sudoku")

        # Nombre de los archivos .sudoku
        self.filename = filename.strip()

    # .sudoku a Blob
    def convertToBinaryData(self):
        
        try: 
            # Convert digital data to binary format
            with open(self.filename, 'rb') as file:
                binaryData = base64.b64encode( file.read() )

            return binaryData

        except OSError as e: 
            pass

        except:
            pass
            
    # Blob a .sudoku
    def convertToSudokuFile(self, binarydata): 
        
        self.filename = ("{}{}".format(self.filename, ".sudoku"))

        with open(self.filename, 'wb') as file: 
            file.write( base64.b64decode(binarydata) )
