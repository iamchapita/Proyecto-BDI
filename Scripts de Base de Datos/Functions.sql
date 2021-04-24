/* 
Contiene la definición de Funciones SQL que se utilizan para diferentes operaciones
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
 */
USE SudokuDB;

-- Se establece a 1 la variable para permitir que las funciones modifiquen las tablas
SET GLOBAL log_bin_trust_function_creators = 1;

-- Se eliminan las funciones
DROP FUNCTION IF EXISTS fn_compareData;
DROP FUNCTION IF EXISTS fn_getNickNameByState;
DROP FUNCTION IF EXISTS fn_getNicknameById;

-- Se cambia el delimitador
DELIMITER $$
    -- Comprueba el estado del usuario (credenciales pasadas por parámetro) en la base de datos
    -- @param: pyNickname recibe el nombre de usuario, es llamada desde python
    -- @param: pyPassword recibe la contraseña del usuario, es llamada desde python
    -- Retorna texto
    CREATE FUNCTION fn_compareData(pyNickname TEXT, pyPassword TEXT) RETURNS TEXT
    BEGIN

    -- Establece una variable con el resultado de buscar en la base de datos el nombre de usuario
    -- que fue pasado por parámetro.
    SET @nicknameResult = IF(pyNickname IN (SELECT tex_nickname FROM User), 1, 0);
    -- Se obtiene la contraseña del usuario utilizando el nombre de usuario recibido por parámetro
    SET @password = (
        SELECT
            tex_password
        FROM
            User
        WHERE
            tex_nickname = pyNickname
    );
    -- Se compara la contraseña guardada en la base de datos con la contraseña pasada por parámetro
    SET @passwordResult = IF(@password = HEX(AES_ENCRYPT(pyPassword, pyNickname)), 1, 0);
    -- Se obtiene el rol del usuario (las credenciales pasadas por parámetro)
    SET @rolResult = IF((SELECT bit_rol FROM User WHERE tex_nickname = pyNickname) = 1, 1, 0);
    -- Se comprueba si el usuario debe o no cambiar su contraseña
    -- Si es verdadero, significa que el usuario ingresó al sistema por primera vez
    SET @newPasswordResult = IF((SELECT HEX(AES_ENCRYPT(pyNickname, pyNickname)) FROM User WHERE tex_nickname = pyNickname) = @password, 1, 0);
    -- Se comprueba el estado del usuario (Habilitado o Deshabilitado)
    SET @userState = IF((SELECT bit_state FROM User WHERE tex_nickname = pyNickname) = 1, 1, 0);
    -- Se establece una variable con los resultados de las operaciones anteriores
    SET @result = (SELECT CONCAT(@nicknameResult, " ", @passwordResult, " " ,@rolResult, " ", @newPasswordResult, " ", @userState));
    -- Se retorna la variable con los resultados
    RETURN @result;

    END $$

-- Se cambia el delimitador
DELIMITER $$
    -- Obtiene el nombre de un usuario por medio del id del Juego
    CREATE FUNCTION fn_getNickNameByState(id_game_fk BIGINT UNSIGNED) RETURNS VARCHAR(40)
    BEGIN 
        RETURN (
                    SELECT  
                        User.tex_nickname AS nickname
                    FROM
                        User
                    INNER JOIN 
                        Game ON User.id = Game.id_user_fk
                    WHERE 
                        Game.id = id_game_fk
                )
            ;
    END $$
-- Se cambia el delimitador
DELIMITER ;

-- Se cambia el delimitador
DELIMITER $$
    -- Obtiene el nombre de un usuario por medio de su identificador
    CREATE FUNCTION fn_getNicknameById(id_user_fk BIGINT UNSIGNED) RETURNS VARCHAR(40)
    BEGIN 
        RETURN (
                    SELECT  
                        tex_nickname AS nickname
                    FROM
                        User
                    WHERE 
                        id = id_user_fk
                )
            ;
    END $$
    
-- Se cambia el delimitador
DELIMITER ;