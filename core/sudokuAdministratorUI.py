from tkinter import *
from SudokuAdministratorCreateUser import *
from SudokuAdministratorDeleteUser import *
from SudokuAdministratorEditUser import *
from SudokuAdministratorBinnacle import *
#from core.screenCenter import ScreenCenter

class SudokuAdmnistratorUI(Frame):

    def __init__(self):
        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        self.parent.title('Opciones Administrador')

        #Tamaño de la ventana
        self.parent.geometry("400x600")
        self.parent.configure(background = "#413c3d")

        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.parent.resizable(False, False)
        
        TitleStyles = tkFont.Font(family="Lucida Grande", size=18)
        
        # self.center = ScreenCenter()
        # self.center.center(parent)

        Button(self.parent, text = 'Crear usuario', bg="#6ea8d9", font=TitleStyles, command= self.goCreateUser).place(x=100, y=110, height = 50, width = 210)
        Button(self.parent, text = 'Editar usuario', bg="#6ea8d9", font=TitleStyles, command= self.goEditUser).place(x=100, y=190, height = 50, width = 210)
        Button(self.parent, text = 'Eliminar usuario', bg="#6ea8d9", font=TitleStyles, command= self.goDeleteUser).place(x=100, y=270, height = 50, width = 210)
        Button(self.parent, text = 'Ir al juego', bg="#6ea8d9", font=TitleStyles, command= self.goGame).place(x=100, y=350, height = 50, width = 210)
        Button(self.parent, text = 'Bitácora', bg="#6ea8d9", font=TitleStyles, command= self.goBinnacle).place(x=100, y=430, height = 50, width = 210)
        Button(self.parent, text = 'Salir', bg="#6ea8d9", font=TitleStyles, command= self.quit).place(x=100, y=500, height = 50, width = 210)
        
    def goCreateUser(self):
        self.parent.withdraw()
        SudokuAdministratorCreateUser(parent=self.parent)
    
    def goDeleteUser(self):
        self.parent.withdraw()
        SudokuAdministratorDeleteUser(parent=self.parent)

    def goEditUser(self):
        self.parent.withdraw()
        SudokuAdministratorEditUser(parent=self.parent)

    def goBinnacle(self):
        self.parent.withdraw()
        SudokuAdministratorBinnacle(parent=self.parent)

    def goGame(self):
        pass

    def quit(self):
        self.parent.destroy()

obj = SudokuAdmnistratorUI()