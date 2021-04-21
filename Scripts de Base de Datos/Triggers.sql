/*
    @author kenneth.cruz@unah.hn
    @version 0.1.1
    @date 2021/04/20
*/

USE SudokuDB; 

DROP TABLE IF EXISTS Binacle;
CREATE TABLE Binacle(
    id SERIAL PRIMARY KEY, 
    tex_nickname TINYTEXT NOT NULL COMMENT "Descripción del nombre del usuario", 
    tex_description TEXT NOT NULL COMMENT "Descripción de la acción que realiza un usuario en el sistema",
    tim_date TIMESTAMP NOT NULL DEFAULT NOW() COMMENT "Tiempo exacto en el que se realizó la acción"
    
)COMMENT = "Almacena acciones realizadas por los usuarios";


DROP FUNCTION IF EXISTS fn_getNickname;

DELIMITER $$

    CREATE FUNCTION fn_getNickName(id BIGINT UNSIGNED) RETURNS VARCHAR(40)
    BEGIN 
        RETURN (
                    SELECT  
                        User.tex_nickname AS nickname
                    FROM
                        User
                    INNER JOIN 
                        Game ON User.id = Game.id_user_fk
                    WHERE 
                        Game.id = id
                )
            ;
    END $$

DELIMITER ;

--
-- Al realizar cualquier acción sobre el tablero. 
--

DROP TRIGGER IF EXISTS tg_createBoard;

DELIMITER $$ 
    
    SET @var = "el usuario # ha ";

    CREATE TRIGGER tg_createBoard 
        AFTER INSERT
        ON State FOR EACH ROW
    BEGIN  
        INSERT INTO Binacle(tex_nickname, tex_description) VALUES
            (
                fn_getNickName(new.id)
                , 

                (
                    SELECT 
                        CASE
                            WHEN  new.cod_state = "nuevo" THEN  CONCAT(@var, "creado un nuevo tablero")
                            WHEN  new.cod_state = "pausado" THEN CONCAT(@var, "pausado el juego")
                            WHEN  new.cod_state = "finalizado" THEN CONCAT(@var, "concluido con éxito el juego")
                            WHEN  new.cod_state = "derrota" THEN CONCAT(@var, "perdido la partida")
                            WHEN  new.cod_state = "continuar" THEN CONCAT(@var, "iniciado un juego en pausa")
                        END 
                )
            )
        ;
    END $$

DELIMITER ; 


--
-- Inicio de sesión
--

DROP TRIGGER IF EXISTS tg_login; 

DELIMITER $$ 

    CREATE TRIGGER tg_login
        AFTER INSERT 
        ON Login FOR EACH ROW
    BEGIN 
        INSERT INTO Binacle(tex_nickname, tex_description) VALUES
            (
                fn_getNickName(new.id), 
                "el usuario # inició sesión"
            )
        ;
    END $$

DELIMITER ;



--
-- Cierre de sesión
--

DROP TRIGGER IF EXISTS tg_login; 

DELIMITER $$ 

    CREATE TRIGGER tg_login
        AFTER INSERT 
        ON LogOff FOR EACH ROW
    BEGIN 
        INSERT INTO Binacle(tex_nickname, tex_description) VALUES
            (
                fn_getNickName(new.id), 
                "el usuario # cerro sesión"
            )
        ;
    END $$

DELIMITER ;

