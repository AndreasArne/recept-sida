USE `recipe_website`;
delete  from recipes where title like "%";

INSERT INTO recipes (title, instructions, description, cook_time) VALUES ("Flygande Jakob", 
	"Bena ur kyckling och lägg i form. Strö över sallads krydda|Vispa grädde ganska fast, blanda ner creme frieche och chilli  sås. Bre över kycklingingen.|Klipp bacon i lagom bitar och stek lätt. Strö jordnötter över formen.|Laga i ugnen i 30 min, 175c.|Server med ris och sallad.",
    "Detta är en jättegod Flygande Jakob utan banan",
    60);

INSERT INTO ingredients (label) VALUES ("Grillad kyckling");
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES
    ( (SELECT MAX(recipe_id) FROM recipes), (SELECT MAX(ingredient_id) FROM ingredients), "1");
INSERT INTO ingredients (label) VALUES ("Italiensk salladskrydda");
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES
    ( (SELECT MAX(recipe_id) FROM recipes), (SELECT MAX(ingredient_id) FROM ingredients), "2 krd");
INSERT INTO ingredients (label) VALUES ("Visp grädder");
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES
    ( (SELECT MAX(recipe_id) FROM recipes), (SELECT MAX(ingredient_id) FROM ingredients), "3 dl");
INSERT INTO ingredients (label) VALUES ("Creme freiche");
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES
    ( (SELECT MAX(recipe_id) FROM recipes), (SELECT MAX(ingredient_id) FROM ingredients), "1,5 dl");
INSERT INTO ingredients (label) VALUES ("Chilli sås");
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES
    ( (SELECT MAX(recipe_id) FROM recipes), (SELECT MAX(ingredient_id) FROM ingredients), "1,5 dl");
INSERT INTO ingredients (label) VALUES ("Bacon");
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES
    ( (SELECT MAX(recipe_id) FROM recipes), (SELECT MAX(ingredient_id) FROM ingredients), "2 paket");
INSERT INTO ingredients (label) VALUES ("Salta jordnötter");
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES
    ( (SELECT MAX(recipe_id) FROM recipes), (SELECT MAX(ingredient_id) FROM ingredients), "1 dl");


SELECT * FROM recipes;
SELECT * FROM recipe_ingredients;

