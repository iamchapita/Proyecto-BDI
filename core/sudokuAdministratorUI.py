from tkinter import *
from core.screenCenter import ScreenCenter

class SudokuAdmnistratorUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.__initUI(parent)

    def __initUI(self, parent):
        self.margin = 70 
        self.side = 50
        self.width = self.margin * 2 + self.side * 9
        self.height = self.margin * 2 + self.side * 9 + 120 
        self.center = ScreenCenter()
        self.center.center(parent)
        self.parent.title("Administración")
        self.parent.resizable(FALSE, FALSE)
        self.parent.configure(background = "white")
        self.pack(fill=BOTH)
        self.canvas = Canvas(parent, width = self.width, height = self.height)
        self.canvas.configure(background="white")
        self.canvas.pack(fill=BOTH, side=TOP)
        createUserButton = Button(parent, text = "Crear Usuario", height = 2, width = 15, command = self. fn)
        createUserButton.pack()
        editUserButton = Button(parent, text = "Editar Usuario", height = 2, width = 15, command = self. fn)
        editUserButton.pack()
        deleteUserButton = Button(parent, text = "ELiminar Usuario", height = 2, width = 15, command = self. fn)
        deleteUserButton.pack()
        seeLogButton = Button(parent, text = "Ver bitácora", height = 2, width = 15, command = self. fn)
        seeLogButton.pack()

    def fn(self):
        pass