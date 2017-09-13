-- MySQL Script generated by MySQL Workbench
-- Wed Sep 13 13:56:36 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema full_friendsdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema full_friendsdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `full_friendsdb` DEFAULT CHARACTER SET utf8 ;
USE `full_friendsdb` ;

-- -----------------------------------------------------
-- Table `full_friendsdb`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `full_friendsdb`.`friends` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `age` INT NULL,
  `friend_since` VARCHAR(255) NULL,
  `year` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
