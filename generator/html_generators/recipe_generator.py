#!/usr/bin/python3
"""
Generate html files from DB data
"""
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from generator.db_retriever import DataRetriever

class RecipeGenerator():
    """
    Class for generating html files
    """

    def __init__(self, db_retriever, env):
        self.db_r = db_retriever
        self.jinja = env


    @staticmethod
    def create_jinja_env(recipe_template_folder):
        """
        Create jinja2 environment
        """
        file_loader = FileSystemLoader(recipe_template_folder)
        env = Environment(autoescape=select_autoescape(
            disabled_extensions=('txt',),
            default_for_string=True,
            default=True),
                          loader=file_loader
                          )
        return env

    @staticmethod
    def create_recipe_filename(recipe):
        """
        Create filename from title and id
        """
        return "{title}-{id}.html".format(
            title=recipe["title"].replace(" ", "-"),
            id=recipe["id"],
        )

    def generate_recipe_html(self):
        """
        Use jinja2 to generate html files
        """
        template = self.jinja.get_template("recipe.html")
        for recipe in self.db_r.query_all_recipes():
            yield self.create_recipe_filename(recipe),\
            template.render(recipe=recipe)

    def write_html_to_file(self, folder, file_name, recipe):
        """
        Write recipe to html file
        """
        file_path = folder + file_name
        with open(file_path, "w") as fh:
            fh.write(recipe)

if __name__ == "__main__":
    RECIPE_TEMPLATE_FOLDER = os.path.abspath(os.path.join(\
            os.path.dirname(__file__))) + "../templates/"
    RECIPE_OUTPUT_FOLDER = os.path.abspath(os.path.join(\
        os.path.dirname(__file__), '../..')) + "/htdocs/recept/"
    db_r = DataRetriever(DataRetriever.create_dev_connection())
    g = Generator(db_r, Generator.create_jinja_env(RECIPE_TEMPLATE_FOLDER))
    for name, recipe_html in g.generate_recipe_html():
        g.write_html_to_file(RECIPE_OUTPUT_FOLDER, name, recipe_html)
