#!/usr/bin/python3
"""
Generate html code for recipe site.
"""
import os
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from generator.html_generators import index_generator


class SiteGenerator():
    """
    Class for generating html code for site
    """
    PROJECT_FOLDER = os.path.abspath(os.path.join(\
        os.path.dirname(__file__), '../'))
    HTDOCS_FOLDER = PROJECT_FOLDER + "/htdocs/"
    TEMPLATES_FOLDER = PROJECT_FOLDER + "/generator/templates/"



    def __init__(self, resources, env):
        self.resources = resources
        self.jinja_env = env
        self.generators = {
            "index": index_generator.IndexGenerator(
                self.jinja_env,
            ),
        }



    def generate_site(self):
        """
        Execute all html generators and create html files
        """
        for gen_name, gen in self.generators.items():
            content = gen.execute(self.resources)
            folder = self.HTDOCS_FOLDER + gen.FOLDER_IN_HTDOCS
            self.create_folders_if_not_exist(folder)
            self.create_html_files(folder, content)



    @staticmethod
    def create_html_files(folder, content):
        """
        Check if need to create multiple html files or one
        """
        if isinstance(content, list):
            for file_content in content:
                file_path = folder + file_content[0]
                SiteGenerator.write_html_to_file(file_path, file_content[1])
        else:
            file_path = folder + content[0]
            SiteGenerator.write_html_to_file(file_path, content[1])



    @staticmethod
    def write_html_to_file(path, html):
        """
        Write html code to file
        """
        with open(path, "w") as fh:
            fh.write(html)



    @staticmethod
    def create_folders_if_not_exist(path):
        """
        If folder and parents don't exist, create them
        """
        os.makedirs(path, exist_ok=True)



    @staticmethod
    def get_resources(project_folder=None):
        """
        Get misc. resources
        """
        if project_folder is None:
            project_folder = SiteGenerator.PROJECT_FOLDER

        config_file = project_folder + "/resources/config.json"
        return json.load(open(config_file, "r"))



    @staticmethod
    def create_jinja_env(templates_folder=None):
        """
        Create jinja2 environment
        """
        if templates_folder is None:
            templates_folder = SiteGenerator.TEMPLATES_FOLDER

        
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
    site.generate_site()
    