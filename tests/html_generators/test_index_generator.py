import pytest
from generator.html_generators import index_generator as gen



@pytest.fixture
def IndexGenerator(jinja_env):
    return gen.IndexGenerator(jinja_env)



def test_generate_html_code(IndexGenerator, resources, index_html):
    html_code = IndexGenerator.generate_html_code(resources)
    assert html_code == index_html



def test_execute(IndexGenerator, resources, index_html):
    file_name, html_code = IndexGenerator.execute(resources)
    assert html_code == index_html
    assert  file_name == "index.html"