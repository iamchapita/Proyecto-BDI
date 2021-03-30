from tkinter import *
from core.sudokuUI import *
from core.sudokuGame import SudokuGame
from core.sudokuUI import SudokuUI

class Screen:
    def __init__(self):
        self.MARGIN = 20
        self.SIDE = 50
        self.WIDTH =  self.MARGIN * 2 + self.SIDE * 9 + 60
        self.HEIGHT = self.MARGIN * 2 + self.SIDE * 9 + 100

    def SplashScreen(self):
        global splash
        splash = Tk()
        splash.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        splash.title("Bievenido a Sudoku!")
        self.endSplashScreen()

    def LoginPage(self):
        splash.destroy()

        loginPage = Tk()
        loginPage.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        loginButton = Button(loginPage, text = "Ingresar", command = lambda: self.StartPage(loginPage))

        userLabel = Label(loginPage, text="Username")
        userLabel.pack()

        userText = Entry(loginPage)
        userText.pack()
        
        userPass = Label(loginPage, text="Password")
        userPass.pack()

        passText = Entry(loginPage)
        passText.pack()

        loginButton.pack()
        loginPage.mainloop()

    def StartPage(self,loginPage):
        loginPage.destroy()
        startPage = Tk()
        startPage.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        newGameButton = Button(startPage, text = "Juego Nuevo", command = lambda: self.MainGame(startPage))
        newGameButton.pack()
        startPage.mainloop()

    def MainGame(self,startPage):
        startPage.destroy()

        with open('debug.sudoku', 'r') as boardFile:
            game = SudokuGame(boardFile)
            game.start()
            root = Tk()
            SudokuUI(root, game)
            root.geometry("%dx%d" % (self.WIDTH, self.HEIGHT + 40))
            root.mainloop()

    def endSplashScreen(self):
        splash.after(3000,self.LoginPage)
        splash.mainloop()



