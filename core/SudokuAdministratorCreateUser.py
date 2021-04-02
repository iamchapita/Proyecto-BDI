from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter

class SudokuAdministratorCreateUser(Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create = Tk()
        super().__init__(self.create)
        self.pack()
        self.__initUI()
        img = PhotoImage(file="images/pause.png", master=self.create)
        Button(self.create, image=img, command=self.goBack, bg="#413c3d").place(x=250, y=480)
        self.master.mainloop()

    def __initUI(self):
        self.icon = PhotoImage(file="images/SudokuLogo.png", master=self.create)
        self.create.iconphoto(True, self.icon)
        self.width = 400
        self.height = 600

        self.center = ScreenCenter()
        self.center.center(self.create, self.width, self.height)

        self.create.title('Crear Usuarios')
        self.create.geometry("%dx%d" %(self.width, self.height))

        # Tamaño de la ventana
        
        # self.create.configure(background = "#413c3d")

        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.create.resizable(False, False)

        #estilos para crear labels
        FontStyles = tkFont.Font(family="Lucida Grande", size=208)
        LabelStyles = tkFont.Font(family="Lucida Grande", size=13)
        
        # Muestra el titulo de la seccion
        label1= Label(self.create, text='Crear un nuevo usuario', font=FontStyles)
        label1.configure(background = "#413c3d", fg="white")
        label1.pack()
        label1.place(x=110,y=100)

        label2= Label(self.create, text='Introduzca el nombre de usuario:', font =LabelStyles)
        label2.configure(background = "#413c3d", fg="#6ea8d9")
        label2.pack()
        label2.place(x=75,y=180)

        input_text = StringVar()
        self.userText = ttk.Entry(self.create, textvariable = input_text)
        self.userText.pack()
        self.userText.place(x=110,y=240, height = 30, width = 200)
        
        Button(self.create, text = 'Crear', command= self.__save, bg="#6ea8d9").place(x=155, y=310, height = 50, width = 110)
        # Button(self.create, text = 'Regresar Menú', command= self.goBack, bg="#6ea8d9").place(x=200, y=480, height = 30, width = 110)
        # self.backgroundImage = PhotoImage(file="images/WelcomeScreen.png", master=self.create)
        # canvas = Canvas(self, width=self.backgroundImage.width(), height=self.backgroundImage.height())
        # labelLogo = Label(self,image=self.backgroundImage)
        # labelLogo.place(x=0, y=0, relwidth=1, relheight=1)
        # canvas.grid(row=0, column=0)

    def __save(self):
        print(self.userText.get())

    def goBack(self):
        self.create.destroy()
        self.parent.deiconify()