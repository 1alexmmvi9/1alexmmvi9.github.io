CREATE TABLE `miempresa`.`pedidos` (
    `id` INT(10) NOT NULL AUTO_INCREMENT ,
    `fecha` DATE NOT NULL ,
    `clientes_apellidos` INT(10) NOT NULL ,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;