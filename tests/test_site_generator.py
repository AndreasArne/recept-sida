import pytest
from generator import site_generator as gen

@pytest.fixture
def SiteGenerator(jinja_env, resources):
    return gen.SiteGenerator(resources, jinja_env)

def test_SiteGenerator_attributes(resources, SiteGenerator):
    assert SiteGenerator.PROJECT_FOLDER.endswith("recept-sida")
    assert SiteGenerator.HTDOCS_FOLDER.endswith("recept-sida/htdocs/")
    assert SiteGenerator.TEMPLATES_FOLDER.endswith("recept-sida/generator/templates/")
    assert SiteGenerator.resources == resources
    assert "index" in SiteGenerator.generators
