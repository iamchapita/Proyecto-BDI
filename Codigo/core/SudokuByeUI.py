from tkinter import *
from core.ScreenCenter import ScreenCenter

"""
Frame que muestra un pequeño mensaje de adios
cuando el usuario se sale por completo del juego.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuBye(Frame):

    """
    Constructor de la clase.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self):

        self.parent = Tk()
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    """
    Creación de los widgets.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):

        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        self.width = 400
        self.height = 300
        self.parent.title('¡Adios!')
        self.parent.iconphoto(True, self.icon)

        self.parent.geometry("%dx%d" % (self.width, self.height))
        self.parent.configure(background = "#171717")
        self.parent.resizable(False, False)

        self.center = ScreenCenter()
        self.center.center(self.parent, self.width, self.height)

        label1= Label(self.parent, text='¡Vuelve Pronto!', font=("lato", 25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=60,y=120)
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.pack()
        label2.place(x=8,y=200)
        self.after(2000,self.parent.destroy)
