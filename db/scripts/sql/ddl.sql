USE `recipe_website`;

-- -----------------------------------------------------
-- Table `recipe_website`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `instructions` MEDIUMTEXT NOT NULL,
  `description` MEDIUMTEXT NOT NULL,
  `cook_time` INT NULL,
  `portions` VARCHAR(10) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`tags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`tags` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `label` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `label_UNIQUE` (`label` ASC),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`ingredients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`ingredients` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `label` VARCHAR(75) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`recipe_ingredient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`recipe_ingredient` (
  `recipe_id` INT NOT NULL,
  `ingredient_id` INT NOT NULL,
  `amount` VARCHAR(45) NOT NULL,
  INDEX `recipe_id_idx` (`recipe_id` ASC),
  INDEX `ingredient_id_idx` (`ingredient_id` ASC),
  PRIMARY KEY (`recipe_id`, `ingredient_id`),
  CONSTRAINT `recipe_ri`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `recipe_website`.`recipes` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `ingredient_ri`
    FOREIGN KEY (`ingredient_id`)
    REFERENCES `recipe_website`.`ingredients` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`recipe_tag`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`recipe_tag` (
  `recipe_id` INT NOT NULL,
  `tag_id` INT NOT NULL,
  PRIMARY KEY (`recipe_id`, `tag_id`),
  INDEX `recipe_id_idx` (`recipe_id` ASC),
  CONSTRAINT `recipe_rc`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `recipe_website`.`recipes` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_website`.`images`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_website`.`images` (
  `recipe_id` INT NOT NULL,
  `file_name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`file_name`),
  INDEX `recipe_id_idx` (`recipe_id` ASC),
  UNIQUE INDEX `file_name_UNIQUE` (`file_name` ASC),
  CONSTRAINT `recipe_i`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `recipe_website`.`recipes` (`id`)
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

	INSERT INTO recipe_ingredient (recipe_id, ingredient_id, amount) VALUES (
		(SELECT MAX(r.id) FROM recipes as r),
		(SELECT i.id FROM ingredients as i where label = in_label),
		in_amount
	);
	END IF;
END //
DELIMITER ;


-- -----------------------------------------------------
-- Stored Procedure `recipe_website`.`connect_tag_dev`
-- Used when inserting data during creation of DB.
-- -----------------------------------------------------
DELIMITER //
CREATE PROCEDURE connect_tag_dev (
	IN in_label VARCHAR(75)
)
BEGIN
	IF NOT EXISTS (SELECT label FROM tags WHERE label = in_label) THEN
		INSERT INTO tags (label) VALUES (in_label);

	INSERT INTO recipe_tag (recipe_id, tag_id) VALUES (
		(SELECT MAX(r.id) FROM recipes as r),
		(SELECT t.id FROM tags as t where label = in_label)
	);
	END IF;
END //
DELIMITER ;