from tkinter import *
from core.SudokuMainWindowUI import SudokuMainWindowUI
from core.SudokuAdministratorUI import * 
from core.ScreenCenter import *

class SudokuLoginPageUI(Frame):

    def __init__(self):
        
        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):

        self.width = 400
        self.height = 600
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.backgroundImage = PhotoImage(file="core/images/LoginScreen.png", master=self.parent)
        self.parent.title("Inicio de Sesión")
        self.parent.resizable(False, False)
        self.parent.geometry("%dx%d"%(self.width, self.height))
        self.parent.iconphoto(True, self.logo)
        center = ScreenCenter()
        center.center(self.parent, self.width, self.height)
        canvas = Canvas(self, width=self.backgroundImage.width(), height=self.backgroundImage.height())
        labelLogo = Label(self,image=self.backgroundImage)
        labelLogo.place(x=0, y=0, relwidth=1, relheight=1)
        canvas.grid(row=0, column=0)
        usernameText = StringVar()
        usernameEntry = Entry(self, textvariable = usernameText)
        passwordText = StringVar()
        passwordEntry = Entry(self, textvariable = passwordText, show = "*")
        canvas.create_window(200, 120, window=usernameEntry)
        canvas.create_window(200, 210, window=passwordEntry)
        loginButton = Button(self, text="Iniciar Sesión", bg="#6ea8d9",width=15, height=2, command = lambda: self.__loginFn(usernameText, passwordText))
        canvas.create_window(200, 260, window=loginButton)

    def __loginFn(self, username = "", password = ""):

        if(len(username.get()) == 0):
            self.parent.destroy()
            SudokuMainWindowUI()
        else:
            self.parent.destroy()
            SudokuAdministratorUI()