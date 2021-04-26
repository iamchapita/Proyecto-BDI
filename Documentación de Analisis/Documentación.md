    Universidad Nacional Autónoma de Honduras (UNAH)
    I PAC 2021   
    Clase: Bases de Datos I
    Sección: 0700
    Catedrático: José Manuel Inestroza Murillo
    Alumnos:  Daniel Alessandro Arteaga Martínez    -   20161000031
              Luis Alejandro Morales Zelaya         -   20161930074
              Gabriela Emperatriz Hernández Cortés  -   20161003982
              Kenneth Leonel Cruz Ordoñez           -   20141010391

# **Proyecto Final - Documentación (Análisis e Investigación)**

## **Índice**

- [**Proyecto Final - Documentación (Análisis e Investigación)**](#proyecto-final---documentación-análisis-e-investigación)
  - [**Índice**](#índice)
  - [**Lluvia de Ideas**](#lluvia-de-ideas)
  - [**Diseño de Ventanas y sus Funciones**](#diseño-de-ventanas-y-sus-funciones)
      - [**Ventanas compartidas entre usuario normal y administrador**](#Ventanas-compartidas-entre-usuario-normal-y-administrador)
        - [*Ventana de Bienvenida*](#ventana-de-bienvenida)
        - [*Ventana de Login*](#Ventana-de-Login)
        - [*Ventana de Despedida*](#Ventana-de-Despedida)
        - [*Ventana del Juego*](#Ventana-del-Juego)
      - [**Ventanas de Administrador**](#Ventanas-de-Administrador)
        - [*Ventana de Opciones de Administrador*](#Ventana-de-Opciones-de-Administrador)
        - [*Ventana de Administración de Usuarios*](#Ventana-de-Administración-de-Usuarios)
        - [*Ventana para crear un nuevo usuario*](#Ventana-para-crear-un-nuevo-usuario)
        - [*Ventana de Lista de Usuarios*](#Ventana-de-Lista-de-Usuarios)
        - [*Ventana de Bitacora*](#Ventana-de-Bitacora)
      - [**Ventanas de Jugador**](#Ventanas-de-Jugador)
        - [*Ventana de cambio de contraseña*](#Ventana-de-cambio-de-contraseña)
        - [*Ventana Menu*](#Ventana-Menu)
        - [*Ventana Scoreboard*](#Ventana-Scoreboard)
  
  - [**Diseño de Base de datos: *SudokuBD***](#diseño-de-base-de-datos-sudokuBD)
    - [**Reglas de negocio**](#reglas-de-negocio)
    - [**Esquema conceptual**](#esquema-conceptual)
      - [*Modelo Entidad Relación*](#modelo-entidad-relación)
      - [*Modelo relacional*](#modelo-relacional)
    - [**Esquema Lógico**](#esquema-lógico)
      - [*Entidades, atributos y dominio*](#entidades-atributos-y-dominio)
      - [*Vistas*](#vistas)
      - [*Funciones*](#funciones)
      - [*Disparadores*](#disparadores)
      - [*Procedimientos Almacenados*](#procedimientos-almacenados)
    - [**Encriptación: Funciones Built-in**](#encriptación-funciones-Built-in)
    - [**Anotaciones finales**](#anotaciones-finales)

  - [**Elementos Conceptuales**](#elementos-conceptuales)
    - [**Tkinter**](#tkinter)
    - [**MySQL Connector**](#mysql-connector)
  - [**Código Fuente de Sudoku Game**](#Código-Fuente-de-Sudoku-Game)
  - [**Actividades**](#actividades)
    - [**Actividad #1**](#Actividad-#1)
    - [**Actividad #2**](#Actividad-#2)
    - [**Actividad #3**](#Actividad-#3)
    - [**Actividad #4**](#-Actividad-#4)
    - [**Actividad #5**](#Actividad-#5)
  - [**NOTAS Y BIBLIOGRÍAS**](#notas-y-bibliogrías)

## **Lluvia de Ideas**

-----

### **Modelados ER y Diagramas ER**

A continuación se presentan los diagramas y modelados para la base de datos.

# **Diseño de Ventanas y sus Funciones**



## **Ventanas compartidas entre usuario normal y administrador**

-----

### *Ventana de Bienvenida*

En esta venta se muestra el logo creado por el equipo. Esta ventana es un splash screen lo cual durara unos segundos para que el usuario la visualice y luego se muestre la ventana de login.

![Splash Screen](https://drive.google.com/uc?export=view&id=1k4j5U8wvhlV4IxfxGDRndm-O6mqkFrlJ "Splash Screen")

### *Ventana de Login*

En esta ventana se le presenta al usuario la ventana donde se requiere su usuario y contraseña para acceder al juego.

![Login Screen](https://drive.google.com/uc?export=view&id=1UgFkapL9M-sxbb3_eN0bMnSvqDbJd435 "Login Screen")

### *Ventana de Despedida*

En esta ventana presenta un pequeño mensaje de despedida que dura unos cuantos segundos para luego cerrar por completo el juego.

![Bye Screen](https://drive.google.com/uc?export=view&id=1YJHSz9ZyZBaSuMXcqy4DjMx7_cB0UXCn "Bye Screen")

### *Ventana del Juego*

En esta ventana se presenta el juego Sudoku donde se tienen las opciones de pausar, deshacer jugada, limpiar tablero y finalizar partida(derrota)

![Bye Screen](https://drive.google.com/uc?export=view&id=1qXeSlxs3qKBiUQJuJwT0QqI_RL3iK_Nf "Bye Screen")

-----

## **Ventanas de Administrador**

-----

### *Ventana de Opciones de Administrador*

En esta ventada se le presenta al administrador todas las opciones que puede usar dentro del juego.

![Admin Main Screen](https://drive.google.com/uc?export=view&id=1itF9gintKQSdnFd94SNs8ZW5KCnWXKCZ "Admin Main Screen")

### *Ventana de Administración de Usuarios*

En esta ventana se muestra todas las acciones que el administrador puede hacer en cuanto a los usuarios registrados en el juego.

![User Administration Screen](https://drive.google.com/uc?export=view&id=1wvUq0OBLoZzUDvjyo3nkaGicaz2ucyD9 "User Administration Screen")

### *Ventana para crear un nuevo usuario*

En esta ventana se puede crear un usuario para que pueda acceder al juego, este mismo tendra como contraseña su nombre de usuario.

![Create User Screen](https://drive.google.com/uc?export=view&id=1WpUaEG8dfDJ87vHZZO2o0G9Z8xs3jzvZ "Create User Screen")

### *Ventana de Lista de Usuarios*

En esta ventana se muestra un tree view en donde salen todos los usuarios registrados en el juego, asi mismo se puede modificar su usuario, contraseña y dar de baja o rehabilitar un usuario.

![User List Screen](https://drive.google.com/uc?export=view&id=1HM9k7Mr0Pp7W1qcXfIDil5JdzYmyAq8t "User List Screen")

### *Ventana de Bitacora*

En esta ventana se mostrara los registros tanto de el administrador como otro jugador y corriente de todo lo que han hecho dentro de juego (login, logout, etc..)

![Binnacle Screen](https://drive.google.com/uc?export=view&id=1_88QxFxJ7PqZlskHwzMXzHNiwAasMhBJ "Binnacle Screen")

-----

## **Ventanas de Jugador**

-----

### *Ventana de cambio de contraseña*

Cuando el administrador crea un usuario este mismo tiene como contraseña su mismo usuario como fue mencionado unos pasos arriba, esta ventana hace que el usuario pueda cambiar su contraseña a lo que desee.

![Change Password Screen](https://drive.google.com/uc?export=view&id=1TEkclQnTKItVLD3U2ITEwbL_wxibqWvq "Change Password Screen")

### *Ventana Menu*

En esta ventana se le muestra el menu al jugador donde tiene las opciones de empezar un nuevo juego, continuar un juego (si ya inicio uno y si se le dio pausa), mejores puntajes y salir.

![Menu Screen](https://drive.google.com/uc?export=view&id=1gJUpsfi_1bKXHwhIpwfTmzpH6FOgnfmb "Menu Screen")

### *Ventana Scoreboard*

En esta ventada se registran los 10 mejores puntajes por cualquier usuario registrado en el juego, asi mismo se muestran de forma ascendente.

![Scoreboard Screen](https://drive.google.com/uc?export=view&id=12W8JcXi60YtDOfWGlGajdW4djzZnP8n5 "Scoreboard Screen")

-----

# **Diseño de Base de datos: SudokuBD**

La permanencia de los datos en el mundo globalizado es una necesidad en su posteridad para realizar en algún momento en el tiempo un análisis de estos, Elmasri en su libro *Fundamentals of Database System* menciona que una base de datos es un conjunto de datos convexos. 
El objetivo de un sistema de almacen de datos es la permanencia y el procesos de dichos datos para una conversión en información. 
Datos proviene del latin *datum* siendo este singular, el primer uso conocido es por el doctor Henry Hammond en el siglo XVII hace uso de esta palabra en un tratado religioso, sin embargo en un conexto fuera del uso de la época moderna. 

En un paper de elaboración propia de la empresa IBM, indica que cerca de 2.5 exabyte (Eb) de datos se generan cada día. Toda esta ingesta cantidad de datos deben de parar en algún sitio y es aquí donde las bondades de las bases de datos se ven reflejadas.

En la presente [sección](#diseño-de-Base-de-datos-SudokuBD) de este documento se plantean respuestas al análisis realizado ( corresponde con las reglas de negocio), se da respuesta al porqué del uso y diseño de esta base de datos (Sudoku), utilizando los criterio de desarrollo, análisis e implementación del equipo de desarrollo para dar solución al problema planteado. Se explica de forma explicita apegada a la teoría y fundamentos los distintos tipos de esquemas, las distintas versiones y cambios en la estructura del diseño que dio paso a la versión final y en producción del proyecto.

Dentro de los requerimientos y documentación pertenecientes a la clase de Base de Datos I (IS501) el SGMB ha utilizar es *MariaDB 10.0.3 en compatibilidad con MySQL 5.7*

En primera instancia se aborda la definición del proyecto y los puntos claves que dieron paso al análisis y a la posterior elaboración del diseño lógico.

## **Reglas de negocio**
Es de suma importancia identificar las reglas de negocio al diseñar una base de datos, estas permiten a los desarrolladores comprender las relaciones entre las entidades participantes.

Algunas de estas reglas se enunian a continuación: 

- Inicio de una nueva partida en pausa

- El usuario puede: 
  - Crear una nueva partida
  - Pausar juego
  - Continuar partida (significa que el usuario puede *pausar* el juego en cualquier momento)
  - Finalizar partida (rendirse)

- Visualizar tabla de resultados

- Acción del juego 
    - Ingresar un digito al puzzle
    - Deshacer la jugada

- Todas las partidas jugadas por un usuario se marcan:
    - éxito (ganó)
    - derrota (perdió)

- Administrador 
  - Elimina un usuario
  - Edita (nombre, contraseña) de un usuario
  - Crea a un usuario

Para una mayor profundidad en la especificación de las regla de negocio para este proyecto, se encuentra en el documento *Análisis.md* dentro de la carpeta *Documentación y análsis*.
Queda claro que se debe utilizar una plataforma con GUI para la inserción de los datos, que funge como interfaz o mediador entre la base de datos y el usuario.
## **Esquema conceptual**
Una vez recopilados y analizados los requisitos, el siguiente paso es crear un esquema conceptual para la base de datos.
Gracias a este enfoque los desarrolladores del equipo pueden centrarse en especificar las propiedades de los datos, sin preocuparse por detalles de almacenamiento e implementación. 

Este esquema es de gran utilidad para una revisión detallada de cambios en el futuro dentro del sistema, en este caso ha sido una guía infalible para detectar redundancia e inconsistencias.

### *Modelo Entidad Relación*

En este apartado se ilustra el resultado del análisis realizado en el paso anterior, evocando un seguimiento en el tiempo de la evolución de los cambios según la necesidad, cambios y ajustes de optimización.  
Se enuncian y explican las entidades y los atributos asociados a cada entidad.  
El dominio y tipos de datos se explica en otro apartado.

<br>

- **Primera versión: ER**
![Modelo ER ver_1](https://drive.google.com/uc?id=1HyN1FRGfCrC-jqtZWEYjpf5Tc0eivuRg)


<br>

Se enuncia una lista de entidades con atributos y entidades

| Entidad | Atributos                                                   | Relación                                      |
|---------|-------------------------------------------------------------|-----------------------------------------------|
| Login   | - id  <br> - date                                           | log                                           |
| User    | - id  <br> - nickname <br> - password <br> - rol            | - log <br> - getout <br> - play <br> - record |
| LogOff  | - id  <br> - date                                           | - Getout                                      |
| Game    | - id  <br> - file  <br> - nameState <br> - time <br> - date | - play <br> - push                            |
| Action  | - id  <br> - number                                         | - push                                        |
| Binacle | - id  <br> - date                                           | - record                                      |
##### Tabla 4.1.1

<br>
<br>

#### **Aclaración**:   
Dado que los cambios en cada versión de este modelo son minímos solo se hará mención de esta [aclaración](#aclaración) *una sola vez* a lo largo del documento, a partir de aquí solo los cambios o eliminaciones de los atributos o entidades se ilustraran en una tabla similar a la [anterior](#tabla-4.1), de igual forma se hará una breve explicación de los cambios. 

<br>
<br>

- **i. Explicación: entidades**  
  - Login:  
    El objetivo de esta entidad es identificar al usuario que ingresa al sistema.
    Está entidad mantiene la información de acceso al sistema de un usuario. 
  
    <br>

  - User:  
    Esta entidad es una de las más importantes dentro del sistema dado que es donde se relacionan las demás entidades, en esta se mantiene la información del usuario, se mantiene el nombre del usuario, los análistas han determinado que el **nombre del usuario** sea único, este hecho facilita la identificación del usuario para la actualización de cualquier dato relacionado con este. Ello implica eliminación o actualización de sus acciones en el tablero.
    
    <br>

  - LogOff:  
    Las reglas de negocio indican que *cualquier acción* por parte del usuario en la interacción con el sistema debe verse reflejado en la persistencia de los datos; esta entidad mantiene la información de cierre de sesión. 
    
    <br>

  - Game:  
    Aparte de mantener los datos del usuario, es necesario mantener los datos pertenecientes a cada tablero. En este caso, los elementos pertenecientes al tablero de juego se almacenan aquí. 
    Existe un archivo .sudoku donde se carga el tablero inicial (este ideal cambia a lo largo de las versiones).
  
    <br>

  - Action:  
    Está entidad almacena las componentes (x, y) junto con el número digitado por el usuario en el tablero. Dado que un usuario querrá *deshacer una jugada*.

    <br>

  - Binacle:  
    Bitácora del sistema, esta entidad mantiene la información de las acciones del usuario.

- **ii. Explicación: atributos**   
  - Login(id, date)  
    (*id*): Identificador único que asocia cada tupla.  
    (*date*): Almacenamos la fecha y hora del momento exacto en el que el registro es insertado, es decir en el momento en el que el usuario ingresa al sistema.

    <br>

  - User(id, nickname, password, rol)
    (*id*): Identificador único que asocia cada tupla.  
    (*nickname*): Nombre del usuario (este nombre es único e irrepetible).  
    (*password*): Contraseña del usuario para el ingreso al sistema.  
    (*rol*): Este es un tipo multivalor, existen dos tipos de usaurios en el sistema, *administrador* y *usuario*, cada uno de estos roles realiza actividades y acciones diferentes dentro del sistema; este apartado se encuentra definido y especificado en las reglas de negocio.

    <br>

  - LogOff(id, date)  
    Similar a la entidad *Login*, en este aspecto el registro corresponde a la salida del usuario del sistema.

    <br>

  - Game(id, file, nameState, time, date)  
    (*id*): Identificador único que asocia cada tupla.  
    (*file*): 
    (*time*): Minutos jugados del tablero escogido.
    (*date*): Fecha y hora del momento en el que un usuario crea un nuevo tablero.

    <br>

  - Action(id, state, number)
    (*id*): Identificador único que asocia cada tupla.  
    (*state*): El estado se encuentra en la dirección asociada a *(0) deshacer jugada*, *(1) continuar jugada*, esto con el motivo de conocer el resultado de cada componente del resultado digitado.  
    (*number*): Almacena cada resultado digitado por el usuario en el tablero.
    
    <br>

  - Binacle(id, date)  
    En el momento de la creación del modelo **Entidad relación** la estructura e integración de la entidad *Bitácora* no era del todo claro, así que de manera volátil y poco estructurada se encontraba como una *idea* no implementada pero necesaria para la realización del proyecto. Sin embargo la forma de integración se encontrase de manera similar a las entidades *Login* y *LogOff*.

<br>

- **Segunda versión: ER**
![Modelo ER ver_2](https://drive.google.com/uc?id=1fqVTp0AzY3Wj-Jagt9DALlzg3tNuLmEj)

<br>


Elevar la experiencia de usuario no es un requerimiento de las reglas de negocio sin embargo elevar esta connotación a un nivel retante y no estático da cierto dinamismo al proyecto, utilizando las bondades que ofrece el almacenamiento de las base de datos relacionales, la idea se encuentra dirigida a mantener *distintos tipos de tableros* con distintos niveles, cada tablero es único y se carga de forma automática al iniciar un nuevo juego por parte del usuario o administrador esto gracias a un archivo dentro del sistema con extensión *.sudoku*.  

Se enuncia una lista de entidades con atributos y entidades. Tomando en consideración la [aclaración](#aclaración) anterior.   

<br>


| Entidad     | Atributos         | Relación |
|-------------|-------------------|----------|
| SudokuBoard | - id <br> - board |          |
##### Tabla 4.1.2

<br>
<br>

- **i. Explicación: entidades**  
  - Sudoku:  
    Contiene *la numeración inicial* de algunos números ya dispuestos en algunas de las celdas de cada tablero al iniciar una partida. Esta numeración es fija, inmutable, única y persistente.

- **ii. Explicación: atributos**   
  - Sudoku(id, board)  
    (*id*): Identificador único que asocia cada tupla.  
    (*board*): Númeración fija correspondiente para cada tablero.  

<br>

- **Tercera versión: ER**
![Modelo ER ver_3](https://drive.google.com/uc?id=1sx4Bx6fY7fHqjjL5aj4murw66mFvIZ2B)


<br>

Tercera modificación del modelo entidad relación, la permanencia del equipo de desarrollo y las constantes reuniones empujan las ideas a una construcción más clara del proyecto. 
La integración de la entidad SudokuBoard con el resto de entidades es necesaria, al igual que una independencia del estado del tablero, dado que los estados de un tablero son multiples, adicionalmente a esto un usuario puede querer jugar distintos tableros (creación de nuevos juegos), a partir de aquí nace la necesidad de convertir un atributo multivalor en una entidad con sus propios atributos asociados a la entidad *Game*.  

Se enuncia una lista de entidades con atributos y entidades. Tomando en consideración la [aclaración](#aclaración) que se encuentra en la descripción de esta sección.    

<br>

| Entidad     | Atributos                                | Relación                                   |
|-------------|------------------------------------------|--------------------------------------------|
| SudokuBoard | - id <br> - board                        | - Have (agrega)                            |
| Game        | - state (elimina)                        | - Have (agrega) <br> - Have  (agrega)      |
| State       | - id <br> - nameState <br> - date        | - Have                                     |
##### Tabla 4.1.3

<br>
<br>

- **i. Explicación: entidades**  
  - SudokuBoard:  
    La integración con el resto de entidades es necesaria para la recuperación de los datos contenidos en esta entidad, estos datos se encuentran relacionados con el usuario, luego de un análisis más profundo, dado que el usuario puede requerir el uso de *otro* tablero con cierta dificultad o complejidad mayor dada sus habilidades y destrezas en el juego.  
    En resumen: se toma en cuenta los tableros que el jugador desea jugar.


  <br>

  - Game:  
    Necesidad de eliminar el atributo multivalor *state*

  <br>

  - State:  
    Esta entidad mantiene los cambio de estado, este hecho se ve reflejado por las acciones que realiza un usuario.  

  <br>


- **ii. Explicación: atributos**   
    Se prescinde realizar explicación del resto de entidades, queda claro la eliminiación de atributos e integración de estas relaciones con el resto de componentes de la base de datos. 
    
  - State(id, nameState, date)  
    (*id*): Identificador único que asocia cada tupla.  
    (*nameState*): Contiene los estados *nuevo*, *pausado*, *finalizado*, *derrota*, *continuar*, depende la acción que el usuario realice se toma una u otro dato contenido en este atributo, estos estados son *autodescriptivos*, hemos mencionado a lo largo del documentos su importancia.  
    *nuevo* refierase a la creación de un nuevo tablero; *finalizado* significa que el usuario ha completado con éxito un tablero, de esta forma ganando.  
    (*date*): Fecha y hora del momento en el que un usuario realiza una acción, este se ve reflejado como un **nuevo estado**.


<br>


- **Versión final: ER**
![Modelo ER ver_5](https://drive.google.com/uc?id=12GCMW9eEoZq7eN4WdT5Xwxky4RStNay6)



<br>

Versión final y en permanencia del esquema conceptual perteneciente a este proyecto. Se implementa la integración de componentes que son necesarios para el funcionamiento del proyecto, de igual forma se elimina entidades que no cumplen un rol determinante, ocupando almacenamiento de forma innecesaria.  
La explicación de **cardinalidad** para este modelo se explica en esta sección, se ha hecho de esta forma dado que las relaciones no han cambiado en demasia a lo largo del proyecto y versiones, así evitamos redundancia en las explicaciones.

Se enuncia una lista de entidades con atributos y entidades. Tomando en consideración la [aclaración](#aclaración) que se encuentra en la descripción de esta sección.   

<br>

| Entidad          | Atributos                                        | Relación           |
|------------------|--------------------------------------------------|--------------------|
| User             | - state (agrega)                                 |                    |
| Binacle          | - nickname (agrega) <br> - description (agrega)  | - Record (elimina) |
| Action (elimina) |                                                  |                    |
##### Tabla 4.1.4

<br>
<br>

- **i. Explicación: entidades**  
  - Binacle  
    Semanas posteriores al análisis inicial y luego de reiteradas lecturas con respecto a las reglas de negocio se visualizó con mayor claridad la implementación de esta entidad. Es necesario almacenar acciones y estados asociados a un usuario. Sin embargo la visualización de estos datos es perteneciente a un único usuario **administrador**.  

  <br>
  
  - Action (eliminación)   
    El proyecto prescinde de la implementación de esta entidad, los atributos modelados estan contenidos en la entidad **Game**, para este caso evitamos la redundancia de datos gracias a la normalización.  

- **ii. Explicación: atributos**   
  - User(state)  
    (*state*): La eliminación de usuarios no es una practica de programación deseable para este proyecto, considerando lo anterior se ha incluido este atributo, el estado del usuario dentro del sistema puede ser: **activo** **inactivo**. Evitamos fuga o agujeros de información en nuestro sistema. 
    Dar de baja a los usuarios, de esta forma se evita eliminar a los usuarios de forma explícita de la base de datos.

  <br>

  - Binacle(nickname, description)  
    (*nickname*): Almacena el nombre del usuario (junto a un conjunto de características incluidas en esta entidad) cada vez que este realiza una acción en el sistema.  
    (*description*): Descripción de la acción que realiza un usuario, explicación detallada de la acción.

- **iii. Explicación: cardinalidad**   

  | Entidad     | Relación                            | Explicación                                                                                                                                 |
  |-------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
  | Login       | - log                               | - Un usuario puede tener una única sesión iniciada                                                                                          |
  | User        | - log <br> - Getout <br> - play     | - Un usuario ingresa múltiples veces al sistema <br> - Un usuario sale múltiples veces del sistema <br> - Un usuario juega múltiples juegos |
  | LogOff      | - Getout                            | - Un usuario puede salirse una sola vez del sistema                                                                                         |
  | Game        | - play <br> - Have <br> - Have <br> | - Un juego es jugado por un usuario <br> - Un juego tiene una sola disposición inicial de números <br> - Un juego tiene múltiples estados   |
  | SudokuBoard | - Have                              | - Un Board tiene múltiples juegos                                                                                                           |
  | State       | - Have                              | - Un juego cambia múltiples veces de estado                                                                                                 |
  ##### Tabla 4.1.5

  <br>

  - La razón de cardinalidad entre las entidades **Login:User**   es: N:1
  - La razón de cardinalidad entre las entidades **LogOff:User**  es: N:1
  - La razón de cardinalidad entre las entidades **User:Game**    es: N:1
  - La razón de cardinalidad entre las entidades **Game:SudokuBoard** es: N:1
  - La razón de cardinalidad entre las entidades **Game:State**   es: 1:N

<br>
<br>

### *Modelo relacional*

<br>

![Modelo relacional ver_3](https://drive.google.com/uc?id=1beRZkQ063BGrnNi9-w7vNUvkgPYIkLuq)

## **Esquema Lógico**

El siguiente paso es la creación de los statements utilizando las bondadades del SGBD asignado para este proyecto.  
En la presente sección se analizan los tipos de datos y la estructura de cada entidad, no se explaya con la explicación de cada entidad, ya que en la sección [Modelo entidad relación](#modelo-entidad-relación) se habla con cierta profundidad y claridad de estos elementos.   

### *Entidades, atributos y dominio*

<br>

- User

  Contiene la información general sobre los usuarios: 

  - El estado de un usuario puede ser activo o inactivo.   
  - El rol del usuario es administrador o usuario.
  - El nombre del usuario es único dentro de la tabla y tiene una longitud máxima de 30 caracteres que permite letras y digitos solamente, el uso del tipo de dato VARCHAR va en esta dirección, dado que el uso de UNIQUE obliga que el tipo de dato sea fijo y no dinámico.
  - Se hace uso del tipo de dato BIT dado que las decisiones a tomar en este atributo son únicamente dos elementos, en este caso la optimización se dirige hacia el almacenamiento, siendo más eficiente que el uso de una estructura de tipo ENUM.
  - La longitud de la contraseña es depreciable.

  <br>

  | Atributo     | Tipo de dato | Dominio | Restricción de integridad |
  |--------------|--------------|---------|---------------------------|
  | id           | SERIAL       |         | PRIMARY KEY               |
  | tex_nickname | VARCHAR      | 30      | UNIQUE, CHECK             |
  | bit_rol      | BIT          | 1       |                           |
  | tex_password | TEXT         |         |                           |
  | bit_state    | BIT          | 1       |                           |
  ##### Tabla 4.1.6

  <br>
  
  **Código**:

  ```SQL
  CREATE TABLE User(
      id SERIAL PRIMARY KEY,
      tex_nickname VARCHAR(30) NOT NULL UNIQUE COMMENT "Nombre de ingreso para el usuario",
      CHECK(tex_nickname RLIKE "[a-zA-Z\d]{4,30}" ), 
      bit_rol BIT(1) DEFAULT 0 NOT NULL COMMENT "0 Usuario | 1 Administrador; Tipos de rol para acceso al sistema", 
      tex_password TEXT NOT NULL COMMENT "Contraseña",
      bit_state BIT(1) DEFAULT 1 NOT NULL COMMENT "0 deshabilitado| 1 habilitado. Dar de baja a los usuarios, de esta forma se evita eliminar a los usuarios de forma explícita de la base de datos"
  )COMMENT "Información general sobre el usuario";
  ```

<br>
<br>

- Login 

  Tabla que almacena la información con respecto al ingreso del usuario
    - Tiene una relación con la tabla User
    - Uso de TIMESTAMP dado que tiene un rango entre los años de 1970 y 2038, mayor versatilidad
  
  <br>

  | Atributo   | Tipo de dato | Dominio | Restricción de integridad |
  |------------|--------------|---------|---------------------------|
  | id         | SERIAL       |         | PRIMARY KEY               |
  | id_user_fk | BIGINT       |         | FOREIGN KEY               |
  | tim_date   | TIMESTAMP    |         |                           |
  ##### Tabla 4.1.7

  <br>

  **Código**:

  ```SQL
  CREATE TABLE Login(
      id SERIAL PRIMARY KEY,
      id_user_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia user",
      tim_date TIMESTAMP DEFAULT NOW() COMMENT "Hora de ingreso al sistema",
      -- tex_nickname TINYTEXT NOT NULL COMMENT "Nombre del usuario",

      FOREIGN KEY (id_user_fk) REFERENCES User(id)
  )COMMENT "Sistema de acceso al sistema";
  ```

<br>
<br>

- SudokuBoard 

  Contiene la información de los datos (digitos) que se cargan a los nuevos tableros que juego el usuario. 
  Solo para aquellos *nuevos juegos* que inicia el usuario. 
    - Internamente se maneja como una cadena con logitud exacta de 89 espacios, 81 digitos más los saltos de linea (se simboliza con el caracter '\n' son ocho en total por tablero), cada tablero es único.

  <br>


  | Atributo  | Tipo de dato | Dominio | Restricción de integridad |
  |-----------|--------------|---------|---------------------------|
  | id        | SERIAL       |         | PRIMARY KEY               |
  | tex_board | VARCHAR      | 89      | UNIQUE                    |
  ##### Tabla 4.1.8

  <br>

  **Código**:

  ```SQL
  CREATE TABLE SudokuBoard(
      id SERIAL PRIMARY KEY,
      tex_board VARCHAR(89) NOT NULL UNIQUE COMMENT "Contiene la información inicial de un tablero, para luego ser rellenado en el Board de la aplicación de escritorio"
  ) COMMENT "Contiene la información de los tableros que pueden ser cargados en la aplicación";
  ```

<br>
<br>

- Game

  Esta entidad es esencial para la integración del juego con el usuario, mantiene una relación entre las distintas actividades y acciones que realiza 
  el jugador, sin embargo funge como intermedio entre otras entidades necesarias para almacenar esta información.
    - **blo_file** primero se debe descomponer el contenido de este atributo según el diseño del sistema, este atributo almacena las jugadas realizadas por el jugador en el tablero, internamente es un arreglo de diccionarios construidos en el lenguaje Python que tiene la siguiente estructura: 
    
      ```Python
        [{row:x1 , col:y1 , val:n, state:0|1}, {row:x2 , col:y2 , val:n, state:0|1}, ...]
      ```
    de esta forma almacena cada una de las jugadas ingresadas por el usuario, se utiliza este estructura para mayor comodidad de la manipulación de los datos a nivel de Python, *row* contiene la componente x del tablero correspondiente al último digito ingresa, esto aplica para la clave *col*, la clave *val* se refiere al digito ingresado, simbolizado con **n**, este n pertenece a los naturales que van del 1 al 9; para la componente en y, la clave *state* se refiere a un estado particular entre que un digito es *ingresado* (0) o que el jugador ha *deshecho*  la jugada (1). En el apartado sobre [Encriptación](#encriptación:-funciones-Built-in) se habla a mayor profundidad sobre este atributo.
    - El resto de atributos se han hablado con cierta profundidad en secciones anteriores, sin embargo *id_user_fk* y *id_sudokuboard_fk* son relaciones que apuntan a las entidades correspondientes descritas en la sección [Esquema conceptual](#esquema-conceptual)
    - **tim_time** es el tiempo que ha permanecido abierto un tablero, es decir el tiempo medido en el que el usuario ha jugado.
    - **tim_date** fecha y hora en la que este tablero fue creado

  <br>

  | Atributo          | Tipo de dato | Dominio | Restricción de integridad |
  |-------------------|--------------|---------|---------------------------|
  | id                | SERIAL       |         | PRIMARY KEY               |
  | id_user_fk        | BIGINT       |         | FOREIGN KEY               |
  | id_sudokuboard_fk | BIGINT       |         | FOREIGN KEY               |
  | blo_file          | BLOB         |         |                           |
  | tim_time          | TIME         |         |                           |
  | tim_date          | TIMESTAMP    |         |                           |
  ##### Tabla 4.1.9

  <br>

  **Código**:

  ```SQL
  CREATE TABLE Game(
      id SERIAL PRIMARY KEY,
      id_user_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia",
      id_sudokuboard_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia los archivos que contiene los tableros",
      blo_file BLOB NOT NULL COMMENT "Archivo .sudoku que genera el programa cada vez que inicia un tablero",
      tim_time TIME NOT NULL COMMENT "hh:mm:ss Minutos transcurridos tras iniciar una partidar o tras continuar una partida pausada",
      tim_date TIMESTAMP DEFAULT NOW() NOT NULL COMMENT "último estado en el que es almacenado el tablero en la base de datos",

      FOREIGN KEY (id_user_fk) REFERENCES User(id),
      FOREIGN KEY (id_sudokuboard_fk) REFERENCES SudokuBoard(id)
  )COMMENT "Tablero del juego";
  ```

<br>
<br>

- LogOff

  Esta entidad internamente es igual a **Login**, sin embargo su objetivo es almacenar la información de todos los usuarios que salen del sistema.
  
  <br>
  
  | Atributo   | Tipo de dato | Dominio | Restricción de integridad |
  |------------|--------------|---------|---------------------------|
  | id         | SERIAL       |         | PRIMARY KEY               |
  | id_user_fk | BIGINT       |         | FOREIGN KEY               |
  | tim_date   | TIMESTAMP    |         |                           |
  ##### Tabla 4.2.1

  <br>

  **Código**:

  ```SQL
  CREATE TABLE LogOff(
      id SERIAL PRIMARY KEY,
      id_user_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia usuario",
      tim_date TIMESTAMP DEFAULT NOW() NOT NULL COMMENT "Tiempo en el que cierre de sesión un usuario",

      FOREIGN KEY (id_user_fk) REFERENCES User(id)
  )COMMENT "Cierre de sesión por parte de un usuario";
  ```

<br>
<br>

- State

  Entidad que almacena el **estado** y el tiempo del juego con respecto a los movimientos o acciones que realiza un jugador. 
  Estas acciones se encuentran asociadas a un único juego
    - Se utiliza el atributo multivalor *cod__state* con un tipo de dato ENUM, establecemos cinco valores: 
      - **nuevo**   
        En el momento de crear un nuevo tablero (este tablero es único mientras la jugada no ha finalizado)
      - **pausado**   
        Cambia a este estado en el momento de presionar el botón pausa, significa que el usuario no puede realizar más acciones en el tablero
      - **finalizado**   
        Significa que el usuario ha completado de forma satisfactoria el tablero, sin equivocación alguna en cada casilla
      - **derrota**   
        El usuario ha decidido no continuar con el tablero actual 
      - **continuar**  
        Juego que mantiene un estado pausa, y que es llamado nuevamente al juego, esta transición se le conoce como *continuar*
      - **tim_date** fecha y hora en la que el usuario cambia el estado del tablero 


  <br>

  | Atributo   | Tipo de dato | Dominio                                                  | Restricción de integridad |
  |------------|--------------|----------------------------------------------------------|---------------------------|
  | id         | SERIAL       |                                                          | PRIMARY KEY               |
  | id_game_fk | BIGINT       |                                                          | FOREIGN KEY               |
  | cod_state  | ENUM         | "nuevo", "pausado", "finalizado", "derrota", "continuar" |                           |
  | tim_date   | TIMESTAMP    |                                                          |                           |
  ##### Tabla 4.2.2

  <br>

  **Código**:

  ```SQL
  CREATE TABLE State(
      id SERIAL PRIMARY KEY,
      id_game_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad Juego",
      cod_state ENUM("nuevo", "pausado", "finalizado", "derrota", "continuar") DEFAULT "nuevo" NOT NULL 
      COMMENT "Estados del juego, el estado finalizado significa haber concluido el juego con éxito, derrota es haber abandonado la partida",
      tim_date TIMESTAMP DEFAULT NOW() NOT NULL COMMENT "último estado en el que es almacenado el tablero en la base de datos",

      FOREIGN KEY (id_game_fk) REFERENCES Game(id)
  )COMMENT "Estados en los que puede estar el tablero de juego para un jugador";
  ```

<br>
<br>

- Binacle

  Esta tabla ha cambiado a lo largo del desarrollo del proyecto, sin embargo los analistas y desarrolladores pertencientes a este equipo concluyen con este modelo, en el que se almacena toda acción relacionada con el juego y el jugador. 
  A continuación se enuncian alguna de estas acciones por parte de un usuario y un administrador: 
  - Acciones por parte del usuario:
    - cambios de estado en el juego
    - ingreso al sistema 
    - salida del sistema
    - visualizar tabla de puntuaciones
  - Acciones por parte del administrador 
    - Mismas acciones del usuario
    - Adicionalmente crear un usuario
    - Editar nombre de usuario
    - Editar contraseña 
    - Cambiar estado de un usuario
      - activo
      - inactivo

  - **tex_nickname** nombre del usuario
  - **tex_description** breve descripción de la acción que ha realizado en el sistema
  - **tim_date** fecha y hora en la que un usuario o administrador realiza una acción en el juego o en el sistema

  <br>

  | Atributo        | Tipo de dato | Dominio | Restricción de integridad |
  |-----------------|--------------|---------|---------------------------|
  | id              | SERIAL       |         | PRIMARY KEY               |
  | tex_nickname    | TINYTEXT     |         |                           |
  | tex_description | TEXT         |         |                           |
  | tim_date        | TIMESTAMP    |         |                           |
  ##### Tabla 4.2.2

  <br>

    **Código**:

  ```SQL
  CREATE TABLE Binacle(
      id SERIAL PRIMARY KEY, 
      tex_nickname TINYTEXT NOT NULL COMMENT "Descripción del nombre del usuario", 
      tex_description TEXT NOT NULL COMMENT "Descripción de la acción que realiza un usuario en el sistema",
      tim_date TIMESTAMP NOT NULL DEFAULT NOW() COMMENT "Tiempo exacto en el que se realizó la acción"
      
  )COMMENT = "Almacena acciones realizadas por los usuarios";
  ```

<br>
<br>

### *Vistas*

<br>

- vw_GetLastLoginUser

  Obtiene el último usuario que ingresó al sistema.

  <br>

  **Código**:

  ```SQL 
  CREATE VIEW vw_GetLastLoginUser
    AS 
    SELECT 
        login.id AS id,
        User.tex_nickname AS name,
        User.bit_rol AS rol 
    FROM 
        User
    INNER JOIN 
        (
            SELECT 
                id_user_fk AS id
            FROM 
                Login 
            ORDER BY 
                tim_date DESC  
            LIMIT 1
        ) AS login ON User.id = login.id
        ;
  ```

<br>
<br>

### *Funciones*

<br>

- fn_CompareDate
  - Parámetros:
    - pyNickname: texto plano que contiene el nombre de usuario que inicia sesión.
    - pyPassword: texto plano que contiene la contraseña del usuario que inicia sesión.
  - Retorno: 
    - nicknameResult: 1 si el nombre de usuario está registrado en la base de datos, 0 si no lo está.
    - passwordResult: 1 si la contraseña pasada por parámetro es igual a la contraseña almacenada en la base de datos, 0 si no lo es.
    - rolResult: 1 si el rol del usuario es administrador, 0 si no lo es.
    - newPasswordResult: 1 si el usuario debe realizar un cambio de contraseña, 0 si no debe hacerlo.
    - userState: 1 si el usuario está habilitado (para ingresar), 0 si está deshabilitado.

  <br>

  **Código**:

  ```SQL
  DROP FUNCTION IF EXISTS fn_compareData;
  DELIMITER $$
    CREATE FUNCTION fn_compareData(pyNickname TEXT, pyPassword TEXT) RETURNS TEXT
    BEGIN

    SET @nicknameResult = IF(pyNickname IN (SELECT tex_nickname FROM User), 1, 0);
    SET @password = (SELECT tex_password FROM User WHERE tex_nickname = pyNickname);
    
    SET @passwordResult = IF(@password = HEX(AES_ENCRYPT(pyPassword, pyNickname)), 1, 0);
    SET @rolResult = IF((SELECT bit_rol FROM User WHERE tex_nickname = pyNickname) = 1, 1, 0);
    SET @newPasswordResult = IF((SELECT HEX(AES_ENCRYPT(pyNickname, pyNickname)) FROM User WHERE tex_nickname = pyNickname) = @password, 1, 0);
    SET @userState = IF((SELECT bit_state FROM User WHERE tex_nickname = pyNickname) = 1, 1, 0);
    SET @result = (SELECT CONCAT(@nicknameResult, " ", @passwordResult, " " ,@rolResult, " ", @newPasswordResult, " ", @userState));

    RETURN @result;

    END $$
  DELIMITER ;
  ```

<br>
<br>

- fn_getNickNameByState:
  - Parámetros:
    - id_game_fk: Entero que corresponde al id de la tabla de Game.
  - Retorno: texto que corresponde al nombre de usuario.
  
  <br>

  **Código**:
  ```SQL
  DROP FUNCTION IF EXISTS fn_getNickNameByState;
  DELIMITER $$
    CREATE FUNCTION fn_getNickNameByState(id_game_fk BIGINT UNSIGNED) RETURNS VARCHAR(40)
    BEGIN 
        RETURN (
                    SELECT  
                        User.tex_nickname AS nickname
                    FROM
                        User
                    INNER JOIN 
                        Game ON User.id = Game.id_user_fk
                    WHERE 
                        Game.id = id_game_fk
                )
            ;
    END $$
  DELIMITER ;
  ```

<br>
<br>

- fn_getNicknameById
  - Parámetros:
    - id_user_fk: entero que corresponde con el id del usuario.
  - Retorno: texto con el nombre de usuario.

  <br>

  **Código**:
  ```SQL
  DROP FUNCTION IF EXISTS fn_getNicknameById;
  DELIMITER $$
    CREATE FUNCTION fn_getNicknameById(id_user_fk BIGINT UNSIGNED) RETURNS VARCHAR(40)
    BEGIN 
        RETURN (
                    SELECT  
                        tex_nickname AS nickname
                    FROM
                        User
                    WHERE 
                        id = id_user_fk
                )
            ;
    END $$
  DELIMITER ;
  ```

<br>
<br>

### *Disparadores*

<br>

- tg_createBoard:

  Se ejecuta después de realizar cualquier acción sobre el tablero (Después de una inserción en la tabla State).

  **Código**:
  ```SQL
  DROP TRIGGER IF EXISTS tg_createBoard;
  DELIMITER $$ 
    CREATE TRIGGER tg_createBoard 
        AFTER INSERT
        ON State FOR EACH ROW
    BEGIN  
        INSERT INTO Binacle(tex_nickname, tex_description) VALUES
            (
                fn_getNickNameByState(new.id_game_fk)
                , 

                (
                    SELECT 
                        CASE
                            WHEN  new.cod_state = 1 THEN  "Creó un nuevo tablero"
                            WHEN  new.cod_state = 2 THEN "Pausó el juego"
                            WHEN  new.cod_state = 3 THEN "Finalizó con éxito la partida"
                            WHEN  new.cod_state = 4 THEN "Perdió la partida"
                            WHEN  new.cod_state = 5 THEN "Continuó la partida en pausa"
                        END 
                )
            )
        ;
    END $$
  DELIMITER ; 
  ```
<br>
<br>

- tg_login:

  Se ejecuta cada vez que un usuario inicia sesión (Después de una inserción en la tabla Login).

  **Código**:
  ```SQL
  DROP TRIGGER IF EXISTS tg_login; 
  DELIMITER $$ 
    CREATE TRIGGER tg_login
        AFTER INSERT 
        ON Login FOR EACH ROW
    BEGIN 
        INSERT INTO Binacle(tex_nickname, tex_description) VALUES
            (
                fn_getNicknameById(new.id_user_fk), 
                "El usuario inició sesión"
            )
        ;
    END $$
  DELIMITER ;
  ```

<br>
<br>

- tg_logOff

  Se ejecuta cada vez que un usuario cierra sesión (Después de una inseción en la tabla LogOff).

  **Código**:
  ```SQL
  DROP TRIGGER IF EXISTS tg_logOff; 
  DELIMITER $$ 
    CREATE TRIGGER tg_logOff
        AFTER INSERT 
        ON LogOff FOR EACH ROW
    BEGIN 
        INSERT INTO Binacle(tex_nickname, tex_description) VALUES
            (
                fn_getNicknameById(new.id_user_fk), 
                "El usuario cerró sesión"
            )
        ;
    END $$
  DELIMITER ;
  ```

<br>
<br>

- tg_createUser

  Se ejecuta cada vez que un usuario es creado (Después de inserción en la tabla User).

  **Código**:
  ```SQL
  DROP TRIGGER IF EXISTS tg_createUser; 
  DELIMITER $$ 
    CREATE TRIGGER tg_createUser
        AFTER INSERT 
        ON User FOR EACH ROW
    BEGIN 
        INSERT INTO Binacle(tex_nickname, tex_description) VALUES
            (
                "admin", 
                CONCAT("El usuario ", new.tex_nickname, " ha sido creado")
                
            )
        ;
    END $$
  DELIMITER ;
  ```
<br>
<br>

### *Procedimientos Almacenados*

<br>

- sp_updatePassword

  Se utiliza el nombre de usuario para encriptar la contraseña, por ende, cada vez que se cambia el nombre de usuario se necesita cambiar el texto con el que se encripta la contraseña. El texto(plano) de la contraseña seguirá intacto, sin embargo, la contraseña se encriptará con el nuevo nombre de usuario. Se encarga de desencriptar la contraseña (con el nombre de usuario actual) y encriptarla con el nuevo nombre de usuario.
  - Parámetros:
    - pyOldNickname: texto que contiene el nombre de usuario actual.
    - pyNewNickname: texto que contiene el nombre de usuario nuevo.

  **Código**:
  ```SQL
  DROP PROCEDURE IF EXISTS sp_updatePassword;
  DELIMITER $$
  CREATE PROCEDURE sp_updatePassword(IN pyOldNickname TEXT, IN pyNewNickname TEXT)
  BEGIN  

    SET @oldPassword = (
        SELECT 
            AES_DECRYPT(UNHEX(tex_password), pyOldNickname) 
        FROM 
            User 
        WHERE 
            tex_nickname = pyOldNickname
        );

    UPDATE 
        User 
    SET 
        tex_password = HEX(AES_ENCRYPT(@oldPassword, pyNewNickname)) 
    WHERE 
        tex_nickname = pyOldNickname;

  END $$
  DELIMITER ;
  ```

<br>
<br>

## **Encriptación: Funciones Built-in**
<br>

- AES_ENCRYPT()

  Es una función incluida en el SGBD que utiliza el algoritmo AES para encriptar.
  - Parámetros:
    - cadena a encriptar.
    - cadena que se utiliza como clave.

  Se utiliza para encriptar tanto la contraseña de cada usuario como tambien el contenido del campo *blo_file* de la tabla Game.
<br>
- AES_DECRYPT()

  Es una función incluida en el SGBD que utiliza el algoritmo AES para desencriptar. 
  - Parámetros:
    - cadena a desencriptar.
    - cadena que se utilizó como clave para encriptar.
<br>
- HEX()

  Es una función incluida en el SGBD que se utiliza para convertir a hexadecimal la cadena pasada por parámetro.
  La función se utliza para obtener el resultado de la contraseña encriptada en hexadecimal.
<br>
- UNHEX()

  Es una función incluida en el SGBD que se utiliza obtener la cadena original desde un valor hexadecimal pasado por parámetro (al inverso que HEX()).

<br>
<br>

## **Anotaciones finales**

![](https://drive.google.com/uc?id=10avXiTMkJS7NIFQ_zou0w3yi4dqXiBqe)
![](https://drive.google.com/uc?id=1xSBS8U8dm5oJ92eOAlD9k0v1CaoVzui6)
![](https://drive.google.com/uc?id=124Ax2SLC-QfAtrW0sr4R_aBgtQFhSSrR)

-----

## **Elementos Conceptuales**

En el proyecto se hacen uso de algunas librerías y clases de Python que se definirán a continuación:

### **Tkinter**

-----

Es una librería que proporciona a las aplicaciones de Python una interfaz de usuario fácil de programar. Además es un conjunto de herramientas GUI de Tcl/Tk (Tcl: Tool Command Language), proporcionando una amplia gama de usos, incluyendo aplicaciones web, de escritorio, redes, administración, pruebas y muchos más.

Tkinter no es solo la única librería para python especializada en la creación de interfaces gráficas, entre las más empleadas están wxPython, PyQt y PyGtk, todas con ventajas y desventajas. Entre los puntos fuertes que caracterizan a Tkinter en la creación de GUI, es que viene instalado con python en casi todas las plataformas, su sintaxis es clara, fácil de aprender y documentación completa.

**Ejemplo:** *test.py* - Ventana de testeo de Tkinter

    from tkinter import *
    Tkinter._test()


### **configparser**

-----

Es una clase que proporciona una función llamada *interpolation* que se puede usar para combinar valores juntos. Los valores que contienen cadenas de formato Python estándar activan la función de interpolación cuando se recuperan. Las opciones nombradas dentro del valor que se está recuperando se reemplazan por sus valores, hasta que no sea necesaria más sustitución.

La interpolación se realiza por defecto cada vez que se llama a *get()*. Pasa un valor verdadero en el argumento raw para recuperar el valor original, sin interpolación.

### **MySQL Connector**

-----

MySQL Connector/Python[7] permite que los programas Python accedan a las bases de datos MySQL, utilizando una API que cumple con la especificación de la API de la base de datos de Python v2.0 (PEP 249).

MySQL Connector/Python incluye soporte para:

- Casi todas las funciones proporcionadas por MySQL Server hasta MySQL Server version 8.0 inclusive.
- Connector/Python 8.0 también es compatible con X DevAPI. Para obtener documentación de los conceptos y el uso de MySQL Connector/Python con X DevAPI, consulte la Guía del usuario de X DevAPI.
- Conversión de valores de parámetros entre tipos de datos de Python y MySQL, por ejemplo, Python datetime y MySQL DATETIME. Puede activar la conversión automática por conveniencia o desactivarla para un rendimiento óptimo.
- Todas las extensiones de MySQL a la sintaxis SQL estándar.
- Compresión de protocolo, que permite comprimir el flujo de datos entre el cliente y el servidor.
- Conexiones usando sockets TCP/IP y en Unix usando sockets Unix.
- Conexiones TCP/IP seguras mediante SSL.
- Conductor autónomo. Connector/Python no requiere la biblioteca cliente MySQL ni ningún módulo de Python fuera de la biblioteca estándar.

Connector/Python no es compatible con los antiguos métodos de autenticación de MySQL Server, lo que significa que las versiones de MySQL anteriores a 4.1 no funcionarán.

-----

## **Código Fuente de Sudoku Game**

-----

- La creación del código se puede encontrar en la página [Sudoku Game with Tkinter](http://newcoder.io/gui/part-1/) el cual esta dividido en cuatro partes.
- En la página anteriormente mencionada se planea la creación de un juego de Sudoku usando Python y Tkinter. 
- Primero se comienza a describir la lógica del juego en donde se menciona que se tiene que verificar si todas las lineas horizontales y columnas verticales contienen los digitos del 1 al 9.
- Se tiene que tomar en cuenta los tableros que el jugador desea jugar.
- Usar un GUI (Graphic User Interface). Es donde entra el uso de la libreria de Tkinter.

-----

## **Actividades**

-----

### **Actividad #1**

Como primera actividad se procedio a leer detenidamente la definición del proyecto para hacer un análisis profundo (análisis.md) de las cosas que se deben instalar y hacer.

![Actividad1](https://drive.google.com/uc?export=view&id=1xjd5oCQNBbpkor6OHT7rgsiARWF8njUB "Actividad1")

### **Actividad #2**

Como segunda actividad se empezo a escribir en análisis de las cosas a hacer y los pasos correctos a seguir. 

![Actividad2](https://drive.google.com/uc?export=view&id=1KJif_w4MEh1JyAZ-CkTDVVeY0qUBMR9d "Actividad2")

### **Actividad #3**

Se comenzó a trabajar en la estructura de la base de datos, el diagrama UML y el diagrama ER.

![Actividad3](https://drive.google.com/uc?export=view&id=1Q8bzvQzUrDcNEuLdWO_meIMWjaMALm35 "Actividad3")

### **Actividad #4**

Una vez teniendo los diagramas respectivos se comenzo a hacer los scripts necesarios para la creación de la base de datos.

![Actividad4](https://drive.google.com/uc?export=view&id=1-mSpcKU1yW6T5MWzHfV0onU1rnw0x7MF "Actividad4")

### **Actividad #5**

Se creo un repositorio en GitHub para facilitar el trabajo y evitar problemas a la hora de trabajar individualmente con los trabajos que se asignan a cada integrante.

![Actividad5](https://drive.google.com/uc?export=view&id=1ovzsyklbMCJwmw6KLeuT6FiTkVZxnGjC "Actividad5")

-----

## **NOTAS Y BIBLIOGRÍAS**

-----

- [1]: Todas las reuniones síncronas del equipo de trabajo se llevaron a cabo en Discord/Google Meet. Estas reuniones se realizaban a partir de las 1pm/9pm (dependiendo de la disponibilidad de los integrantes) para poder cumplir con los deberes del proyecto.

  - ![ServerDiscord](https://drive.google.com/uc?export=view&id=1hG9Ydwo63XZoqSyQg1DjbC-BSxDOJ-jN "ServerDiscord")

- [2]: Para las discución y la planeación del proyecto de forma asíncrona se creó un grupo de whatsapp y se le dio uso al canal de texto en el servidor de Discord/Google Meet
- [3] "tkinter - Interfaz de Python a Tcl / Tk - Documentación de Python 3.9.1", Docs.python.org , 2020. [En línea]. Disponible: https://docs.python.org/3/library/tkinter.html.
- [4] "configparser - Analizador de archivos de configuración - Documentación de Python 3.9.1", Docs.python.org , 2020. [En línea]. Disponible: https://docs.python.org/3/library/configparser.html.
- [5] K. Lee y S. Hubbard, Estructuras de datos y algoritmos con Python. , 2ª ed. Springer, 2015.
- [6] "MySQL :: MySQL Connector / Python Developer Guide :: 1 Introducción a MySQL Connector / Python", Dev.mysql.com , 2020. [En línea]. Disponible: https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html.
- [7] "Not Your Type? Big Data Matchmaker On Five Data Types You Need To Explore Today", 2012. Disponible: http://www.dataversity.net/not-your-type-big-data-matchmaker-on-five-data-types-you-need-to-explore-today
