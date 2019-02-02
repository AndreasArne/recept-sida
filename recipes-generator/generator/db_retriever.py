#!/usr/bin/python3
"""
Retrieve recipes from database
"""
from configparser import ConfigParser
import mysql.connector
import json

class DataRetriever():
    """
    Class for retrieve receipes from database
    """

    def __init__(self, connection):
        self.db = connection

    @staticmethod
    def get_db_config():
        """
        Get databse config from config file
        """
        config = ConfigParser()
        config.read('/mnt/c/Users/aar/.my.cnf')
        return dict(config["mysql"])

    @classmethod
    def create_dev_connection(cls):
        """
        Create DB connection for dev environment
        """
        config = cls.get_db_config()

        mydb = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            passwd=config["password"],
            database=config["database"]
        )
        return mydb

    def query_recipe_data(self, recipe_id, recipe):
        """
        Query recipe data, ingredients, tags, images
        """
        cursor = self.db.cursor()

        # Images
        cursor.execute("SELECT file_name FROM images \
            WHERE recipe_id = %s", (recipe_id,)
        )
        recipe["images"] = [row[0] for row in cursor]
        
        # Tags
        cursor.execute("SELECT t.label FROM tags as t\
            INNER JOIN recipe_tag as rt\
                ON rt.tag_id = t.id\
            WHERE rt.recipe_id = %s", (recipe_id,)
        )
        recipe["tags"] = [row[0] for row in cursor]

        # Ingredients
        cursor.execute("SELECT ri.amount, i.label FROM ingredients as i\
            INNER JOIN recipe_ingredient as ri\
                ON ri.ingredient_id = i.id\
            WHERE ri.recipe_id = %s", (recipe_id,)
        )
        recipe["ingredients"] = [row[0] + " " + row[1] for row in cursor]

    def query_all_recipes(self):
        """
        Query DB for recipes
        """
        recipe_cursor = self.db.cursor(buffered=True)

        recipe_cursor.execute("SELECT * FROM recipes;")
        recipe_columns = recipe_cursor.column_names

        for r_row in recipe_cursor:
            recipe = dict(zip(recipe_columns, r_row))
            recipe["instructions"] = recipe["instructions"].split("|")
            recipe_id = recipe["id"]

            self.query_recipe_data(recipe_id, recipe)

            yield recipe


if __name__ == "__main__":
    dr = DataRetriever(DataRetriever.create_dev_connection())
    for x in dr.query_all_recipes():
        print(x)
