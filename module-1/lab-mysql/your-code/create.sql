#Challenge 2 - Create the Database and Tables

-- -----------------------------------------------------
-- Table `lab_cars`.`Cars`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `lab_cars`.`Cars` 
(`car_id` VARCHAR(255) NULL DEFAULT NULL,
  `manufacturer` VARCHAR(255) NULL DEFAULT NULL,
  `modelo` VARCHAR(255) NULL DEFAULT NULL,
  `year` SMALLINT(6) NULL DEFAULT NULL,
  `color` VARCHAR(255) NULL DEFAULT NULL);


-- -----------------------------------------------------
-- Table `lab_cars`.`Costumers`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `lab_cars`.`Costumers` (
  `id_costumer` SMALLINT(6) NULL DEFAULT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `phone_num` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `city` VARCHAR(255) NULL DEFAULT NULL,
  `state` VARCHAR(255) NULL DEFAULT NULL,
  `country` VARCHAR(255) NULL DEFAULT NULL,
  `zip` INT(11) NULL DEFAULT NULL);

-- -----------------------------------------------------
-- Table `lab_cars`.`Invoices`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `lab_cars`.`Invoices` (
  `invoice_num` INT(11) NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `car` VARCHAR(255) NULL DEFAULT NULL,
  `costumer` SMALLINT(6) NULL DEFAULT NULL,
  `salesperson` INT(11) NULL DEFAULT NULL);

-- -----------------------------------------------------
-- Table `lab_cars`.`Salesperson`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `lab_cars`.`Salesperson` (
  `id_staff` INT(11) NULL DEFAULT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `store` VARCHAR(255) NULL DEFAULT NULL);
