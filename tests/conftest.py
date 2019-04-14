import pytest
import os
import json
import shutil
from jinja2 import Environment, FileSystemLoader, select_autoescape



PROJECT_FOLDER = os.path.abspath(os.path.join(\
    os.path.dirname(__file__), '../'))
HTDOCS_FOLDER = PROJECT_FOLDER + "/htdocs/"
TEMPLATES_FOLDER = PROJECT_FOLDER + "/generator/templates/"



def read_test_resource(file_name):
    index_file = PROJECT_FOLDER + "/tests/resources/" + file_name
    with open(index_file, "r") as fh:
        return fh.read()



@pytest.fixture(scope="session")
def clean_tmp():
    def delete_folder():
        shutil.rmtree(PROJECT_FOLDER + "/tests/tmp")
    return delete_folder



@pytest.fixture(scope="session")
def index_html():
    """
    Get index.html code from file
    """
    return read_test_resource("index.html")



@pytest.fixture(scope="session")
def jinja_env():
    """
    Create jinja2 environment
    """
    
    file_loader = FileSystemLoader(TEMPLATES_FOLDER)
    env = Environment(autoescape=select_autoescape(
        disabled_extensions=('txt',),
        default_for_string=True,
        default=True),
                      loader=file_loader
                      )
    return env



@pytest.fixture(scope="session")
def resources():
    """
    Get resource config
    """
    config_file = PROJECT_FOLDER + "/resources/config.json"
    return json.load(open(config_file, "r"))
