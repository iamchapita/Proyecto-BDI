from tkinter import *
from tkinter import ttk
from core.screenCenter import ScreenCenter
from core.sudokuLoginPageUI import SudokuLoginPageUI

class SudokuSplashScreenUI(ttk.Frame):

    def __init__(self, parent=None):
        if not parent:
            parent = Tk()
            parent.title("Bienvenido")
            parent.resizable(FALSE, FALSE)

        super().__init__(parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        self.margin = 70 
        self.side = 50
        self.width = self.margin * 2 + self.side * 9
        self.height = self.margin * 2 + self.side * 9 + 120 
        #self.center = ScreenCenter()
        #self.center.center(self)
        #self.configure(background = "white")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self, width=self.width, height= self.height)
        self.canvas.configure(background = "white")
        self.canvas.pack(fill=BOTH, side=TOP)

        ttk.Button(self, text = "Entrar", command = self.goToLoginPage).pack()

    def goToLoginPage(self):
        self.destroy()
        SudokuLoginPageUI(self.master)
        
    