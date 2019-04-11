#!/usr/bin/python3
"""
Generate html code for recipe site.
"""
import os
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape



class SiteGenerator():
    """
    Class for generating html code for site
    """
    PROJECT_FOLDER = os.path.abspath(os.path.join(\
        os.path.dirname(__file__), '../'))
    HTDOCS_FOLDER = PROJECT_FOLDER + "/htdocs/"
    TEMPLATES_FOLDER = PROJECT_FOLDER + "/templates/"



    def __init__(self, resources, env):
        self.resources = resources
        self.jinja_env = env
        self.generators = []


    def generate_site(self):
        for gen in self.generators:
            gen.execute()


    @staticmethod
    def get_resources(project_folder=SiteGenerator.PROJECT_FOLDER):
        """
        Get misc. resources
        """
        config_file = project_folder + "/resources/config.json"
        return json.load(open(config_file, "r"))



    @staticmethod
    def create_jinja_env(templates_folder=SiteGenerator.TEMPLATES_FOLDER):
        """
        Create jinja2 environment
        """
        file_loader = FileSystemLoader(templates_folder)
        env = Environment(autoescape=select_autoescape(
            disabled_extensions=('txt',),
            default_for_string=True,
            default=True),
                          loader=file_loader
                          )
        return env



if __name__ == "__main__":
    jinja_env = SiteGenerator.create_jinja_env()
    resources = SiteGenerator.get_resources()
    site = SiteGenerator(resources, jinja_env)
    