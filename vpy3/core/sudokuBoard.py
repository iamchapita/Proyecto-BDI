from core.sudokuError import SudokuError
#from sudokuError import SudokuError

class SudokuBoard(object):

    # Constructor de la clase
    def __init__(self, boardFile):
        """ 
        Se define el contenido del objeto con el constructor como 
        una funcion que simula ser del tipo privado.
        """
        self.board = self.__createBoard(boardFile)
    
    """ 
    Se define la función que va a cargar el tablero, posiblemente los 
    números que van en cada casilla del tablero. En la versión 
    original se carga desde un archivo, en este caso se va a cargar desde la BD.
    """
    def __createBoard(self, boardFile):
        board = []

        for line in boardFile:
            # Quita los espacios en blanco al principio y al final
            # de la linea
            line = line.strip()

            """ if (len(line) != 9):
                raise SudokuError ("Error que posiblemente no se presente")
            """

            board.append([])

            for char in line:
                if (not char.isdigit()):
                    raise SudokuError("Los únicos caracteres válidos son números")
                board[-1].append(int(char))

        if (len(board) != 9):
            raise SudokuBoard("Cada tablero de sudoku debe tener 9 lineas largo")

        return board



""" with open('vpy3/n00b.sudoku', 'r') as boardFile:

    obj = SudokuBoard(boardFile)
    
    for i in range(9):
        print(obj.board[i])
"""