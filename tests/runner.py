#!/usr/bin/python3
"""
Run test suites for game of life
"""
import unittest
import sys

import test_recipe_generator

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_recipe_generator))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

# exit with status
sys.exit(not result.wasSuccessful())
