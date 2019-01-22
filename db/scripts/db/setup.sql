-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema recipe_website
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `recipe_website` ;

-- -----------------------------------------------------
-- Schema recipe_website
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recipe_website` DEFAULT CHARACTER SET utf8 COLLATE utf8_swedish_ci ;
USE `recipe_website` ;


CREATE USER IF NOT EXISTS 'dev'@'%' IDENTIFIED BY 'pass';

GRANT ALL ON `recipe_website`.* TO 'dev';

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
