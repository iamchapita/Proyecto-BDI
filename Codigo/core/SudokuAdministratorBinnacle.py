from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from core.ScreenCenter import ScreenCenter
from core.SudokuByeUI import SudokuBye
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLToolConnection import ToolConnection

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
        
        self.config = ConfigConnection() #Conexión al archivo de configuración
        self.db = MySQLEngine(self.config.getConfig()) #Conexión a la base de datos

        self.pack()
        self.__initUI()
    
    """
    Creación de los widgets que se veran en pantalla.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __initUI(self):
        self.img = PhotoImage(file="core/images/back.png", master=self.child)
        self.backButton= Button(self.child, image=self.img, command= self.__goBack,bg="#171717", borderwidth=0, highlightthickness=0)
        self.backButton.pack()
        self.backButton.place(x=880, y=20)
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

        self.dataView = ttk.Treeview(self.child, columns=("#1","#2", "#3"))
        self.dataView.pack()

        self.dataView.heading("#0", text="Indice", anchor = CENTER)
        self.dataView.heading("#1", text="Usuario", anchor = CENTER)
        self.dataView.heading("#2", text="Descripción actividad", anchor = CENTER)
        self.dataView.heading("#3", text="Fecha y Hora", anchor = CENTER)

        self.dataView.place(x=45, y=160)
        self.dataView.column("#0", width=50, anchor = CENTER)
        self.dataView.column("#1", width=200, anchor = CENTER)
        self.dataView.column("#2", width=420)
        self.dataView.column("#3", width=180, anchor = CENTER)
        
        label1= Label(self.child, text='Registro de bitácora', font=("Lato",25))
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=335,y=90)

        labelBrand = Label(self.child, image=self.brand, borderwidth=0)
        labelBrand.pack()
        labelBrand.place(x=280,y=485)

        self.loadBinacle()

    
    """
        Obtiene todas los registros o actividades de cada uno 
        de los usuarios (login, log-out, fecha y hora, estado del tablero)
    """
    def loadBinacle(self) -> None: 
        
        #Obtiene la información de la bitácora y el nombre de cada usuario
        #Esta consulta se realiza de está forma debido a la naturaleza del data view
        query = """
                    SELECT 
                        User.tex_nickname AS name,
                        Result.state AS state,
                        Result.date AS date
                    FROM
                    (
                        SELECT 
                            user, 
                            state, 
                            date
                        FROM vw_Binacle
                    ) Result 
                    INNER JOIN 
                        User ON Result.user = User.id
                    ORDER BY 
                        Result.date DESC;
                """

        transaction = self.db.select( query=query )

        if transaction:
            count = len(transaction)
            for data in transaction:
                self.dataView.insert("", 0, text="{}".format(count) , values=(data[0], data[1], data[2]))
                count -=1
        else: 
            print("El jugador no tiene juegos finalizados")
    
    
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
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            
            self.child.destroy()
            sys.exit()
            SudokuBye()
        else:
            pass