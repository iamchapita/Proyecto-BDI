/*
    @author kenneth.cruz@unah.hn
    @version 0.1.2
    @date 2021/04/20
*/

USE SudokuDB; 

--
-- Al realizar cualquier acción sobre el tablero. 
--

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
                            WHEN  new.cod_state = 1 THEN  "el usuario # ha creado un nuevo tablero"
                            WHEN  new.cod_state = 2 THEN "el usuario # ha pausado el juego"
                            WHEN  new.cod_state = 3 THEN "el usuario # ha concluido con éxito el juego"
                            WHEN  new.cod_state = 4 THEN "el usuario # ha perdido la partida"
                            WHEN  new.cod_state = 5 THEN "el usuario # ha iniciado un juego en pausa"
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
                fn_getNicknameById(new.id_user_fk), 
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
                fn_getNicknameById(new.id_user_fk), 
                "el usuario # cerro sesión"
            )
        ;
    END $$

DELIMITER ;

--
-- Eliminación/Recuperación de usuario (Cambio de estado)
--

DROP TRIGGER IF EXISTS tg_createUser; 

DELIMITER $$ 

    CREATE TRIGGER tg_createUser
        AFTER INSERT 
        ON User FOR EACH ROW
    BEGIN 
        INSERT INTO Binacle(tex_nickname, tex_description) VALUES
            (
                new.tex_nickname, 
                "el usuario # ha sido creado"
                
            )
        ;
    END $$

DELIMITER ;