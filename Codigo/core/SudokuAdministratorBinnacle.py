"""
    @author: gehernandezc@unah.hn
    @version: 1.0
    @date 2021/04/03
"""

from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter
from core.Close import DialogClose

class SudokuAdministratorBinnacle(Frame):

    def __init__(self, parent=None):
        self.parent = parent
        self.child = Tk()
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        self.pack()
        self.__initUI()
        img = PhotoImage(file="core/images/back.png", master=self.child)
        btnBack= Button(self.child, image=img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        btnBack.pack()
        btnBack.place(x=880, y=20)
        self.master.mainloop()

    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.width = 900
        self.height = 600

        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)

        self.child.title('Bitácora')

        #Tamaño de la ventana
        self.child.geometry("960x540")
        self.child.configure(background = "#171717")

        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.child.resizable(False, False)

        self.dataView = ttk.Treeview(self.child, columns=("#1","#2"))
        self.dataView.pack()
        self.dataView.heading("#0", text="Indice")
        self.dataView.heading("#1", text="Usuario")
        self.dataView.heading("#2", text="Descripción actividad")
        self.dataView.place(x=45, y=160)
        self.dataView.column("#0", width=50)
        self.dataView.column("#1", width=200)
        self.dataView.column("#2", width=615)
        
        # Muestra el titulo de la seccion
        label1= Label(self.child, text='Registro de bitácora', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=335,y=90)

        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=280,y=485)

    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()

    def __onClosing(self):
        d = DialogClose(self.child)
        self.child.wait_window(d.top)