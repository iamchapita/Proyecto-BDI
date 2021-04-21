/*
    @author kenneth.cruz@unah.hn
    @version 0.1.0
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


DROP TRIGGER IF EXISTS tg_createBoard;

DELIMITER $$ 

    CREATE TRIGGER tg_createBoard 
        AFTER INSERT
        ON State FOR EACH ROW
    BEGIN  
        INSERT INTO Binacle(tex_nickname, tex_description) VALUES
            (
                (
                    SELECT  
                        User.tex_nickname AS nickname
                    FROM
                        User
                    INNER JOIN 
                        Game ON User.id = Game.id_user_fk
                    WHERE 
                        Game.id = new.id_game_fk
                ), 

                (
                    SELECT 
                        CASE
                            WHEN  new.cod_state = "nuevo" THEN  "ha creado un nuevo tablero"
                            WHEN  new.cod_state = "pausado" THEN "ha pausado el juego"
                            WHEN  new.cod_state = "finalizado" THEN "ha concluido con éxito el juego"
                            WHEN  new.cod_state = "derrota" THEN "ha perdido la partida"
                            WHEN  new.cod_state = "continuar" THEN "ha iniciado un juego en pausa"
                        END 
                )
            )
        ;
    END $$

DELIMITER ; 