from tkinter import *
from core.ScreenCenter import ScreenCenter
from core.DialogClose import DialogClose
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.FileManipulation.EncryptDecrypt import EncryptDecryptSudokuFile
from core.SudokuByeUI import SudokuBye

MARGIN = 70 # ! Se le sumaron 20 y se restaron 20 en los parámetros necesarios.
SIDE = 50
WIDTH = MARGIN * 2 + SIDE * 9
HEIGHT = MARGIN * 2 + SIDE * 9 +120# !Se le sumaron 120 para ampliar de forma vertical la ventana

class SudokuBoardUI(Frame):
    
    def __init__(self, parent, game):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)
        self.game = game
        self.row = -1
        self.col = -1
        self.timeNow = "00:00:00" #Tiempo en pausa
        self.config = ConfigConnection() #Conexión al archivo de configuración
        self.db = MySQLEngine(self.config.getConfig()) #Conexión a la base de datos
        self.stack = [] #{row: , col: , val: , state: } Coordenadas del ingreso de los datos a la tabla
        self.undoStack = []  #{row: , col: , val: , state: } Coordenadas de las jugadas deshechas
        self.encryptDecrypt = EncryptDecryptSudokuFile( self.db ) #Encripta y desencripta los datos del tablero
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.username = ""
        self.idUsername = None
        self.idBoard = None #Numero del board seleccionado
        self.getUsernameLogin()
        self.__initUI()

    def __initUI(self):
        self.parent.title("Sudoku")
        self.parent.resizable(FALSE, FALSE)
        self.parent.configure(background = "#171717")
        self.parent.geometry("%dx%d" %(550, 685))
        center = ScreenCenter()
        center.center(self.parent, WIDTH, 682)
        self.pack(fill=BOTH)
        self.canvas = Canvas(self.parent, width=WIDTH, height= 540)
        self.canvas.configure(background = "#171717")
        self.canvas.pack(fill=BOTH, side=TOP)

        #'Nombre de usuario'
        self.labelNameUser= Label(self.parent, text=self.username, font=("Lato",13))
        self.labelNameUser.configure(background = "#171717", fg="white")
        self.labelNameUser.pack()
        self.labelNameUser.place(x=50,y=20)

        self.timer = StringVar()
        
        self.labelTime= Label(self.parent, text='00:00:00', font=("Lato",13))
        self.labelTime.configure(background = "#171717", fg="white")
        self.labelTime.pack()
        self.labelTime.place(x=430,y=20)

        self.clearButton = Button(self.parent, text="Limpiar Tablero", bg="#6ea8d9", font=("Lato",15), command=self.__clearAnswers)
        self.clearButton.pack(fill=BOTH, side=BOTTOM)
        self.returnButton = Button(self.parent, text="Deshacer jugada", bg="#6ea8d9", font=("Lato",15), command=self.__undoMove)
        self.returnButton.pack(fill=BOTH, side=BOTTOM)
        self.pauseButton = Button(self.parent, text="Pausa", bg="#6ea8d9", font=("Lato",15), command=self.__pauseGame)
        self.pauseButton.pack(fill=BOTH, side=BOTTOM)
        self.finishButton = Button(self.parent, text="Finalizar partida", bg="#6ea8d9", font=("Lato",15), command=self.__endGame)
        self.finishButton.pack(fill=BOTH, side=BOTTOM)
        
        self.__drawGrid()
        self.__drawPuzzle()
        self.canvas.bind("<Button-1>", self.__cellClicked)
        self.canvas.bind("<Key>", self.__keyPressed)
        self.__timer()
    
    def __endGame(self):
        MsgBox = messagebox.askquestion ('Finalizar partida','¿Está seguro de finalizar la partida como derrota?',icon = 'warning')
        if MsgBox == 'yes':

            self.pauseTime()
            
            #El juego termina y el estado del tablero cambia
            (ToolConnection()).updateGameBoard(
                            username=self.username,
                            idUsername= self.idUsername, 
                            idBoard= self.idBoard, #id del board que se está jugando
                            state= 4, # derrota
                            time= self.timeNow, 
                            stack= self.stack
                )

            print("Regresar al menú principal")
        else:
            pass

    """
        Mantiene la funcionalidad de 'Pausar partida' y 'Reanudar partda'
        Detiene la partida del puzzle, 
        conlleva a que el tiempo se detiene, 
        se guarda el estado del tablero en la base de datos la base de datos
    """
    def __pauseGame(self):
        
        #Se ha presionado 'pausa'
        if self.pauseButton.cget('text') == "Pausa": 

            #Detiene el temporizador y actualiza el tiempo transcurrida en la partida
            self.pauseTime()
            #Actualiza el estado de la base de datos a 'pausa'
            self.__processPushPause()
            #Cambia el nombre del text en el button
            self.pauseButton.configure(text="Reanudar")

        #Se ha presionado 'Reanudar'
        else: 
            
            self.__updateTime()

            # Se obtiene el id del proceso after, con este id se procede a cancelar el proceso after
            self.afterId =  self.parent.after(1000, self.__timer)
            
            #Cambia el nombre del text en el button
            self.pauseButton.configure(text="Pausa")

        #self.game.pause = True


    """
        Detiene el temporizador y actualiza el tiempo transcurrida en la partida
    """
    def pauseTime(self) -> None: 
        
        self.timeNow = (ToolConnection()).formatTime(
                            hour=self.hours, 
                            minute=self.minutes, 
                            second=self.seconds
                    )

        print( self.timeNow )

        # Se cancela el evento after, El timer deja de funcionar
        self.parent.after_cancel(self.afterId)

    """
        Realiza la conexión y los procesos que implica
        internamente con la base de datos, a partir del botón 'Pausa'
        - Guarda el estado del tablero en la bd
        - Guarda el tiempo en pausa en la bd
        - Guarda la stack en la bd
        - Guarda undoStack en la bd
    """
    def __processPushPause(self): 
        

        self.pauseTime()
        
        #El juego termina y el estado del tablero cambia
        (ToolConnection()).updateGameBoard(
                        username=self.username,
                        idUsername= self.idUsername, 
                        idBoard= self.idBoard, #id del board que se está jugando


                        state= 2, #pausa
                        time= self.timeNow, 
                        stack= self.stack
            )
        

    """
        Realiza la conexión y los procesos que implica
        internamente con la base de datos, a partir del botón 'Reanudar'
    """
    def __processPushResume(self):
        pass
    
    """
        Asigna los valores de inicio de sesión del usuario 
        logeado (id, username)
    """        
    def getUsernameLogin(self):
        
        tool = ToolConnection()

        self.idUsername, self.username = tool.getLastLoginUser()

        self.idBoard = tool.getIdBoard(idUsername=self.idUsername)

        print( "username:{}, id: {}, idBoard: {}".format(
                self.username, 
                self.idUsername, 
                self.idBoard) 
            )


    """
        Última partida jugada
        Obtiene el estado de esa partida ('pausado', 'finalizado', 'derrota')
    """
    def getLastGamePlayed(self): 
        
        query = """
                SELECT 
                    id_user_fk AS id, 
                    blo_file AS stack,
                    tim_time AS time, 
                    cod_nameState AS state
                FROM 
                    Game 
                WHERE 
                    id_user_fk=%s
                ORDER BY 
                    id DESC
                LIMIT 1
                """
        
        transaction = self.db.select(query=query, data=(self.idUsername, ))
        self.db.closeConnection()

        return transaction

    """
        Actualiza el tiempo transcurrido de la partida 
        mediante la transición 'pausa'-'reanudar'
    """
    def __updateTime(self): 
        
        #hh:mm:ss 00:04:16 -> [0, 4, 16] 
        time = list(map(int, (self.timeNow).split( ":" ) ))
        

        self.hours = time[0]
        self.minutes = time[1]
        self.seconds = time[2]


    def __drawGrid(self):

        for i in range(10):
            color = "#6ea8d9" if i % 3 == 0 else "gray"
            x0 = MARGIN + i * SIDE - 20 # !Se restaron 20
            y0 = MARGIN
            x1 = MARGIN + i * SIDE - 20 # !Se restaron 20
            y1 = HEIGHT - MARGIN - 120 # !Se restaron 120
            # Lineas Verticales
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
            
            x0 = MARGIN - 20 # !Se restaron 20
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN - 20 # !Se restaron 20
            y1 = MARGIN + i * SIDE
            # Lineas Horizontales
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
    
    def __drawPuzzle(self):

        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.puzzle[i][j]
                if answer != 0:
                    x = MARGIN+ j * SIDE + SIDE / 2  - 20 # !Se restaron 20
                    y = MARGIN + i * SIDE + SIDE / 2
                    original = self.game.startPuzzle[i][j]
                    color = "white" if answer == original else "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )
        
    def __drawCursor(self):
            
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            #print(self.row, self.col)
            x0 = MARGIN + self.col * SIDE + 1 - 20 # ! Se restaron 20
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1 - 20 #! Se restaron 20
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            #print("coordenadas: ",x0,x1,y0,y1)
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )

    def __drawVictory(self):

        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="victory",
            fill="white", font=("Arial", 32)
        )

    def __cellClicked(self, event):

        if (self.game.gameOver):
            return

        if (self.game.pause):
            return

        x, y = event.x + 20, event.y # ! Se restaron 20 al evento x
        if (MARGIN  < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN - 120):
            self.canvas.focus_set()
            row, col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE
            #print(row, col)
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
                #print("posición2",row, col)
                #pass

            # ! Se comprueba si la posición del arreglo es igual a 0, esto significa que es una posición donde
            # ! el usuario debe introducir un valor, o sea, que es "seleccionable".
            # ! Si se cambia el chequeo de posiciones donde se puede escribir por un arreglo de booleanos 
            # ! donde True pertenezca a una posición donde se puede escribir, entonces se puede implementar
            # ! la acción de sobreescribir un cuadro que ya fue escrito por el usuario.
            # ?Si se usa un else pinta todos los cuadros incluidos los que estan definidos
            # ?por el archivo 
            elif self.game.puzzle[row][col] == 0:
                #print("posición3",row, col)
                self.row, self.col = row, col
                #pass
        """
        Setea a -1 (no se pinta el recuadro de selección) los valores de fila y columna
        else:
            self.row, self.col = -1, -1 
        """
        
        self.__drawCursor()
    
    def __keyPressed(self, event):
        
        #A ver de que lado masca la iguana
        print( self.game.gameOver )

        if (self.game.gameOver):
            print("Hola buenas tardes")
            #return
            
        if (self.row >= 0 and self.col >= 0 and event.char in "1234567890"):
            try:
                
                #Esta cosita pinta los numeritos en el puzzle
                self.game.puzzle[self.row][self.col] = int(event.char)

                #Agrega el par ordenado de coordenadas y el valor del número ingresado por el usuario a la pila
                self.stack.append( {"row":self.row, "col":self.col, "val": int(event.char), "state": 0} )
                print( self.stack )

            except:
                pass
            self.col, self.row = -1, -1
            self.__drawPuzzle()
            self.__drawCursor()
            if self.game.checkWin():
                self.__drawVictory()

    def __clearAnswers(self):
        self.game.start()
        self.canvas.delete("victory")
        self.__drawPuzzle()

    """
        Esta función retrocede un movimiento en el tablero, 
        dejando el valor inicial cero
    """
    def __undoMove(self):

        try:
            #Mientras existan elementos en la pila
            if len(self.stack):
                #Agrega el par ordenado de coordenadas y el valor del último número ingresado por el usuario
                self.undoStack.append( self.stack.pop() ) 
                #índice actual de la pila
                length = len(self.undoStack) - 1
                #Cambio de estado
                self.undoStack[length]['state'] = 1

                print( 
                        "stack:{}, row:{}, col:{}".format(
                            self.undoStack, 
                            self.undoStack[length]['row'],
                            self.undoStack[length]['col']
                            ) 
                    )
                
                #Esta cosita pinta los numeritos en el puzzle
                self.game.puzzle[ self.undoStack[length]['row'] ][ self.undoStack[length]['col']  ] = 0

        except:
            print("Un error ha ocurrido uwu")

        self.col, self.row = -1, -1
        self.__drawPuzzle()
        self.__drawCursor()
        if self.game.checkWin():
            self.__drawVictory()


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

            self.db.closeConnection() 
            self.parent.destroy()
            sys.exit()
            SudokuBye()
        else:
            pass

    
    # Fución encargada de pintar el tiempo de partida en pantalla
    def __timer(self):
        
        self.timer.set("{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds))
        self.labelTime.configure(text = self.timer.get())
        
        if (self.seconds <= 59):
            #time.sleep(1)
            self.seconds += 1

            if (self.minutes <= 59 and self.seconds == 59 + 1):
                self.minutes += 1

                if (self.minutes == 60 and self.seconds == 59 + 1 ):
                    self.hours += 1
                    self.minutes = 0
                    self.seconds = 0
        else:
            self.seconds = 0

        # Se obtiene el id del proceso after, con este id se procede a cancelar el proceso after
        self.afterId =  self.parent.after(1000, self.__timer)