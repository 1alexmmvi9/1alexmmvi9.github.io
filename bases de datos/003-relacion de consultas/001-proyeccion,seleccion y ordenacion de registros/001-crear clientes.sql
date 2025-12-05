CREATE TABLE `miempresa`. (
    `id` INT(10) NOT NULL AUTO_INCREMENT ,
    `nombre` VARCHAR(255) NOT NULL ,
    `apellidos` VARCHAR(255) NOT NULL ,
    `email` VARCHAR(255) NOT NULL ,
    `poblacion` VARCHAR(255) NOT NULL ,
    `fecahdenacimiento` DATE NOT NULL ,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;