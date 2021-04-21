/*
    @author kenneth.cruz@unah.hn
    @version 0.1.7
    @date 2021/03/30
*/

DROP DATABASE IF EXISTS SudokuDB;

CREATE DATABASE SudokuDB CHARACTER SET utf8; 

USE SudokuDB; 

CREATE TABLE User(
    id SERIAL PRIMARY KEY,
    tex_nickname VARCHAR(30) NOT NULL UNIQUE COMMENT "Nombre de ingreso para el usuario",
    CHECK(tex_nickname RLIKE "[a-zA-Z\d]{4,30}" ), 
    bit_rol BIT(1) DEFAULT 0 NOT NULL COMMENT "0 Usuario | 1 Administrador; Tipos de rol para acceso al sistema", 
    tex_password TEXT NOT NULL COMMENT "Contraseña",
    bit_state BIT(1) DEFAULT 1 NOT NULL COMMENT "0 deshabilitado| 1 habilitado. Dar de baja a los usuarios, de esta forma se evita eliminar a los usuarios de forma explícita de la base de datos"
)COMMENT "Información general sobre el usuario";

CREATE TABLE Login(
    id SERIAL PRIMARY KEY,
    id_user_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia user",
    tim_date TIMESTAMP DEFAULT NOW() COMMENT "Hora de ingreso al sistema",
    -- tex_nickname TINYTEXT NOT NULL COMMENT "Nombre del usuario",

    FOREIGN KEY (id_user_fk) REFERENCES User(id)
)COMMENT "Sistema de acceso al sistema";

CREATE TABLE SudokuBoard(
    id SERIAL PRIMARY KEY,
    tex_board VARCHAR(89) NOT NULL UNIQUE COMMENT "Contiene la información inicial de un tablero, para luego ser rellenado en el Board de la aplicación de escritorio"
) COMMENT "Contiene la información de los tableros que pueden ser cargados en la aplicación";


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

CREATE TABLE LogOff(
    id SERIAL PRIMARY KEY,
    id_user_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia usuario",
    tim_date TIMESTAMP DEFAULT NOW() NOT NULL COMMENT "Tiempo en el que cierre de sesión un usuario",

    FOREIGN KEY (id_user_fk) REFERENCES User(id)
)COMMENT "Cierre de sesión por parte de un usuario";


CREATE TABLE State(
    id SERIAL PRIMARY KEY,
    id_game_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad Juego",
    cod_state ENUM("nuevo", "pausado", "finalizado", "derrota", "continuar") DEFAULT "nuevo" NOT NULL 
    COMMENT "Estados del juego, el estado finalizado significa haber concluido el juego con éxito, derrota es haber abandonado la partida",
    tim_date TIMESTAMP DEFAULT NOW() NOT NULL COMMENT "último estado en el que es almacenado el tablero en la base de datos",

    FOREIGN KEY (id_game_fk) REFERENCES Game(id)
)COMMENT "Estados en los que puede estar el tablero de juego para un jugador";


CREATE TABLE Action(
    id SERIAL PRIMARY KEY,
    bit_state bit(1) DEFAULT 0 NOT NULL COMMENT "'0' rellenar respuesta | '1' Un usuario puede desear 'regresar' una (o varias) jugadas atrás",
    sma_number SMALLINT UNSIGNED DEFAULT 0 NOT NULL COMMENT "Resultado ingresado por el usuario",
    sma_row SMALLINT UNSIGNED NOT NULL COMMENT "Coordenada en el eje x dentro del tablero",
    sma_column SMALLINT UNSIGNED NOT NULL COMMENT "Coordenada en el eje y dentro del tablero"
)COMMENT "Resultado de cada casilla que rellena un jugador";


CREATE TABLE GameAction(
    id SERIAL PRIMARY KEY,
    id_action_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la table action",
    id_game_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la tabla Game",

    FOREIGN KEY (id_action_fk) REFERENCES Action(id),
    FOREIGN KEY (id_game_fk) REFERENCES Game(id)
)COMMENT "Relación entre un tablero y los resultados ingresados por el usuario";