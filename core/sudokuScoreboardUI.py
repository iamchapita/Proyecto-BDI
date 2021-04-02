from tkinter import *
import os

class SudokuScoreboardUI(Frame):

    def __init__(self):

        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):

        self.width = 400
        self.height = 300
        self.logo = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.parent.title("Scoreboard")
        self.parent.resizable(False, False)
        self.parent.geometry("%dx%d"%(self.width, self.height))
        self.parent.iconphoto(True, self.logo)

        os.chdir("./Scripts de Base de Datos")
        file = open("scoreboardTest.txt")
        data = file.read()
        file.close()

        results = Text(self)
        results.insert(INSERT, data)
        results.configure(state="disabled", background="#413c3d", foreground="white")
        results.grid(row=0, column = 0)
