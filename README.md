# Definición de Proyecto de Investigación y Desarrollo

## Definición de Proyecto


Crear un programa en Python3 que haga uso de Python/Tkinter y MariaDB/MySQL (en compatibilidad) para la implementación de base de datos sobre un juego de Sudoku. El código fuente y el funcionamiento del Sudoku lo extraerá del siguiente [enlace](http://newcoder.io/gui/part-4/) con las consideraciones siguientes:

- En el proyecto debe incluir el o los autores del componente Sudoku como un subcomponente de su documentación.
- El juego actual debe ser modificado de acuerdo con los requerimientos del proyecto.
- Este es el único código de Sudoku válido para el proyecto.


## Requerimientos del Proyecto

- El propósito del proyecto es hacer uso del código fuente hecho en Tkinter de Python2 y adaptarlo a Python3 usando conceptos de Base de Datos, modificando el código fuente del juego, donde:

    - El sistema debe incluir una ventana splash screen de bienvenida al iniciar el programa.

    - El sistema debe incluir una ventana de login. Sólo puede ingresar un usuario registrado en el sistema. Debe existir un usuario administrador previamente registrado en el sistema. Si el usuario administrador se autentica en el juego, éste debe disponer de una pantalla adicional para poder crear, eliminar y editar los datos de autenticación de usuarios (jugadores).

    - Una vez autenticado, el sistema debe mostrar una ventana de inicio donde el jugador puede retomar su último juego pausado, o puede iniciar un nuevo juego usando uno de los Boards disponibles (debe leer el sitio del juego para comprender algunos conceptos mencionados en los enunciados de este proyecto).

    - El sistema debe incluir una tabla en pantalla llamada tabla o tablero de score con los 10 mejores tiempos de los juegos exitosos del jugador autenticado, indicando sobre cuál Board, con cuál tiempo (formato HH:MM:SS) y sobre cuál fecha (formato YYYY/MM/DD HH:mm:SS) obtuvo dicho resultado. El equipo de desarrolladores decidirá dónde incrustar/llamar/mostrar dicho componente.

- El código original hace uso de ciertos tableros mediante archivos físicos con extensión “.sudoku”, los cuales deben migrarse y leerse desde la base de datos exclusivamente. 

- La configuración hacia las bases de datos se debe realizar mediante un archivo de texto llamado config.ini [(configparser)](https://docs.python.org/3/library/configparser.html) que debe ser parte de su proyecto. Con excepción de este archivo, todo el resto de componentes de datos se deben manejar desde la base de datos. El criterio que aplique el estudiante sobre estos conceptos será parte de la evaluación del proyecto.

- La ventana del juego de Sudoku debe incluir en algún lugar el tiempo de juego que lleva un jugador sobre el juego actual (formato HH:MM:SS). Si el jugador cierra la ventana o pausa/detiene el juego [mediante un botón destinado para ello], el sistema debe recordar el tiempo jugado y los datos registrados actuales del juego. A este estado se le llamará juego en espera, juego pausado o juego actual en progreso. Sólo puede haber un juego actual en progreso, por jugador. Cuando el jugador retome el juego pausado, el juego de mantener el mismo estado de cuando se pausó.

- La ventana del juego original incluye un botón “Clear Answers” el cual debe ser modificado para eliminar el último movimiento. Eliminar el último movimiento refiere a una cola de movimientos del jugador, de tal forma que dicho botón remueve el movimiento más reciente y por tanto posee la capacidad de borrar uno a uno los movimientos realizados por el jugador.

- Una vez completado un juego con éxito, el sistema debe registrar su completitud agregando el logro del jugador a su tablero de score personal. En este estado, el jugador ya no tiene un juego en espera.

- El jugador debe poder tener la opción de finalizar el juego actual como derrota, para iniciar un nuevo juego. Elegir un nuevo juego (eligiendo el mismo o un nuevo Board) deberá requerir confirmación del usuario (mediante una pantalla dialogbox) para marcar como derrota su juego en progreso (si es que existe un juego en espera) antes de iniciar su nuevo juego.

- Adicionalmente, los programadores de cada equipo de trabajo deberán agregarle al sistema un módulo de registro de bitácora que debe estar bajo la visualización del usuario administrador. El equipo de desarrolladores decidirá dónde incrustar/llamar/mostrar dicho componente.

    - El administrador debe poder ser capaz de crear jugadores, pero un usuario jugador no debe tener dicho privilegio de creación. Ambos roles de usuario, administrador y jugador, deben poder jugar Sudoku.

    - La bitácora deberá guardar todas las acciones del usuario, incluyendo, autenticación, inicio de un juego, acción dentro del juego, fin de un juego, pausa de un juego, visualización de tabla de resultados, y cualquier otra acción bajo el criterio de los programadores, incluyendo a todos los usuarios del sistema.

- Para evitar el uso de trampa, los datos de la base de datos debe encriptarse. El equipo de desarrolladores debe usar su criterio según todas las lecturas de la clase, y la libertad de investigación, para reconocer cómo y dónde se debe aplicar la encriptación en un sistema de base de datos. La encriptación debe ser manejada mediante SQL.

- Cada equipo de trabajo usará su conocimiento, criterio y experiencia en las prácticas de la clase, usando los temas de la Unidad 1 y de la Unidad 2, para decidir qué datos se deben registrar para cada ente/actor/relación de este sistema.

- Debe hacer uso obligatorio de vistas, triggers, funciones, procedimientos almacenados y tipos de datos multi-valor, junto con las técnicas de programación aprendidas a lo largo de toda la Unidad 2 para resolver su proyecto.

## Migración de Python2 a Python3

- El juego original se encuentra en versión Python2 y debe ser migrado a versión Python3, según lo definido en la Planificación Académica de la clase.

- El estudiante puede migrar el juego a Python3 haciendo una ejecución de juego y corrigiendo uno a uno los errores que le indique la consola.

    - Resolución error 1: Instalar Tkinter para Python3.

    - Resolución error 2: Hacer uso de range en lugar de xrange en los ciclos.

    - Resolución error 3: seguir la línea de código del error donde se indique que se está usando un índice flotante en lugar de un índice numérico, para aplicar un cast mediante int(...).

- Para ver cómo ejecutar el código, debe leer, copiar el código y seguir las indicaciones del enlace del proyecto.    
