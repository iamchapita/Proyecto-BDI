USE SudokuDB;

DROP PROCEDURE IF EXISTS sp_verifyLogin;
/*
DELIMITER $$

CREATE PROCEDURE sp_verifyLogin (IN pyNickname TEXT, IN pyPassword TEXT, OUT result TEXT)
BEGIN

    SET @nicknameResult = IF(pyNickname IN (SELECT tex_nickname FROM User), 1, 0);
    SET @password = (
        SELECT
            tex_password
        FROM
            User
        WHERE
            tex_nickname = pyNickname
    );
    SET @passwordResult = IF(@password = HEX(AES_ENCRYPT(pyPassword, pyNickname)), 1, 0);
    SET @rolResult = IF((SELECT bit_rol FROM User WHERE tex_nickname = pyNickname) = 1, 1, 0);
    SET result = (SELECT CONCAT(" ", @nicknameResult, " ", @passwordResult, " " ,@rolResult));
    
END$$

DELIMITER ;

SET @result = "";
CALL sp_verifyLogin("admin", "admin", @result);
SELECT @result AS Resultado; */