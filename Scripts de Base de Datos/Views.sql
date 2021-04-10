/*
    @author gehernandezc@unah.hn, kenneth.cruz@unah.hn
    @version 0.1.3
    @date 2021/04/03
*/

USE SudokuDB; 

CREATE VIEW vw_Binacle
    AS 
        SELECT 
            Binacle.user AS user, 
            Binacle.state AS state,
            Binacle.date AS date
        FROM 
        (
            (
            SELECT 
                id_user_fk AS user, 
                "login" AS state,
                tim_date AS date 
            FROM 
                Login 
            )

            UNION

            (
                SELECT 
                    id_user_fk AS user, 
                    "logout" AS state,
                    tim_date AS date 
                FROM 
                    LogOff
            )

            UNION

            (
                SELECT 
                    Game.id_user_fk AS user, 
                    IF(BoardState.state=2, "pausa", BoardState.state) AS state, 
                    BoardState.date AS date
                FROM 
                    Game
                INNER JOIN
                (
                    SELECT
                        id_game_fk,
                        cod_state AS state, 
                        tim_date AS date 
                    FROM 
                        State 
                    WHERE 
                        cod_state IN (2, 3, 4)

                ) BoardState ON Game.id = BoardState.id_game_fk
            )
        ) AS Binacle
        ORDER BY 
            Binacle.date DESC

;

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