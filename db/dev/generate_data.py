#!/usr/bin/python3
"""
Generate insert script script for mysql
"""
import json
DATA_FILE = "recipes.json"
SQL_FILE = "../scripts/insert_generated.sql"


# USE `recipe_website`;
SQL = "USE `recipe_website`;\n\
delete from recipes where title like '%';\n\
\n\
{insert}\n\
\n\
select ri.amount,i.label, r.*\n\
from recipe_ingredients as ri\n\
    INNER JOIN recipes as r\n\
        on ri.recipe_id = r.recipe_id\n\
    INNER JOIN ingredients as i\n\
        on ri.ingredient_id = i.ingredient_id;\n"


def build_recipe_string(recipe):
    insert_receipe = "INSERT INTO recipes (title, instructions, description, cook_time) VALUES (\n\
        '{title}',\n\
        '{instr}',\n\
        '{desc}',\n\
        '{cook_time}');\n"
    insert_ingredient_connect = "CALL connect_ingredient_dev('{label}','{amount}');\n"

    recipe_sql = insert_receipe.format(
        title=recipe["title"],
        instr="|".join(recipe["instr"]),
        desc=recipe["desc"],
        cook_time=recipe["cook_time"],
    )
    for ingredient in recipe["ingredients"]:
        recipe_sql += insert_ingredient_connect.format(
            label=ingredient["label"],
            amount=ingredient["amount"],
        )

    return recipe_sql

def generate_sql(recipes):
    global SQL
    recipes_list = []
    for recipe in recipes:
        recipes_list.append(build_recipe_string(recipe))

    print("\n".join(recipes_list))
    SQL = SQL.format(insert="\n".join(recipes_list))

def dump_sql_query():
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