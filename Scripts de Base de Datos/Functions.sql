USE SudokuDB;

SET GLOBAL log_bin_trust_function_creators = 1;

DELIMITER $$
    DROP FUNCTION IF EXISTS fn_compareData;
    CREATE FUNCTION fn_compareData(tex_pynickname TEXT, tex_pypassword TEXT) RETURNS TINYINT
    BEGIN

        SET @password = (SELECT tex_password FROM User WHERE tex_nickname = tex_pynickname);
        SET @result = IF(@password = HEX(AES_ENCRYPT(tex_pypassword, tex_pynickname)), 1, 0);
        RETURN @result;

    END $$

DELIMITER ;

-- SELECT fn_compareData("admin", "admin") AS Data