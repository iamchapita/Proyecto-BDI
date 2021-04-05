from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose

"""
Frame que permite la visualización para editar un usuario.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuAdministratorEditUser(Frame):

    """
    Constructor de la clase.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self, parent):
        self.parent = parent
        self.child = Tk()
        self.child.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.child)
        img = PhotoImage(file="core/images/back.png", master=self.child)
        btnBack= Button(self.child, image=img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        btnBack.pack()
        btnBack.place(x=315, y=20)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    """
    Creación de los widgets.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.child)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.child)
        self.width = 400
        self.height = 600
        self.center = ScreenCenter()
        self.center.center(self.child, self.width, self.height)
        self.child.title('Editar Usuarios')
        self.child.iconphoto(True, self.icon)
        #Tamaño de la ventana
        self.child.geometry("%dx%d" %(self.width, self.height))
        self.child.configure(background = "#171717")
        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.child.resizable(False, False)
        
        # Muestra el titulo de la seccion
        label1= Label(self.child, text='Editar usuario', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=100,y=100)

        label2= Label(self.child, text='Introduzca el nombre de usuario a editar:', font =("Lato",15))
        label2.configure(background = "#171717", fg="#6ea8d9")
        label2.pack()
        label2.place(x=20,y=170)
        
        input_text1 = StringVar()
        self.userText = ttk.Entry(self.child, textvariable = input_text1, font=("Lato",10),  justify=CENTER)
        self.userText.pack()
        self.userText.place(x=110,y=210, height = 30, width = 200)

        label3= Label(self.child, text='Introduzca el nuevo nombre de usuario:', font =("Lato",15))
        label3.configure(background = "#171717", fg="#6ea8d9")
        label3.pack()
        label3.place(x=25,y=270)
        
        input_text2 = StringVar()
        self.userTextEdited = ttk.Entry(self.child, textvariable = input_text2, font=("Lato",10),  justify=CENTER)
        self.userTextEdited.pack()
        self.userTextEdited.place(x=110,y=310, height = 30, width = 200)
        
        Button(self.child, text = 'Editar', command= self.__save, bg="#6ea8d9", font=("Lato",15)).place(x=155, y=380, height = 50, width = 110)
        
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=8,y=555)

    """
    Función que permite guardar los cambios.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __save(self):
        print(self.userText.get())
        print(self.userTextEdited.get())
        self.userText.delete(0, "end")
        self.userTextEdited.delete(0, "end")

    """
    Función que permite regresar a la ventana anterior al presionar el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goBack(self):
        self.child.destroy()
        self.parent.deiconify()
    
    """
    Función que permite minimizar o salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __onClosing(self):
        self.dialogClose = DialogClose(self.parent)
        self.parent.wait_window(self.dialogClose)