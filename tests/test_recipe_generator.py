#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tests the class used to retrieve recipes data from the database
"""
import unittest
import json
import mock
from context import recipe_generator as gen
from context import db_retriever as db_r
from context import PROJECT_FOLDER


class RecipeGeneratorTestCase(unittest.TestCase):
    """
    Test suite for testing the class for generating html files
    """
    RESOURCES_RECPIES = PROJECT_FOLDER + "/tests/resources/recipes_html/"
    RECIPE_TEMPLATE_FOLDER = PROJECT_FOLDER + "/generator/templates/"

    def setUp(self):
        self.maxDiff = None


    @staticmethod
    def read_file(filename):
        """
        readfiles
        """
        with open(filename, "r") as fh:
            return fh.read()

    def test_write_html_file(self):
        """
        Test Generator.write_html_to_file() 
        """
        db = mock.create_autospec(db_r.DataRetriever)
        generator = gen.RecipeGenerator(db, gen.RecipeGenerator.create_jinja_env(self.RECIPE_TEMPLATE_FOLDER))
        folder = "/htdocs/recept/"

        m = mock.mock_open()
        with mock.patch('builtins.open', m, create=False):
            generator.write_html_to_file(folder, "test-name-000.html", "content")

        m.assert_called_once_with(folder + "test-name-000.html", "w")
        handler = m()
        handler.write.assert_called_with("content")

    def test_create_filename(self):
        """
        Test Generator.generate_recipe_html()
        """
        test_dict = [{
            "title": "test name",
            "id": 3
        }, {
            "title": "test_name",
            "id": "2"
        }]
        filename = gen.RecipeGenerator.create_recipe_filename(test_dict[0])
        self.assertEqual(filename, "test-name-3.html")

        filename = gen.RecipeGenerator.create_recipe_filename(test_dict[1])
        self.assertEqual(filename, "test_name-2.html")

    def test_generate_html(self):
        """
        Test RecipeGenerator.generate_recipe_html()
        """
        db = mock.create_autospec(db_r.DataRetriever)
        generator = gen.RecipeGenerator(db, gen.RecipeGenerator.create_jinja_env(self.RECIPE_TEMPLATE_FOLDER))

        with open(PROJECT_FOLDER + "/resources/recipes.json", "r") as json_file:
            recipes_json = json.loads(json_file.read())
            for indx_rec, recipe in enumerate(recipes_json):
                for indx_ingr, ingredient in enumerate(recipe["ingredients"]):
                    recipes_json[indx_rec]["ingredients"][indx_ingr] = ingredient["amount"] + " " + ingredient["label"]
            db.query_all_recipes.return_value = recipes_json

        for recipe_tuple in generator.generate_recipe_html():
            self.assertEqual(
                recipe_tuple[1],
                self.read_file(self.RESOURCES_RECPIES + recipe_tuple[0])
            )

if __name__ == '__main__':
    unittest.main(verbosity=2)
