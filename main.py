import argparse
from tkinter import *
from core.sudokuGame import SudokuGame
from core.sudokuBoardUI import SudokuBoardUI
from core.sudokuLoginPageUI import SudokuLoginPageUI
from core.sudokuMainWindowUI import SudokuMainWindowUI
from core.sudokuSplashScreenUI import SudokuSplashScreenUI
from core.sudokuAdministratorUI import SudokuAdmnistratorUI

boards = ['debug', 'n00b', 'l33t', 'error']
margin = 20
side = 50
width =  margin * 2 + side * 9 + 60
height = margin * 2 + side * 9 + 100

if __name__ == '__main__':
    
    with open('core/sudoku/n00b.sudoku', 'r') as boardFile:
        obj = SudokuSplashScreenUI()