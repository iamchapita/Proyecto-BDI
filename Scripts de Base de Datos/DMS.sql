/*
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales 
    @version 1.0
*/


USE SudokuDB;

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE User;
/*TRUNCATE TABLE Game;
TRUNCATE TABLE Login;
TRUNCATE TABLE LogOff;
TRUNCATE TABLE State;
TRUNCATE TABLE Action;
TRUNCATE TABLE GameAction;*/
SET FOREIGN_KEY_CHECKS = 1;


INSERT INTO User(tex_nickname, tex_password, bit_rol) VALUES
    ("admin", HEX(AES_ENCRYPT("admin", "admin")), 1) --  Administrador
;


INSERT INTO SudokuBoard(tex_board) VALUES 
    ('000846032\n630297100\n284015960\n400508300\n398004005\n001009080\n160000070\n840601053\n700000004'), -- Este tiene solución
    ('210000400\n380400702\n000720000\n024806900\n000000000\n001203540\n000058000\n903004028\n008000057'), -- n00b original
    ('008100000\n602003094\n709080006\n800320060\n061070350\n030014009\n900040208\n120800905\n000001600'), -- easy
    ('010007200\n009024003\n007900060\n140070006\n900208001\n500040038\n090001600\n800490300\n001600050'), -- medium
    ('007200003\n000057860\n090300000\n709001200\n060070090\n001400306\n000006080\n046710000\n100003600'), -- hard
    ('000846532\n635297148\n284315967\n476528391\n398164725\n521739486\n163452879\n849671253\n752983614')  -- Está casi completo 917
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
    
