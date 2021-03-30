import argparse
from tkinter import *
from core.sudokuGame import SudokuGame
from core.sudokuUI import SudokuUI
from core.allScreen import Screen

BOARDS = ['debug', 'n00b', 'l33t', 'error']
MARGIN = 20
SIDE = 50
WIDTH =  MARGIN * 2 + SIDE * 9 + 60
HEIGHT = MARGIN * 2 + SIDE * 9 + 100


if __name__ == '__main__':

    # with open('%s.sudoku' % board_name, 'r') as boards_file:
    (Screen()).SplashScreen()
        
        
