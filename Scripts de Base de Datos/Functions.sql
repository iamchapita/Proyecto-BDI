USE SudokuDB;

SET GLOBAL log_bin_trust_function_creators = 1;

DROP FUNCTION IF EXISTS fn_compareData;
DROP FUNCTION IF EXISTS fn_updatePassword;
DELIMITER $$
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
    SET @newPasswordResult = IF((SELECT HEX(AES_ENCRYPT(pyNickname, pyNickname)) FROM User WHERE tex_nickname = pyNickname) = @password, 1, 0);
    SET @userState = IF((SELECT bit_state FROM User WHERE tex_nickname = pyNickname) = 1, 1, 0);
    SET @result = (SELECT CONCAT(@nicknameResult, " ", @passwordResult, " " ,@rolResult, " ", @newPasswordResult, " ", @userState));
    RETURN @result;

    END $$


    CREATE FUNCTION fn_updatePassword(pyOldNickname TEXT, pyNewNickname TEXT) RETURNS TEXT
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

    RETURN "";

    END $$

DELIMITER ;

-- SELECT fn_compareData("iampaisa", "contra");