from core.sudokuBoard import SudokuBoard
#from sudokuBoard import SudokuBoard

class SudokuGame(object):

    def __init__(self, boardFile):
        self.boardFile = boardFile
        self.startPuzzle = SudokuBoard(boardFile).board

    def start(self):
        self.gameOver = False
        self.puzzle = []

        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append(self.startPuzzle[i][j])
    
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
        
        self.gameOver = True
        return True

    def __checkBlock(self, block):
        # Set es usada para guardar múltiples objetos de una 
        # variabe
        return set(block) == set(range(1, 10))
        
    def __checkRow(self, row):
        return self.__checkBlock(self.puzzle[row])

    def __checkColumn(self, column):
        return self.__checkBlock(
            [self.puzzle[row][column] for row in range(9)]
            )
    
    def __checkSquare(self, row, column):
        return self.__checkBlock(
            [
                self.puzzle[r][c]
                for r in range(row * 3, (row + 1) * 3)
                for c in range(column * 3, (column +1) * 3)
            ]
        )