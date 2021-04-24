/* 
Contiene la definición de Funciones SQL que se utilizan para diferentes operaciones
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
*/

USE SudokuDB;

-- Se elimina el Procedimiento si existe
DROP PROCEDURE IF EXISTS sp_updatePassword;

-- Se cambia el delimitador
DELIMITER $$
-- Actualiza la contraseña
-- Se utiliza el nombre de usuario para encriptar la contraseña, por ende, cada vez que se cambia
-- el nombre de usuario se necesita cambiar el texto con el que se encripta la contraseña.
-- El texto(plano) de la contraseña seguirá intacto, sin embargo, la contraseña se encriptará con
-- el nuevo nombre de usuario
-- Se encarga de desencriptar la contraseña (con el nombre de usuario viejo) y encriptarla con el 
-- nuevo nombre de usuario.
-- @Param: pyOldNickname es un parámetro recibido desde python y contiene el nombre de usuario actual.
-- @Param: pyNewNickname es un parámetro recibido desde python y contiene el nombre de usuario nuevo.
CREATE PROCEDURE sp_updatePassword(IN pyOldNickname TEXT, IN pyNewNickname TEXT)
BEGIN
    
    -- Se obtiene la contraseña en texto plano y se almacena en la variable.
    SET @oldPassword = (
        SELECT 
            AES_DECRYPT(UNHEX(tex_password), pyOldNickname) 
        FROM 
            User 
        WHERE 
            tex_nickname = pyOldNickname
        );

    -- Realiza la actualización de la contraseña, encriptandola con el nuevo nombre de usuario.
    UPDATE 
        User 
    SET 
        tex_password = HEX(AES_ENCRYPT(@oldPassword, pyNewNickname)) 
    WHERE 
        tex_nickname = pyOldNickname;

END $$

DELIMITER ;