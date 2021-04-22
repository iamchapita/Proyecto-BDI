# -*- coding: utf-8 -*-
from tkinter import *

from core.EngineSQL.ConfigConnection import ConfigConnection
from core.EngineSQL.MySQLEngine import MySQLEngine
from core.EngineSQL.MySQLToolConnection import ToolConnection
from core.FileManipulation.EncryptDecrypt import EncryptDecryptSudokuFile
from core.ScreenCenter import ScreenCenter
from core.SudokuByeUI import SudokuBye
from core.SudokuGame import SudokuGame

# ! Se le sumaron 20 y se restaron 20 en los parámetros necesarios.
MARGIN = 70 
SIDE = 50
WIDTH = MARGIN * 2 + SIDE * 9
# !Se le sumaron 120 para ampliar de forma vertical la ventana
HEIGHT = MARGIN * 2 + SIDE * 9 +120 

class SudokuBoardUI(Frame):
    
    def __init__(self, parent, game, mainAdmin, mainUser, hours=0, minutes=0, seconds=0):
        self.mainAdmin = mainAdmin
        self.mainUser = mainUser
        self.parent = parent
        # Se captura el evento de cierre de una ventana y se ejecuta la función __onClosing.
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)
        self.game = game
        self.row = -1
        self.col = -1
        self.timeNow = "00:00:00" # Tiempo en pausa
        self.config = ConfigConnection() # Conexión al archivo de configuración
        self.db = MySQLEngine(self.config.getConfig()) # Conexión a la base de datos
        self.stack = [] # {row: , col: , val: , state: } Coordenadas del ingreso de los datos a la tabla
        self.undoStack = []  # {row: , col: , val: , state: } Coordenadas de las jugadas deshechas
        self.encryptDecrypt = EncryptDecryptSudokuFile( self.db ) # Encripta y desencripta los datos del tablero
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)
        self.username = "" 
        self.rol = ""
        self.idUsername = None
        self.idBoard = None # Numero del board seleccionado
        # Obtiene los datos del usuario que está loggeado
        self.getUsernameLogin()
        # Evalua el estado del último tablero jugado
        self.evaluateBoardStatus() 
        # Se inicializan los componentes gráficos
        self.__initUI()

    def __initUI(self):
        # Se importan las imagenes usadas en la ventana
        self.img = PhotoImage(file="core/images/help.png", master=self.parent)
        # Se establecen los valores de ancho y alto de la ventana
        self.localwidth = 760
        self.localheight = 545
        # Se establece el titulo de la ventana
        self.parent.title("Sudoku")
        # Se bloque la opción de cambiar de tamaño la ventana
        self.parent.resizable(FALSE, FALSE)
        # Se configura un color de background a la ventana
        self.parent.configure(background = "#171717")
        # Se establecen las dimensiones de la ventana
        self.parent.geometry("%dx%d" %(self.localwidth, self.localheight))
        # Se centra la ventana en pantalla
        center = ScreenCenter()
        center.center(self.parent, self.localwidth, self.localheight)
        # Se pinta la ventana
        self.pack(fill=BOTH)
        # Se crea el elemento canvas que sirve para pintar el tablero y su valores
        self.canvas = Canvas(self.parent, width=WIDTH, height=self.localheight)
        # Se configura el elemento canvas
        self.canvas.configure(background = "#171717")
        # Se pinta el elemento canvas
        self.canvas.pack(fill=BOTH, side=TOP)
        
        # Se crean labels para contener texto
        self.labelNameUser= Label(self.parent, text=self.username, font=("Lato",13))
        self.labelTime= Label(self.parent, text='00:00:00', font=("Lato",13))

        # Se configura el color el background y de la fuente
        self.labelNameUser.configure(background = "#171717", fg="white")
        self.labelTime.configure(background = "#171717", fg="white")

        # Se posiciona los labels en la ventana
        self.labelNameUser.pack()
        self.labelNameUser.place(x=50,y=20)
        self.labelTime.pack()
        self.labelTime.place(x=430,y=20)

        # Se inicializa un variable de texto haciendo uso de una clase de tkinter
        self.timer = StringVar()
    
        # Se establecen los botones y se configuran sus parámetros
        self.helpButton= Button(self.parent, image=self.img, command = self.__help)
        self.finishButton = Button(self.parent, text="Finalizar partida", bg="#6ea8d9", font=("Lato",15), height=2, width=13, command=self.__endGame)
        self.pauseButton = Button(self.parent, text="Pausa", bg="#6ea8d9", font=("Lato",15), height=2, width=13, command=self.__pauseGame)
        self.returnButton = Button(self.parent, text="Deshacer jugada", bg="#6ea8d9", font=("Lato",15), height=2, width=13, command=self.__undoMove)
        self.clearButton = Button(self.parent, text="Limpiar Tablero", bg="#6ea8d9", font=("Lato",15), height=2, width=13, command=self.__clearAnswers)

        # Se configura el botón de ayuda
        self.helpButton.configure(bg="#171717", borderwidth=0, highlightthickness=0)

        # Se posicionan lo botones en el espacio de la ventana
        self.helpButton.place(x=670, y=20)
        self.finishButton.place(x=540, y=250)
        self.pauseButton.place(x=540, y=320)
        self.returnButton.place(x=540, y=390)
        self.clearButton.place(x=540, y=460)
        
        # Se pintan las casillas del tablero
        self.__drawGrid()
        # Se pintan los valores del tablero
        self.__drawPuzzle()
        # Se maneja el evento de click sobre el tablero
        self.canvas.bind("<Button-1>", self.__cellClicked)
        # Se maneja el evento de tecla presionada
        self.canvas.bind("<Key>", self.__keyPressed)
        # Se inicializa el tiempo
        self.__timer()

    # Se llama cuando el usuario desea terminar la partida (como derrota)
    def __endGame(self):
        # Se muestra un mensaje de confirmanción 
        MsgBox = messagebox.askquestion ('Finalizar partida','¿Está seguro de finalizar la partida como derrota?',icon = 'warning')
        if MsgBox == 'yes':
            # Se pausa el tiempo
            self.pauseTime()
            
            # Confirma si el rol del usuario es de administrador
            if(self.rol==1):
                # Se destruye la ventana actual
                self.parent.destroy()
                # Se muestra la ventana principal del administrador
                self.mainAdmin.deiconify()

            # Confirma si el rol del usuario es de juagdor
            if(self.rol==0):
                # Destruye la ventana actual    
                self.parent.destroy()
                # Se muestra la ventana principal del Usuario        
                self.mainUser.deiconify()

            #El juego termina (derrota) y el estado del tablero cambia
            (ToolConnection()).updateGameBoard(
                            username=self.username,
                            idUsername= self.idUsername, 
                            idBoard= self.idBoard, #id del board que se está jugando
                            state= 4, # derrota
                            time= self.timeNow, 
                            stack= self.stack
                )
            
            #Cerrar conexión a la base de datos
            self.db.closeConnection()
            
        else:
            pass

    # Mantiene la funcionalidad de 'Pausar partida' y 'Reanudar partda'
    # Detiene la partida del puzzle, conlleva a que el tiempo se detiene, 
    # se guarda el estado del tablero en la base de datos la base de datos
    def __pauseGame(self):
        self.pauseButton.config(state="disabled")
        #Se ha presionado 'pausa'
        if self.pauseButton.cget('text') == "Pausa": 
            
            self.game.pause = True

            # Confirma si el rol del usuario es de administrador
            if(self.rol==1):
                # Se destruye la ventana actual
                self.after(105,self.parent.destroy)
                # Se muestra la ventana principal del administrador
                self.after(100,self.mainAdmin.deiconify)
            
            # Confirma si el rol del usuario es de juagdor
            if(self.rol==0):
                # Destruye la ventana actual
                self.after(105,self.parent.destroy)
                # Se muestra la ventana principal del Usuario
                self.after(100,self.mainUser.deiconify)
            
            #Detiene el temporizador y actualiza el tiempo transcurrida en la partida
            self.pauseTime()
            #Actualiza el estado de la base de datos a 'pausa'
            self.__processPushPause()
            #Cambia el nombre del text en el button
            #self.pauseButton.configure(text="Reanudar")

        #Se ha presionado 'Reanudar'
        else: 
            
            self.__updateTime()
            self.game.pause = False
            # Se obtiene el id del proceso after, con este id se procede a cancelar el proceso after
            self.afterId =  self.parent.after(1000, self.__timer)
            
            #Cambia el nombre del text en el button
            self.pauseButton.configure(text="Pausa")

    # Detiene el temporizador y actualiza el tiempo transcurrida en la partida
    def pauseTime(self) -> None: 
        
        # Obtienne los valores del tiempo(hora, minutos, segundos) y forma una cadena con formato de tiempo
        self.timeNow = (ToolConnection()).formatTime(
                            hour=self.hours, 
                            minute=self.minutes, 
                            second=self.seconds
                    )

        # Se cancela el evento after, El timer deja de funcionar
        self.parent.after_cancel(self.afterId)

    # Realiza la conexión y los procesos que implica internamente con la base de datos, a partir del botón 'Pausa'
    # - Guarda el estado del tablero en la bd
    # - Guarda el tiempo en pausa en la bd
    # - Guarda la stack en la bd
    # - Guarda undoStack en la bd
    def __processPushPause(self): 
        # Se pausa el tiempo
        self.pauseTime()
        
        #El juego termina y el estado del tablero cambia
        (ToolConnection()).updateGameBoard(
                        username=self.username,
                        idUsername= self.idUsername, 
                        idBoard= self.idBoard, # id del board que se está jugando
                        state= 2, # pausa
                        time= self.timeNow, 
                        stack= self.stack
            )
        
    # Asigna los valores de inicio de sesión del usuario logeado (id, username)
    def getUsernameLogin(self):
        
        tool = ToolConnection()

        self.idUsername, self.username, self.rol = tool.getLastLoginUser()

        self.idBoard = tool.getIdBoard(idUsername=self.idUsername)

    # Última partida jugada
    # Obtiene el estado de esa partida ('pausado', 'finalizado', 'derrota')
    def getLastGamePlayed(self) -> list: 

        # Se prepara la query  
        query = """
                SELECT 
                    Board.stack AS stack,
                    Board.time AS time,
                    State.cod_state AS state
                FROM 
                    State
                INNER JOIN 
                (
                    SELECT 
                        id,
                        id_user_fk AS user, 
                        blo_file AS stack,
                        tim_time AS time
                    FROM 
                        Game 
                    WHERE 
                        id_user_fk=%s
                    ORDER BY 
                        id DESC
                    LIMIT 1
                ) AS Board ON State.id_game_fk = Board.id
                ORDER BY 
                    State.tim_date DESC
                LIMIT 1;
                """

        # Se hace la consulta a la base de datos y se almacena en una variable
        transaction = self.db.select(query=query, data=(self.idUsername, ))

        # Se retorna el resultado de la consulta
        return transaction

    # Actualiza el tiempo transcurrido de la partida mediante la transición 'pausa'-'reanudar'
    def __updateTime(self): 
        # Se obtiene la cadena del tiempo y se separa usando : como delimitador 
        #hh:mm:ss 00:04:16 -> [0, 4, 16] 
        time = list(map(int, (self.timeNow).split( ":" ) ))
        # Se establece el valor de las variables con la posición que le corresponde
        self.hours = time[0]
        self.minutes = time[1]
        self.seconds = time[2]

    # Se pintan las casillas del tablero
    def __drawGrid(self):
        
        for i in range(10):
            # Se pintan los colores de las lineas
            color = "#6ea8d9" if i % 3 == 0 else "gray"
            # Se calculan las coordenadas
            x0 = MARGIN + i * SIDE - 20 # !Se restaron 20
            y0 = MARGIN
            x1 = MARGIN + i * SIDE - 20 # !Se restaron 20
            y1 = HEIGHT - MARGIN - 120 # !Se restaron 120
            # Corresponde a las lineas Verticales
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
            # Se calculan las coordenadas
            x0 = MARGIN - 20 # !Se restaron 20
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN - 20 # !Se restaron 20
            y1 = MARGIN + i * SIDE
            # Corresponde a las lineas Horizontales
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
    
    # Se pintan los números en el tablero, tanto los números "originales" como los números
    # que introduzca el jugador
    def __drawPuzzle(self):
        
        # Borra los números del tablero
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
    
    # Pinta un recuadro rojo sobre la casilla seleccionada en el tablero
    def __drawCursor(self):
        
        # Borra el recuadro rojo si está pintado en otra casilla del tablero
        self.canvas.delete("cursor")

        # Obtiene la fla y columna donde se clickeo (se va a pintar el recuadro rojo)
        if self.row >= 0 and self.col >= 0:
            
            # Calcula las coordenadas dónde se va a pintar el recuadro rojo
            x0 = MARGIN + self.col * SIDE + 1 - 20 # ! Se restaron 20
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1 - 20 #! Se restaron 20
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            
            # Pinta el recuadro rojo
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )

    # Pinta un aviso de que la partida se ganó
    def __drawVictory(self):
        # Pausa el contador de tiempo

        self.pauseTime()
        # Se definen la coordenadas donde se va a pintar el aviso de ganado
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7

        # Se pinta el aviso
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        # Se crea el texto que va dentro del aviso de partida ganada
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="victory",
            fill="white", font=("Arial", 32)
        )
        
        # Se deshabilitan los botones 
        self.clearButton.config(state="disabled")
        self.pauseButton.config(state="disabled")
        self.returnButton.config(state="disabled")
        self.returnButton.config(state="disabled")
        self.finishButton.config(state="disabled")

        #El juego termina (finalizado) y el estado del tablero cambia
        (ToolConnection()).updateGameBoard(
                        username=self.username,
                        idUsername= self.idUsername, 
                        idBoard= self.idBoard, # id del board que se está jugando
                        state= 3, # finalizado
                        time= self.timeNow, 
                        stack= self.stack
            )
        
        #Cerrar conexión a la base de datos
        self.db.closeConnection()
        
        # Se decide que pantalla se va a mostrar después de ganar la partida
        if(self.rol==1):
            # Se destruye la ventana actual
            self.after(105,self.parent.destroy)
            # Se muestra la ventana principal del administrador
            self.after(100,self.mainAdmin.deiconify)

        if(self.rol==0):
            # Se destruye la ventana actual
            self.after(105,self.parent.destroy)
            # Se muestra la ventana principal del usuario jugador
            self.after(100,self.mainUser.deiconify)
    
    # Maneja el evento de click sobre el tablero
    def __cellClicked(self, event):

        if (self.game.gameOver):
            return

        if (self.game.pause):
            return

        # Obtiene las coordenadas de donde se hizo click
        x, y = event.x + 20, event.y # ! Se restaron 20 al evento x
        # Comprueba que las coordenadas esten dentro del tablero
        if (MARGIN  < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN - 120):
            # Establece el foco al canvas, que es el contenedor del tablero
            self.canvas.focus_set()
            # Obtiene la fila y columna donde se hizo click
            row, col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE
            # Si se clickeo sobre una casilla que ya estaba "enfocada"
            if (row, col) == (self.row, self.col):
                # Se borra el enfoque
                # Simula la acción de seleccionar y deseleccionar
                self.row, self.col = -1, -1
                # Se establecen los valores de la columna y de la fila de forma que se puedan leer por
                # la función __drawCursor
            elif self.game.puzzle[row][col] == 0:
                self.row, self.col = row, col
        
        # Se llama la función para pintar el recuadro rojo sobre la casilla clickeada
        self.__drawCursor()

    
    # Evalua sí el estado del tablero es 'continuar'. 
    # De ser así carga las jugadas de la base de datos al tablero por medio de la pila (stack)
    # @transaction: [(stack, time, state)]
    def evaluateBoardStatus(self) -> None:
        
        transaction = self.getLastGamePlayed()[0]

        if transaction: 
            
            blo_file, self.timeNow, state = transaction

            #Evalua sí el tablero cumple con la condición al haber presionado el botón 'Continuar juego' 
            if state == 'continuar':
                
                self.stack = eval( self.encryptDecrypt.decrypt(encryptData=blo_file, password=self.username) )

                for json in self.stack: 
                    # Pinta los numeritos en el puzzle
                    self.game.puzzle[ json['row'] ][ json['col'] ] = json['val']
    
    # Maneja el evento de tecla presionada
    # Se usa para pintar el número en el tablero
    def __keyPressed(self, event):
        
        # Se comprueba que los valores de la columna y fila no sean 0
        # Se comprueba que la tecla presionada sea un número
        if (self.row >= 0 and self.col >= 0 and event.char in "1234567890"):
            try:        
                # Pinta los numeritos en el puzzle
                self.game.puzzle[self.row][self.col] = int(event.char)

                # Agrega el par ordenado de coordenadas y el valor del número ingresado por el usuario a la pila
                self.stack.append( {"row":self.row, "col":self.col, "val": int(event.char), "state": 0} )

            except:
                pass
            # Se establece valores para la columna y fila de forma que se la casilla seleccionada
            # ya no lo este más
            self.col, self.row = -1, -1
            # Se pintan los números en el tablero
            self.__drawPuzzle()
            # Se pinta el recuadro rojo en el tablero (o se elmina)
            self.__drawCursor()
            # Se comprueba si el tablero está lleno de forma correcta para marcar victoria
            if self.game.checkWin():
                # Se muestra el aviso de partida ganada
                self.__drawVictory()

    # Elimina todos los valores que introdujo el usuario en el tablero
    def __clearAnswers(self):
        # Elimina los valores introducidos en el arreglo
        self.game.start()
        # Se pinta de nuevo los valores del tablero
        self.__drawPuzzle()

    # Esta función retrocede un movimiento en el tablero, dejando el valor inicial cero
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
                #Esta cosita pinta los numeritos en el puzzle
                self.game.puzzle[ self.undoStack[length]['row'] ][ self.undoStack[length]['col']  ] = 0
        except:
            pass
        
        # Se establecen las variables de forma que no haya ningún recuadro seleccionado en pantalla
        self.col, self.row = -1, -1
        # Se pintan los números del tablero
        self.__drawPuzzle()
        # Se pinta el recuadro rojo que indica que un cuadro está seleccionado
        self.__drawCursor()
        # Si cumple la condición el juego se finaliza con éxito (tablero lleno correctamente)
        if self.game.checkWin():
            # Se muestra que la  partida se ganó
            self.__drawVictory()

    # Función que pregunta al usuario si desea salir del juego.
    def __onClosing(self):
        MsgBox = messagebox.askquestion ('Salir','¿Estás seguro de que quieres salir?',icon = 'warning')
        if MsgBox == 'yes':
            
            #Se ingresa a la base de datos la información del usuario que cierra sesión
            (ToolConnection()).logout()
            # Se cierra la conexión a la Base de datos
            self.db.closeConnection() 
            # Destruye la ventana actual
            self.parent.destroy()
            # Cierra la ejecución del programa
            sys.exit()
            # Muestra la ventana de despedida
            SudokuBye()
        else:
            pass

    # Fución encargada de pintar el tiempo de partida en pantalla
    def __timer(self):
        
        # Se establece el contenido de la variable
        self.timer.set("{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds))
        # Se pinta el tiempo en la pantalla
        self.labelTime.configure(text = self.timer.get())
        
        if (self.seconds <= 59):
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

    # Se muestra un messageBox de ayuda, que contiene las reglas del juego.
    def __help(self):
        messagebox.showinfo(message="Regla 1: Hay que completar las casillas vacías con un solo número del 1 al 9. \nRegla 2: En una misma fila no puede haber números repetidos. \nRegla 3: En una misma columna no puede haber números repetidos. \nRegla 4: En una misma región no puede haber números repetidos. \nRegla 5: La solución de un sudoku es única.", title="Instrucciones juego")
