"""
    @author: gehernandezc@unah.hn
    @version: 1.0
    @date 2021/04/03
"""

from tkinter import *
from tkinter import ttk
from core.ScreenCenter import ScreenCenter
from core.SudokuAdministratorCreateUser import *
from core.SudokuAdministratorDeleteUser import *
from core.SudokuAdministratorEditUser import *
from core.Close import DialogClose

class SudokuUserAdministration(Frame):

    def __init__(self, parent):
        self.parent=parent
        self.child = Tk()
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        self.pack()
        self.__initUI()
        img = PhotoImage(file="core/images/back.png", master=self.child)
        btnBack= Button(self.child, image=img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        btnBack.pack()
        btnBack.place(x=315, y=20)
        self.master.mainloop()

    def __initUI(self):
        # Se debe utilizar la ruta core/images/SudokuLogo.png al implementarlo en el main
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.width = 400
        self.height = 600
        self.child.title('Administración de usuarios')
        self.child.iconphoto(True, self.icon)
        # Tamaño de la ventana
        self.child.geometry("%dx%d" % (self.width, self.height))

        self.child.configure(background = "#171717")
        self.child.resizable(False, False)
        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)
        label1= Label(self.child, text='Administrar usuarios', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=60,y=120)
        Button(self.child, text = 'Crear usuario', bg="#6ea8d9", font=("Lato",17), command= self.__goCreateUser).place(x=50, y=220, height = 50, width = 310)
        Button(self.child, text = 'Editar usuario', bg="#6ea8d9", font=("Lato",17), command= self.__goEditUser).place(x=50, y=280, height = 50, width =310)
        Button(self.child, text = 'Eliminar usuario', bg="#6ea8d9", font=("Lato",17), command= self.__goDeleteUser).place(x=50, y=340, height = 50, width =310)
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=0,y=555)
    
    def __goCreateUser(self):
        self.child.withdraw()
        SudokuAdministratorCreateUser(parent=self.child)
    
    def __goDeleteUser(self):
        self.child.withdraw()
        SudokuAdministratorDeleteUser(parent=self.child)

    def __goEditUser(self):
        self.child.withdraw()
        SudokuAdministratorEditUser(parent=self.child)

    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()

    def __onClosing(self):
        d = DialogClose(self.child)
        self.child.wait_window(d.top)