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

    def center(self, win, par_width, par_height):
        """
        centers a tkinter window
        :param win: the root or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width() + par_width
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height() + par_height
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def SplashScreen(self):
        global splash
        splash = Tk()
        self.center(splash, 200, 300)
        splash.title("¡Bienvenido a Sudoku!")
        self.endSplashScreen()

    def LoginPage(self):
        splash.destroy()

        loginPage = Tk()
        # loginPage.geometry("%dx%d" % (self.WIDTH, self.HEIGHT + 40))
        self.center(loginPage, 0, 40)
        loginButton = Button(loginPage, text = "Ingresar", command = lambda: self.AdministratorPage(loginPage))

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

    # Función que loggea un usuario normal (Funcional)
    # def StartPage(self,loginPage):
    #     loginPage.destroy()
    #     startPage = Tk()
    #     # startPage.geometry("%dx%d" % (self.WIDTH, self.HEIGHT + 40))
    #     self.center(startPage, 0, 40)
    #     newGameButton = Button(startPage, text = "Juego Nuevo", command = lambda: self.MainGame(startPage))
    #     newGameButton.pack()
    #     startPage.mainloop()
    
    def AdministratorPage(self,loginPage):
        loginPage.destroy()
        startPage = Tk()
        # startPage.geometry("%dx%d" % (self.WIDTH, self.HEIGHT + 40))
        self.center(startPage, 40, 40)
        CreateUser = Button(startPage, text = "Crear Usuario", height = 2, width = 15, command = lambda: self.MainGame(startPage))
        CreateUser.pack()
        EditUser = Button(startPage, text = "Editar Usuario", height = 2, width = 15, command = lambda: self.MainGame(startPage))
        EditUser.pack()
        DeleteUser = Button(startPage, text = "ELiminar Usuario", height = 2, width = 15, command = lambda: self.MainGame(startPage))
        DeleteUser.pack()
        SeeLog = Button(startPage, text = "Ver bitácora", height = 2, width = 15, command = lambda: self.MainGame(startPage))
        SeeLog.pack()

        startPage.mainloop()

    def MainGame(self,startPage):
        startPage.destroy()

        with open('debug.sudoku', 'r') as boardFile:
            game = SudokuGame(boardFile)
            game.start()
            root = Tk()
            SudokuUI(root, game)
            # root.geometry("%dx%d" % (self.WIDTH, self.HEIGHT + 40))
            self.center(root, 0, 0)
            root.mainloop()

    def endSplashScreen(self):
        splash.after(3000,self.LoginPage)
        splash.mainloop()

    

