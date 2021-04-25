/*
    @author gehernandezc@unah.hn, kenneth.cruz@unah.hn
    @version 0.1.3
    @date 2021/04/03
*/

USE SudokuDB; 

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