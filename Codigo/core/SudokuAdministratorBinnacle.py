from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose
from core.SudokuByeUI import SudokuBye

"""
Frame que permite visualizar todos los componentes de la bitacora.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuAdministratorBinnacle(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
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

    """
    Creación de los widgets que se veran en pantalla.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.width = 900
        self.height = 600

        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)

        self.child.title('Bitácora')
        self.child.geometry("960x540")
        self.child.configure(background = "#171717")
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
        
        label1= Label(self.child, text='Registro de bitácora', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=335,y=90)

        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=280,y=485)

    """
    Función que permite regresar a la ventana anterior al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()

    """
    Función que pregunta al usuario si desea salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 3.0
    """
    def __onClosing(self):
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            self.child.destroy()
            sys.exit()
            SudokuBye()
        else:
            pass