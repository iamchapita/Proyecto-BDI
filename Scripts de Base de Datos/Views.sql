/*
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales 
    @version 1.0
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