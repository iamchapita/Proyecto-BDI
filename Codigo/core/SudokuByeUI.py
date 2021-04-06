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
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80, padx=2)
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.grid(row=2,column=1,sticky = "nsew", padx=2)
        self.after(500,self.parent.destroy)
