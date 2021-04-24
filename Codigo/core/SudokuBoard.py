# -*- coding: utf-8 -*-
"""
Se encarga de cargar el archivo de tablero a un arreglo para poner manipularlo
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuBoard(object):

    # Constructor de la clase
    def __init__(self, boardFile):
        """ 
        Se define el contenido del objeto con el constructor como 
        una funcion que simula ser del tipo privado.
        """
        self.board = self.__createBoard(boardFile)
    
    # Se define la función que va a cargar el tablero.
    #  En la versión original se carga desde un archivo, en este 
    # caso se va a cargar desde la BD.
    def __createBoard(self, boardFile):
        board = []

        for line in boardFile:
            # Quita los espacios en blanco al principio y al final
            # de la linea
            line = line.strip()

            # Agrega un list vacío
            board.append([])

            # Comprueba que las lineas esten compuestas solamente de números
            for char in line:
                if (not char.isdigit()):
                    raise SudokuError("Los únicos caracteres válidos son números")
                board[-1].append(int(char))
                
        # retorna el resultado
        return board
