from tkinter import *
from tkinter import messagebox
from core.ScreenCenter import ScreenCenter
from core.SudokuGame import SudokuGame
from core.SudokuBoardUI import SudokuBoardUI
from core.SudokuScoreboardUI import SudokuScoreboardUI
from core.DialogClose import DialogClose
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLToolConnection import ToolConnection

from random import randint
import os


"""
Frame que muestra el Main Window y todos sus respectivos widgets de la aplicación
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuMainWindowUI(Frame):

    """
    Constructor de la clase donde si incializan todos los componentes de
    la ventana.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self):
        self.parent = Tk()
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.config = ConfigConnection() #Conexión al archivo de configuración        
        self.db = MySQLEngine( self.config.getConfig() ) #Conexión a la base de datos
        self.idBoard = None #Numero del board seleccionado
        super().__init__(self.parent)

        self.username = ""
        self.idUsername = None
        self.getUsernameLogin()   

        self.__initUI()
        self.master.mainloop()     

    """
    Creación de los widgets que se veran en pantalla.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        self.width = 400
        self.height = 600
        self.parent.title('Menu')
        self.parent.iconphoto(True, self.icon)

        self.parent.geometry("%dx%d" % (self.width, self.height))
        self.parent.configure(background = "#171717")
        self.parent.resizable(False, False)

        self.center = ScreenCenter()
        self.center.center(self.parent, self.width, self.height)

        label1= Label(self.parent, text='¿Qué deseas hacer?', font=("lato", 20))
        label1.configure(background = "#171717", fg="white")
        label1.grid(row=1,column=1,sticky = "nsew", pady = 80, padx=70)

        Button(self.parent, text = 'Nuevo juego', bg="#6ea8d9", font=("lato", 17), command= self.__newGame).grid(row=2,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=37)
        Button(self.parent, text = 'Continuar juego', bg="#6ea8d9", font=("lato", 17), command= self.__continueGame).grid(row=3,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=18)
        Button(self.parent, text = 'Mejores puntajes', bg="#6ea8d9", font=("lato", 17), command= self.__bestScores).grid(row=4,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=11)
        Button(self.parent, text = 'Salir', bg="#6ea8d9", font=("lato", 17), command= self.__onClosing).grid(row=5,column=1,sticky = "nsew", pady = 5, padx=80, ipadx=83)
        
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.grid(row=6,column=1,pady = 130)

    """
    Función que inicia el juego cuando se presiona el botón.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __newGame(self):
        
        filename = "n00b.sudoku"

        query = "SELECT id, tex_board FROM SudokuBoard"
        #Obtiene la información de todos los boards (tableros iniciales) cargados en la entidad SudokuBoard
        sudokuBoard = self.db.select(query=query)


        #Carga la información de sudokuBoard al archivo n00b.sudoku
        self.__processFile(filename, sudokuBoard)

        #Carga la información de tablero 'nuevo' a la base de datos
        self.__createNewGame()
        
        #with open('core/sudoku/n00b.sudoku', 'r') as boardFile:
        with open('core/sudoku/{}'.format(filename), 'r') as boardFile:
            self.parent.destroy()
            game = SudokuGame(boardFile)
            game.start()
            root = Tk()
            SudokuBoardUI(root, game)
            root.mainloop()


    """
        Creación de un nuevo registro de Juego
        dentro de la base de datos
    """
    def __createNewGame(self):
        
        self.db.insert(
                table="Game", 
                fields=[
                            "id_user_fk",
                            "id_sudokuboard_fk", 
                            "blo_file", 
                            "tim_time", 
                            "cod_nameState"
                        ], 
                values=[
                            self.idUsername, 
                            self.idBoard, 
                            "[]", 
                            "00:00:00", 
                            1
                ]
            )
        
        self.db.closeConnection()

    """
        Se escribe un nuevo tablero dentro del archivo .sudoku
        @data = [(id, tex_board)]
    """
    def __processFile(self, filename, data=[]): 
        
        boardFile = open('core/sudoku/{}'.format(filename), 'w')
        #Borra la información contenida en el documento
        boardFile.truncate()

        if data:     
            
            index = randint(0, len(data)-1)

            #Se selecciona un board al azar
            board = data[index][1]

            self.idBoard = data[index][0]

            #Escribe el nuevo tablero en el documento .sudoku
            boardFile.write( board )

        boardFile.close()
                

    """
    Función que permite continuar un juego pausado.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __continueGame(self):
        pass

    """
    Función que permite visualizar los mejores puntajes.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __bestScores(self):
        self.parent.withdraw()
        SudokuScoreboardUI(parent=self.parent)

    """
    Función que pregunta al usuario si desea salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 2.0
    """
    def __onClosing(self):
        MsgBox = messagebox.askquestion ('Salir','Estas seguro de que te quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            self.child.destroy()
            sys.exit()
        else:
            pass

    
    """
        Asigna los valores de inicio de sesión del usuario 
        logeado (id, username)
    """        
    def getUsernameLogin(self):

        self.idUsername, self.username = (ToolConnection()).getLastLoginUser()

        print( "A VER id: {}, username: {}".format(self.idUsername, self.username) )