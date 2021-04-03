from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter

class SudokuAdministratorCreateUser(Frame):

    def __init__(self, parent):
        self.parent = parent
        self.child = Tk()
        super().__init__(self.child)
        self.pack()
        self.__initUI()
        img = PhotoImage(file="core/images/back.png", master=self.child)
        btnBack= Button(self.child, image=img, command= self.goBack,bg="#171717", borderwidth=0, highlightthickness=0)
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

        self.child.title('Crear Usuarios')
        self.child.geometry("%dx%d" %(self.width, self.height))

        # Tamaño de la ventana
        
        self.child.configure(background = "#171717")

        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.child.resizable(False, False)

        #estilos para crear labels
        
        # Muestra el titulo de la seccion
        label1= Label(self.child, text='Crear un nuevo usuario', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=30,y=120)

        label2= Label(self.child, text='Introduzca el nombre de usuario:', font =("Lato",15))
        label2.configure(background = "#171717", fg="#6ea8d9")
        label2.pack()
        label2.place(x=65,y=200)

        input_text = StringVar()
        self.userText = ttk.Entry(self.child, textvariable = input_text, font=("Lato",10),  justify=CENTER)
        self.userText.pack()
        self.userText.place(x=110,y=240, height = 30, width = 200)
        
        Button(self.child, text = 'Crear', command= self.__save, bg="#6ea8d9", font=("Lato",15)).place(x=155, y=310, height = 50, width = 110)
        # Button(self.child, text = 'Regresar Menú', command= self.goBack, bg="#6ea8d9").place(x=200, y=480, height = 30, width = 110)
        # self.backgroundImage = PhotoImage(file="images/WelcomeScreen.png", master=self.child)
        # canvas = Canvas(self, width=self.backgroundImage.width(), height=self.backgroundImage.height())
        # labelLogo = Label(self,image=self.backgroundImage)
        # labelLogo.place(x=0, y=0, relwidth=1, relheight=1)
        # canvas.grid(row=0, column=0)
        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=8,y=555)

    def __save(self):
        print(self.userText.get())
        self.userText.delete(0, "end")

    def goBack(self):
        self.child.destroy()
        self.parent.deiconify()