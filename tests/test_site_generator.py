import pytest
import os
import builtins
from unittest.mock import mock_open, patch, call
from generator import site_generator as gen

@pytest.fixture(scope="function")
def SiteGenerator(jinja_env, resources):
    return gen.SiteGenerator(resources, jinja_env)



def test_SiteGenerator_attributes(resources, SiteGenerator):
    assert SiteGenerator.PROJECT_FOLDER.endswith("recept-sida")
    assert SiteGenerator.HTDOCS_FOLDER.endswith("recept-sida/htdocs/")
    assert SiteGenerator.TEMPLATES_FOLDER.endswith("recept-sida/generator/templates/")
    assert SiteGenerator.resources == resources
    assert "index" in SiteGenerator.generators



def test_create_html_files_list(SiteGenerator):
    folder = SiteGenerator.PROJECT_FOLDER + "/tests/tmp/" 
    content = [
        ("test.html", "code"),
        ("test2.html", "code2"),
        ("test3.html", "code3"),
    ]

    with patch('builtins.open', mock_open()) as m:
        SiteGenerator.create_html_files(folder, content)
        print(m.mock_calls)
        for file_content in content:
            assert call(folder + file_content[0], "w") in m.mock_calls
        handler = m()
        for file_content in content:
            assert call(file_content[1]) in handler.write.mock_calls



def test_create_html_files_tuple(SiteGenerator):
    folder = SiteGenerator.PROJECT_FOLDER + "/tests/tmp/" 
    content = "test.html", "code"

    with patch('builtins.open', mock_open()) as m:
        SiteGenerator.create_html_files(folder, content)
        m.assert_called_once_with(folder + content[0], 'w')
        handle = m()
        handle.write.assert_called_once_with(content[1])



def test_create_folder_if_not_exist(SiteGenerator, clean_tmp):
    SiteGenerator.create_folders_if_not_exist(
        SiteGenerator.PROJECT_FOLDER + "/tests/tmp/hej"
    )
    assert os.path.isdir(SiteGenerator.PROJECT_FOLDER + "/tests/tmp/hej")
    clean_tmp()



def test_create_folder_if_exist(SiteGenerator, clean_tmp):
    SiteGenerator.create_folders_if_not_exist(
        SiteGenerator.PROJECT_FOLDER + "/tests/tmp/hej"
    )
    SiteGenerator.create_folders_if_not_exist(
        SiteGenerator.PROJECT_FOLDER + "/tests/tmp"
    )
    assert os.path.isdir(SiteGenerator.PROJECT_FOLDER + "/tests/tmp/hej")
    clean_tmp()
