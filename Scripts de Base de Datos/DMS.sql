/*
    @author: kenneth.cruz@unah.hn
    @verion: 0.1.2
    @date 2021/03/30
*/


USE SudokuDB;

SET FOREIGN_KEY_CHECKS = 0;
/*TRUNCATE TABLE Login;*/
TRUNCATE TABLE User;
/*TRUNCATE TABLE Game;
TRUNCATE TABLE LogOff;
TRUNCATE TABLE State;
TRUNCATE TABLE Action;
TRUNCATE TABLE GameAction;*/
SET FOREIGN_KEY_CHECKS = 1;


INSERT INTO User(tex_nickname, tex_password, bit_rol) VALUES
    ("admin", HEX(AES_ENCRYPT("admin", "admin")), 1), --  Administrador
    ('iampaisa', HEX(AES_ENCRYPT('iampaisa', 'iampaisa')), 0) -- Usuario Alejandro
;
;

/* INSERT INTO User(tex_nickname, tex_password) VALUES
    ('erabbitt0', HEX(AES_ENCRYPT('mJByZXjyki', 'erabbitt0'))),
    ('gstudde1', HEX(AES_ENCRYPT('YdFODDUvP7', 'gstudde1'))),
    ('kkenen2', HEX(AES_ENCRYPT('xGfVpB', 'kkenen2'))),
    ('mopy3', HEX(AES_ENCRYPT('EQWT2hbqmL', 'mopy3'))),
    ('twands4', HEX(AES_ENCRYPT('SlfF6e5QXRJV', 'twands4'))),
    ('rdeards5', HEX(AES_ENCRYPT('UyYT8WyV', 'rdeards5'))),
    ('greisenberg6', HEX(AES_ENCRYPT('nAyNB45k2Z', 'greisenberg6'))),
    ('hwenban7', HEX(AES_ENCRYPT('CHsUNHRGrXJz', 'hwenban7'))),
    ('vhallet8', HEX(AES_ENCRYPT('HEd05CvByt76', 'vhallet8'))),
    ('iraymond9', HEX(AES_ENCRYPT('twn5ts', 'iraymond9'))),
    ('mshellarda', HEX(AES_ENCRYPT('i1FYF9', 'mshellarda'))),
    ('hthomasenb', HEX(AES_ENCRYPT('JPjD98XGFGX', 'hthomasenb'))),
    ('rbaldrickc', HEX(AES_ENCRYPT('u7UQM7xFj1Y', 'rbaldrickc'))),
    ('ksheppardd', HEX(AES_ENCRYPT('9hac0D2aw', 'ksheppardd')))
;

Desencriptar
Ejemplo para el usuario "erabbitt0": 
AES_DECRYPT(UNHEX('FAC1959052C12F533F4E43B422C62DA6'),'erabbitt0')
*/
    
