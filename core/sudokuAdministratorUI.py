from tkinter import *
#from core.screenCenter import ScreenCenter

class SudokuAdmnistratorUI(Frame):

    def __init__(self):
        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        self.margin = 70 
        self.side = 50
        self.width = self.margin * 2 + self.side * 9
        self.height = self.margin * 2 + self.side * 9 + 120 
        # self.center = ScreenCenter()
        # self.center.center(parent)
        self.parent.title("Administración")
        self.parent.resizable(FALSE, FALSE)
        self.parent.configure(background = "white")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self.parent, width = self.width, height = self.height)
        self.canvas.configure(background="white")
        self.canvas.pack(fill=BOTH, side=TOP)
        createUserButton = Button(self, text = "Crear Usuario", height = 2, width = 15, command = self. fn)
        createUserButton.pack()
        editUserButton = Button(self, text = "Editar Usuario", height = 2, width = 15, command = self. fn)
        editUserButton.pack()
        deleteUserButton = Button(self, text = "ELiminar Usuario", height = 2, width = 15, command = self. fn)
        deleteUserButton.pack()
        seeLogButton = Button(self, text = "Ver bitácora", height = 2, width = 15, command = self.fn)
        seeLogButton.pack()

    def fn(self):
        pass


obj = SudokuAdmnistratorUI()