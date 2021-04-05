USE SudokuDB;

SET GLOBAL log_bin_trust_function_creators = 1;

DELIMITER $$
    DROP FUNCTION IF EXISTS fn_compareData;
    CREATE FUNCTION fn_compareData(pyNickname TEXT, pyPassword TEXT) RETURNS TEXT
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
    SET @newPasswordResult = IF((SELECT HEX(AES_ENCRYPT(pyPassword, pyNickname)) FROM User WHERE tex_nickname = pyNickname ) = @password, 1, 0);
    SET @result = (SELECT CONCAT(@nicknameResult, " ", @passwordResult, " " ,@rolResult, " ", @newPasswordResult));
    RETURN @result;

    END $$

DELIMITER ;