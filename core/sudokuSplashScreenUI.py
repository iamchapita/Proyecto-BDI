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
            self.logo = PhotoImage(file = "core/images/SudokuLogo.png")
            parent.iconphoto(True,self.logo)


        self.logoImage = PhotoImage(file = "core/images/WelcomeScreen.png")
        super().__init__(parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        
        canvasObject = Canvas(self,height=self.logoImage.height(), width=self.logoImage.width())
        l_logo = Label(self,image=self.logoImage)
        l_logo.place(x=0, y=0, relwidth=1, relheight=1)
        canvasObject.grid(row=0,column=0)

        ttk.Button(self, text = "Entrar", command = self.goToLoginPage).grid(pady=40)

    def goToLoginPage(self):
        self.destroy()
        SudokuLoginPageUI(self.master)
        
    