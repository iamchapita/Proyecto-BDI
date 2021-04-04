/*
    @author kenneth.cruz@unah.hn
    @version 0.1.2
    @date 2021/03/30
*/

DROP DATABASE IF EXISTS SudokuDB;

CREATE DATABASE SudokuDB CHARACTER SET utf8; 

USE SudokuDB; 

CREATE TABLE User(
    id SERIAL PRIMARY KEY,
    tex_nickname VARCHAR(30) NOT NULL UNIQUE COMMENT "Nombre de ingreso para el usuario",
    CHECK( tex_nickname RLIKE "[a-zA-Z0-9._-]{3,}" ), 
    bit_rol BIT(1) DEFAULT 0 NOT NULL COMMENT "0 Usuario | 1 Administrador; Tipos de rol para acceso al sistema", 
    tex_password TEXT NOT NULL COMMENT "Contraseña",
    CHECK( tex_password RLIKE "[a-zA-Z\d_.-]{ 4,}" ) 
)COMMENT "Información general sobre el usuario";

CREATE TABLE Login(
    id SERIAL PRIMARY KEY,
    id_user_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia user",
    dat_date TIMESTAMP DEFAULT NOW() COMMENT "Hora de ingreso al sistema",
    -- tex_nickname TINYTEXT NOT NULL COMMENT "Nombre del usuario",

    FOREIGN KEY (id_user_fk) REFERENCES User(id)
)COMMENT "Sistema de acceso al sistema";

CREATE TABLE Game(
    id SERIAL PRIMARY KEY,
    id_user_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia",
    blo_file BLOB NOT NULL COMMENT "Archivo .sudoku que genera el programa cada vez que inicia un tablero",
    hor_time TIME NOT NULL COMMENT "hh:mm:ss Minutos transcurridos tras iniciar una partidar o tras continuar una partida pausada",
    tim_date TIMESTAMP DEFAULT NOW() NOT NULL COMMENT "último estado en el que es almacenado el tablero en la base de datos",

    FOREIGN KEY (id_user_fk) REFERENCES User(id)
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
    cod_nameState ENUM("nuevo", "pausado", "finalizado", "derrota") DEFAULT "nuevo" NOT NULL 
    COMMENT "Estados del juego, el estado finalizado significa haber concluido el juego con éxito, derrota es haber abandonado la partida",

    FOREIGN KEY (id_game_fk) REFERENCES Game(id)
)COMMENT "Estados en los que puede estar el tablero de juego para un jugador";


CREATE TABLE Action(
    id SERIAL PRIMARY KEY,
    bit_state bit(1) DEFAULT 0 NOT NULL COMMENT "'0' rellenar respuesta | '1' Un usuario puede desear 'regresar' una (o varias) jugadas atrás",
    sma_number SMALLINT UNSIGNED DEFAULT 0 NOT NULL COMMENT "Resultado ingresado por el usuario"
)COMMENT "Resultado de cada casilla que rellena un juagdor";


CREATE TABLE GameAction(
    id SERIAL PRIMARY KEY,
    id_action_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la table action",
    id_game_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la tabla Game",

    FOREIGN KEY (id_action_fk) REFERENCES Action(id),
    FOREIGN KEY (id_game_fk) REFERENCES Game(id)
)COMMENT "Relación entre un tablero y los resultados ingresados por el usuario";



CREATE VIEW Binacle
    AS 
    SELECT 
        User.id AS "user",
        Login.id AS "login", -- Ingreso al sistema
        LogOff.id AS "logoff", -- Salida del sistema
        State.id AS "State", -- Pausa, creación, inicio, ganó, perdió el usuario en el juego,
        Action.id AS "acciones" -- Cada vez que inserta un número al tablero
    FROM 
        User
    INNER JOIN 
        Login ON User.id = Login.id_user_fk
    INNER JOIN 
        LogOff ON User.id = LogOff.id_user_fk
    INNER JOIN  
        Game ON  User.id = Game.id_user_fk
    INNER JOIN 
        State ON Game.id = State.id_game_fk
    INNER JOIN 
        GameAction ON Game.id = GameAction.id_game_fk
    INNER JOIN 
        Action ON Action.id = GameAction.id_action_fk
;
