from tkinter import *
from core.ScreenCenter import ScreenCenter
from core.SudokuLoginPageUI import SudokuLoginPageUI

class SudokuSplashScreenUI(Frame):

    def __init__(self):
        
        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.backgroundImage = PhotoImage(file="core/images/WelcomeScreen.png", master=self.parent)
        self.parent.title("Bienvenido")
        self.parent.resizable(False, False)
        self.parent.iconphoto(True, self.icon)
        self.parent.geometry("%dx%d" % (self.backgroundImage.width(), self.backgroundImage.height()))
        center = ScreenCenter()
        center.center(self.parent, self.backgroundImage.width(), self.backgroundImage.height())
        canvas = Canvas(self, width=self.backgroundImage.width(), height=self.backgroundImage.height())
        labelLogo = Label(self,image=self.backgroundImage)
        labelLogo.place(x=0, y=0, relwidth=1, relheight=1)
        canvas.grid(row=0, column=0)
        self.after(1500, self.goToLoginPage)

    def goToLoginPage(self):
        self.parent.destroy()
        SudokuLoginPageUI()
        
    