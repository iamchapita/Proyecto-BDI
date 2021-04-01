import argparse
from tkinter import *
from core.sudokuSplashScreenUI import SudokuSplashScreenUI

boards = ['debug', 'n00b', 'l33t', 'error']
margin = 20
side = 50
width =  margin * 2 + side * 9 + 60
height = margin * 2 + side * 9 + 100

if __name__ == '__main__':
    
    with open('core/sudoku/n00b.sudoku', 'r') as boardFile:
        obj = SudokuSplashScreenUI()