"""
Import all modules from ../generator/ so test modules don't need to import path
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#pylint: disable=unused-import, wrong-import-position
from generator.html_generators import recipe_generator
from generator import db_retriever

PROJECT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))