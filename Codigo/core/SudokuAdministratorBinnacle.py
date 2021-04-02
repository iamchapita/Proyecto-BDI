from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter

class SudokuAdministratorBinnacle(Frame):

    def __init__(self, parent=None):
        self.parent = parent
        self.binnacle = Tk()
        super().__init__(self.binnacle)
        self.pack()
        self.__initUI()
        img = PhotoImage(file="images/pause.png", master=self.binnacle)
        Button(self.binnacle, image=img, command=self.goBack, bg="#413c3d").place(x=780, y=420)
        self.master.mainloop()

    def __initUI(self):
        self.width = 900
        self.height = 600

        self.center = ScreenCenter()
        self.center.center(self.binnacle, self.width, self.height)

        self.binnacle.title('Bitácora')

        #Tamaño de la ventana
        self.binnacle.geometry("960x540")
        self.binnacle.configure(background = "#413c3d")

        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.binnacle.resizable(False, False)

        #estilos para crear labels
        TitleStyles = tkFont.Font(family="Lucida Grande", size=150)
        ButtonStyles = tkFont.Font(family="Lucida Grande", size=18)


        self.dataView = ttk.Treeview(self.binnacle, columns=("#1","#2"))
        self.dataView.pack()
        self.dataView.heading("#0", text="Indice")
        self.dataView.heading("#1", text="Usuario")
        self.dataView.heading("#2", text="Descripción actividad")
        self.dataView.place(x=40, y=140)
        self.dataView.column("#0", width=50)
        self.dataView.column("#1", width=200)
        self.dataView.column("#2", width=615)

        
        # Muestra el titulo de la seccion
        label1= Label(self.binnacle, text='Registro de bitácora', font =TitleStyles)
        label1.configure(background = "#413c3d", fg="white")
        label1.pack()
        label1.place(x=750,y=100)

    def goBack(self):
        self.binnacle.destroy()
        self.parent.deiconify()