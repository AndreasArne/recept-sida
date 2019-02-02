#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tests the class used to retrieve recipes data from the database
"""
import unittest
import json
import mock
from context import html_generator as gen
from context import db_retriever as db_r
from context import PROJECT_FOLDER


class HtmlGeneratorTestCase(unittest.TestCase):
    """
    Test suite for testing the class for generating html files
    """

    def setUp(self):
        pass

    def test_write_html_file(self):
        """
        Test Generator.write_html_to_file() 
        """
        db = mock.create_autospec(db_r.DataRetriever)
        generator = gen.Generator(db, gen.Generator.create_jinja_env())

        m = mock.mock_open()
        with mock.patch('builtins.open', m, create=False):
            generator.write_html_to_file("test-name-000", "content")

        m.assert_called_once_with(PROJECT_FOLDER + "/htdocs/recipes/test-name-000", "w")
        handler = m()
        handler.write.assert_called_with("content")

    def test_generate_html(self):
        """
        Test Generator.generate_recipe_html()
        """
        db = mock.create_autospec(db_r.DataRetriever)
        generator = gen.Generator(db, gen.Generator.create_jinja_env())

        with open(PROJECT_FOLDER + "/resources/recipes.json", "r") as json_file:
            db.query_all_recipes.return_value = json.loads(json_file.read())

        # pylint: disable=C0330
        recipes_html = [
        """<!doctype html>
<html lang="sv">
<head>
    <meta charset="utf-8">
    <title>Flygande Jakob</title>
    <link rel="stylesheet" href="style/style.css">
    <link rel="icon" href="favicon.ico">
</head>
<body>
    <h1>Flygande Jakob</h1>

<script type="text/javascript" src="js/main.js"></script>
</body>
</html>""",
        """<!doctype html>
<html lang="sv">
<head>
    <meta charset="utf-8">
    <title>Creme brulee</title>
    <link rel="stylesheet" href="style/style.css">
    <link rel="icon" href="favicon.ico">
</head>
<body>
    <h1>Creme brulee</h1>

<script type="text/javascript" src="js/main.js"></script>
</body>
</html>"""]
        for indx, recipe in enumerate(generator.generate_recipe_html()):
            self.assertEqual(
                recipe[1], 
                recipes_html[indx]
            )

if __name__ == '__main__':
    unittest.main(verbosity=2)
