CREATE TABLE 'miempresa'.'empleados'
(
    'id' INT NOT NULL AUTO_INCREMENT ,
    'nombre' VARCHAR(100) NOT NULL ,
    'apellidos' VARCHAR(100) NOT NULL ,
    'telefono' VARCHAR(100) NOT NULL ,
    'email' VARCHAR(100) NOT NULL ,
    PRIMARY KEY ('id')
) ENGINE = InnoDB