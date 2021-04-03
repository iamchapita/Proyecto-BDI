"""
    @author: gehernandezc@unah.hn
    @version: 1.0
    @date 2021/04/03
"""

from tkinter import *
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter
from core.Close import DialogClose

class SudokuAdministratorDeleteUser(Frame):

    def __init__(self, parent):
        self.parent = parent
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
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.child.iconphoto(True, self.icon)
        self.width = 400
        self.height = 600
        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)
        self.child.title('Eliminar Usuarios')
        #Tamaño de la ventana
        self.child.geometry("%dx%d" %(self.width, self.height))
        self.child.configure(background = "#171717")
        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.child.resizable(False, False)

        # Muestra el titulo de la seccion
        label1= Label(self.child, text='Eliminar usuario', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=80,y=120)

        label2= Label(self.child, text='Introduzca el nombre de usuario a eliminar:', font =("Lato",15))
        label2.configure(background = "#171717", fg="#6ea8d9")
        label2.pack()
        label2.place(x=10,y=200)

        input_text = StringVar()
        self.userText = ttk.Entry(self.child, textvariable = input_text, font=("Lato",10),  justify=CENTER)
        self.userText.pack()
        self.userText.place(x=110,y=250, height = 30, width = 200)

        Button(self.child, text = 'Eliminar', command= self.__save, bg="#6ea8d9", font=("Lato",15)).place(x=155, y=340, height = 50, width = 110)

        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=8,y=555)

    def __save(self):
        print(self.userText.get())
        self.userText.delete(0, "end")

    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()
    
    def __onClosing(self):
        d = DialogClose(self.child)
        self.child.wait_window(d.top)