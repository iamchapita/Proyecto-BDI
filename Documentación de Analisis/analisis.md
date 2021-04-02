# Análisis proyecto IS 510

## Lluvia de ideas

- Pantallas 
    
    
    - Splash: 
        Bienvenida o recibimiento al usuario 
        Logo y nombre del programa (*aun falta*)
    
    - Login 
        Ingreso del usuario 
        - nickname 
        - password 

    - Administrador 
        - Autentica la información de los usuarios:
            - Elimina 
            - Edita
            - crea 

        - Bitacora (pantalla)
            - Deberá ser obeservada solo por el administrador
                - Incluye información sobre los jugadores
                    - Ingreso al sistema
                    - Salida del sistema
                    - Inicio de una nueva partida en pausa
                    - Creación de una nueva partida
                    - Pausa  de una partida
                    - finalización (éxito)  de una partida
                    - Visualización de la tabla de resultados de cada jugador
                    - Acción del juego 
                        - Ingreso de un resultado al canvas
                        - Deshacer jugada
                    - Marcar como derrota (finalizar partida. Botón falso de finalizar partida)
                    - Todas las partidas jugadas por cada usuario
                        - éxito
                        - derrota

    - Menú (nombre del usuario)
        -  Pantalla de inicio que incluye la configuración del juego a nivel del usuario 
            - Iniciar partida 
            - Continuar partida 
            - Score boards

    - Board 
        - El canvas del juego para iniciar una partida
        - Incluye: 
            - Nombre del usuario 
            - Tiempo transcurrido en partida por jugador
            - Botones: 
                - Pausa (almacena el tiempo y el estado actual del juego en el tablero, es decir los valores incluidos en cada matriz)
                    - Sea cual sea el caso el avance del juego actual se almacena en la base de datos.
                - Regresar o deshacer jugadada
                    - Cambiar el valor de la matriz, de esa jugada, a **cero**.
                        - Por cada vez que se *presione* el botón *deshacer* ese movimiento se debe almacenar en una *pila*, que se limpia cada vez que termina una partida.
                        - Cada vez que se pausa o guarda la partida, este arreglo debe ser almacenado en la base de datos.
                - Guardar partida
                
                - Sólo puede haber un juego actual en progreso, por jugador.
                    - Es decir solo puede existir un jugaor jugando una partida a la vez.
                
                - Independientemente *gane* o *pause* el usuario (completar la matriz) los archivos y estados del tablero (canvas) deben almacenarse en la base de datos (.sudoku)
                
                - Sí el usuario no pausa el juego e inicia una partida nueva, los movimientos hechos en la partida anterior que no hayan sido guardados de forma física (pulsando el botón *pausa*) no serán almacenados en la base de datos.

                - Derrota
                    - No guarda ningún avance del juego y se marca como derrota en el score
                    - Requiere confirmación del usuario 
                        - Desea continuar con el mismo tablero (se limpia toda la matriz)
                        - Inicia una nueva partida (un nuevo canvas)

    - Score 
        - Los puntajes (10) de los mejores tiempo *del jugador*. 
            - Tiempo 
            - Fecha 
        - Botón para ver la partida completa finalizada (para ver la chepia xD) **extra**
    
    


- El código original hace uso de ciertos tableros mediante archivos físicos con extensión “.sudoku”, los cuales deben migrarse y leerse desde la base de datos exclusivamente.
    - Generar un archivo .sudoku por cada partida (con el estado del tablero) que haga o relice el usuario.  Cada archivo generado debe almacenarse en la BD. 

- Archivo .init
    - Mantiene la configuración de la base de datos 
        - hostname
        - database (nombre)
        - port 
        - user
        - password

- El jugador termina la partido 
    - gameover
        - Pausado
    - finalizado con éxito
        - Se agrega a la tabla de **Score**
        - Se elimina la *pila* de respuestas

- Encriptar
    - Referencia para las operaciones de encriptación: 
        https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html
        - Los archivos .sudoku para evitar el plagio (AES256)
        - La contraseña para cada usuario (SHA1) 

- Migración de Python2 a Python3

- Metodología
    - Datos multivalor
    - Triggers
    - Procedimientos almacenados
    - Funciones
    - Vistas

- Nombre de Métodos, clases 
    - Inglés

## Entidades 

- Rol
- Puntuación
- Usuario
- Partida
- Bitácora 
- Tablero


## Entidades y atributos

- Login (hora y fecha, usuario)
- Rol (estado)
- Puntuación (nombre del jugador, tiempo invertido por partida)
- Usuario (nombre, contraseña)
- Partida (estado de la partida{finalizada, pausada, derrota}, archivo, pila, tiempo, fecha)
- Bitácora(Ingreso al sistema, 
        Salida del sistema, 
        Inicio de una nueva partida en pausa, 
        Creación de una nueva partida, 
        Pausa  de una partida, 
        finalización (éxito)  de una partida, 
        Acción del juego) 

