#!/usr/bin/python3
"""
Generate insert script script for mysql
"""
import json
DATA_FILE = "recipes.json"
SQL_FILE = "db/insert_generated.sql"


# USE `recipe_website`;
SQL = "USE `recipe_website`;\n\
delete from recipes where title like '%';\n\
\n\
{insert}\n\
\n\
select ri.amount,i.label, img.*\n\
from recipe_ingredient as ri\n\
    INNER JOIN recipes as r\n\
        on ri.recipe_id = r.id\n\
    INNER JOIN ingredients as i\n\
        on ri.ingredient_id = i.id\n\
	INNER JOIN images as img\n\
		on r.id = img.recipe_id;\n"


def build_recipe_string(recipe):
    """
    Build SQL string for a recipe
    """
    insert_receipe = "INSERT INTO recipes (title, instructions, description, portions, cook_time) VALUES (\n\
        '{title}',\n\
        '{instr}',\n\
        '{desc}',\n\
        '{portions}',\n\
        '{cook_time}');\n"
    insert_ingredient_connect = "CALL connect_ingredient_dev('{label}','{amount}');\n"
    insert_image = "INSERT INTO images (recipe_id, file_name) VALUES (\n\
        (SELECT MAX(r.id) FROM recipes as r),\n\
        '{file_name}');\n"
    insert_tag_connect = "CALL connect_tag_dev('{label}');\n"


    # Recipe
    recipe_sql = insert_receipe.format(
        title=recipe["title"],
        instr="|".join(recipe["instr"]),
        desc=recipe["desc"],
        cook_time=recipe["cook_time"],
        portions=recipe["portions"],
    )

    # Ingredients
    for ingredient in recipe["ingredients"]:
        recipe_sql += insert_ingredient_connect.format(
            label=ingredient["label"],
            amount=ingredient["amount"],
        )
    # Images
    for img in recipe["images"]:
        recipe_sql += insert_image.format(
            file_name=img,
        )
    # Tags
    for tag in recipe["tags"]:
        recipe_sql += insert_tag_connect.format(
            label=tag,
        )

    return recipe_sql

def generate_sql(recipes):
    """
    Build SQL string for all recipes from file
    """
    global SQL
    recipes_list = []
    for recipe in recipes:
        recipes_list.append(build_recipe_string(recipe))

    SQL = SQL.format(insert="\n".join(recipes_list))

def dump_sql_query():
    """
    Write SQL string to file
    """
    with open(SQL_FILE, "w") as fh:
        fh.write(SQL)

def get_data():
    """
    Read json data from file
    """
    with open(DATA_FILE, "r") as fh:
        return json.load(fh)

def generate_script():
    """
    Main file for script
    """
    recipes = get_data()
    generate_sql(recipes)
    dump_sql_query()


if __name__ == "__main__":
    generate_script()
