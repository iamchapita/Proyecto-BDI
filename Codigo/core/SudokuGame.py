# -*- coding: utf-8 -*-
from core.SudokuBoard import SudokuBoard

"""
Contiene métodos para cargar y comprobar el estado del tablero
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuGame(object):

    # Constructor de la clase
    def __init__(self, boardFile):
        self.boardFile = boardFile
        # Se obtiene el tablero en forma de list
        self.startPuzzle = SudokuBoard(boardFile).board
        # Se establecen banderas para indicar el estado del tablero
        self.gameOver = False
        self.pause = False

    # Define el estado inicial del tablero
    def start(self):
        self.puzzle = []

        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append(self.startPuzzle[i][j])
    
    # Corrobora que el tablero este lleno de forma correcta
    def checkWin(self):
        
        for row in range(9):
            if (not self.__checkRow(row)):
                return False

        for column in range(9):
            if (not self.__checkColumn(column)):
                return False
        
        for row in range(3):
            for column in range(3):
                if (not self.__checkSquare(row, column)):
                    return False

        # Se establece la variable a True señalando que el juego acabo y se ganó
        self.gameOver = True
        return True

    # Corrobora que cada bloque del tablero este lleno correctamente
    def __checkBlock(self, block):
        # Set es usada para guardar múltiples objetos de una variabe
        return set(block) == set(range(1, 10))
    
    # Corrobora que la fila esté llena correctamente
    def __checkRow(self, row):
        return self.__checkBlock(self.puzzle[row])

    # Corrobora que la columna esté llena correctamente
    def __checkColumn(self, column):
        return self.__checkBlock(
            [self.puzzle[row][column] for row in range(9)]
            )
    
    # Corrobora que cada cuadrado del tablero esté lleno correctamente
    def __checkSquare(self, row, column):
        return self.__checkBlock(
            [
                self.puzzle[r][c]
                for r in range(row * 3, (row + 1) * 3)
                for c in range(column * 3, (column +1) * 3)
            ]
        )
