USE `recipe_website`;

-- -----------------------------------------------------
-- Table `recipe_website`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`recipes` (
  `recipe_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `instructions` MEDIUMTEXT NOT NULL,
  `description` MEDIUMTEXT NOT NULL,
  `cook_time` INT NULL,
  `portions` VARCHAR(10) NULL,
  PRIMARY KEY (`recipe_id`),
  UNIQUE INDEX `id_UNIQUE` (`recipe_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`category` (
  `category_id` INT NOT NULL AUTO_INCREMENT,
  `label` VARCHAR(100) NOT NULL UNIQUE,
  PRIMARY KEY (`category_id`),
  UNIQUE INDEX `idtags_UNIQUE` (`category_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`ingredients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`ingredients` (
  `ingredient_id` INT NOT NULL AUTO_INCREMENT,
  `label` VARCHAR(75) NOT NULL UNIQUE,
  PRIMARY KEY (`ingredient_id`),
  UNIQUE INDEX `id_UNIQUE` (`ingredient_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`recipe_ingredients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`recipe_ingredients` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `recipe_id` INT NOT NULL,
  `ingredient_id` INT NOT NULL,
  `amount` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `recipe_id_idx` (`recipe_id` ASC),
  INDEX `ingredient_id_idx` (`ingredient_id` ASC),
  CONSTRAINT `recipe_ri`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `recipe_website`.`recipes` (`recipe_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `ingredient_ri`
    FOREIGN KEY (`ingredient_id`)
    REFERENCES `recipe_website`.`ingredients` (`ingredient_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`recipe_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`recipe_category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `recipe_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `recipe_id_idx` (`recipe_id` ASC),
  INDEX `category_id_idx` (`category_id` ASC),
  CONSTRAINT `recipe_rc`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `recipe_website`.`recipes` (`recipe_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `category_rc`
    FOREIGN KEY (`category_id`)
    REFERENCES `recipe_website`.`category` (`category_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`images`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`images` (
  `image_id` INT NOT NULL AUTO_INCREMENT,
  `recipe_id` INT NOT NULL,
  `file_name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`image_id`),
  UNIQUE INDEX `id_UNIQUE` (`image_id` ASC),
  INDEX `recipe_id_idx` (`recipe_id` ASC),
  CONSTRAINT `recipe_i`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `recipe_website`.`recipes` (`recipe_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Stored Procedure `recipe_website`.`connect_ingredient_dev`
-- Used when inserting data during creation of DB.
-- -----------------------------------------------------
DELIMITER //
CREATE PROCEDURE connect_ingredient_dev (
	IN in_label VARCHAR(75),
    IN in_amount VARCHAR(45)
)
BEGIN
	IF NOT EXISTS (SELECT label FROM ingredients WHERE label = in_label) THEN
		INSERT INTO ingredients (label) VALUES (in_label);

	INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES (
		(SELECT MAX(recipe_id) FROM recipes),
		(SELECT ingredient_id FROM ingredients where label = in_label),
		in_amount
	);
	END IF;
END //
DELIMITER ;