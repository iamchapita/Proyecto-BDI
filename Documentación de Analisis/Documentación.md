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
    - [**Modelados ER y Diagramas ER**](#modelados-er-y-diagramas-er)
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
  - [**Elementos Conceptuales**](#elementos-conceptuales)
    - [**Tkinter**](#tkinter)
    - [**MySQL Connector**](#mysql-connector)
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

Diagrama UML:
  
  ![M&D-ER-A](https://drive.google.com/uc?export=view&id=1LcmdihAf789uWKR6vDuqI7Gudur7L7vP "Diagrama UML")

Diagrama ER:

  ![M&D-ER-B](https://drive.google.com/uc?export=view&id=18wtSAeSUh3Qon_7OtJJvHvpgTFBPxeHb "Diagrama ER")

-----

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

- [1]: Todas las reuniones síncronas del equipo de trabajo se llevaron a cabo en Discord la cual es una aplicación freeware de diálogo y texto. Estas reuniones se realizaban a partir de las 4pm cuando los miembros del equipo ya habian terminados sus jornada academica para así contar con a disposición de tiempo necesaria para poder cumplir con los deberes del proyecto.

  - ![ServerDiscord](https://drive.google.com/uc?export=view&id=1hG9Ydwo63XZoqSyQg1DjbC-BSxDOJ-jN "ServerDiscord")

- [2]: Para las discución y la planeación del proyecto de forma asíncrona se creó un grupo de whatsapp y se le dio uso al canal de texto en el servidor de Discord/Google Meet
- [3] "tkinter - Interfaz de Python a Tcl / Tk - Documentación de Python 3.9.1", Docs.python.org , 2020. [En línea]. Disponible: https://docs.python.org/3/library/tkinter.html.
- [4] "configparser - Analizador de archivos de configuración - Documentación de Python 3.9.1", Docs.python.org , 2020. [En línea]. Disponible: https://docs.python.org/3/library/configparser.html.
- [5] K. Lee y S. Hubbard, Estructuras de datos y algoritmos con Python. , 2ª ed. Springer, 2015.
- [6] "MySQL :: MySQL Connector / Python Developer Guide :: 1 Introducción a MySQL Connector / Python", Dev.mysql.com , 2020. [En línea]. Disponible: https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html.
