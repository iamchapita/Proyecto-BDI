from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

class SudokuAdministratorEditUser(Frame):

    def __init__(self, parent):
        self.parent = parent
        self.edit = Tk()
        super().__init__(self.edit)
        self.pack()
        self.__initUI()
        img = PhotoImage(file="images/pause.png", master=self.edit)
        Button(self.edit, image=img, command=self.goBack, bg="#413c3d").place(x=250, y=480)
        self.master.mainloop()

    def __initUI(self):

        self.edit.title('Crear Usuarios')

        #Tamaño de la ventana
        self.edit.geometry("400x600")
        self.edit.configure(background = "#413c3d")

        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.edit.resizable(False, False)

        #estilos para crear labels
        FontStyles = tkFont.Font(family="Lucida Grande", size=208)
        LabelStyles = tkFont.Font(family="Lucida Grande", size=13)

        
        # Muestra el titulo de la seccion
        label1= Label(self.edit, text='Editar usuario', font=FontStyles)
        label1.configure(background = "#413c3d", fg="white")
        label1.pack()
        label1.place(x=150,y=80)

        label2= Label(self.edit, text='Introduzca el nombre de usuario a editar:', font =LabelStyles)
        label2.configure(background = "#413c3d", fg="#6ea8d9")
        label2.pack()
        label2.place(x=50,y=150)

        
        input_text1 = StringVar()
        self.userText = ttk.Entry(self.edit, textvariable = input_text1)
        self.userText.pack()
        self.userText.place(x=110,y=200, height = 30, width = 200)

        label3= Label(self.edit, text='Introduzca el nuevo nombre de usuario:', font =LabelStyles)
        label3.configure(background = "#413c3d", fg="#6ea8d9")
        label3.pack()
        label3.place(x=50,y=250)
        
        input_text2 = StringVar()
        self.userTextEdited = ttk.Entry(self.edit, textvariable = input_text2)
        self.userTextEdited.pack()
        self.userTextEdited.place(x=110,y=300, height = 30, width = 200)
        
        Button(self.edit, text = 'Editar', command= self.__save, bg="#6ea8d9").place(x=155, y=370, height = 50, width = 110)

    def __save(self):
        print(self.userText.get())
        print(self.userTextEdited.get())

    def goBack(self):
        self.edit.destroy()
        self.parent.deiconify()