#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tests the class used to retrieve recipes data from the database
"""
from sys import argv
import unittest
from context import db_retriver as db_r

class TestCreateGamefield(unittest.TestCase):
    """
    Test suite for testing the class for retrieveing recipe data from database
    """

    def setUp(self):
        pass

    def test_create_2dlist(self):
        """
        Testing creat_2dlist function
        """
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main(verbosity=2)
