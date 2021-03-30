SELECT 
    @@session.block_encryption_mode;

SET 
    @@session.block_encryption_mode = "aes-256-ecb";

SELECT
    @@session.block_encryption_mode;

SET
    @var = "Texto de prueba para encriptar";

SET
    @pass = "Esta es la contraseña para encriptar";

SET @encrypted = AES_ENCRYPT(@var, @pass);

SELECT AES_DECRYPT(@encrypted, @pass);