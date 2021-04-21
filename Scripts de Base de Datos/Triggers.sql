/*
    @author kenneth.cruz@unah.hn
    @version 0.1.1
    @date 2021/04/20
*/

USE SudokuDB; 

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

DROP TRIGGER IF EXISTS tg_logOff; 

DELIMITER $$ 

    CREATE TRIGGER tg_logOff
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

