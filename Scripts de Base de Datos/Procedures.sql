USE SudokuDB;

DROP PROCEDURE IF EXISTS sp_updatePassword;

DELIMITER $$
CREATE PROCEDURE sp_updatePassword(IN pyOldNickname TEXT, IN pyNewNickname TEXT)
BEGIN
    
    SET @oldPassword = (
        SELECT 
            AES_DECRYPT(UNHEX(tex_password), pyOldNickname) 
        FROM 
            User 
        WHERE 
            tex_nickname = pyOldNickname
        );

    UPDATE 
        User 
    SET 
        tex_password = HEX(AES_ENCRYPT(@oldPassword, pyNewNickname)) 
    WHERE 
        tex_nickname = pyOldNickname;

END $$

DELIMITER ;