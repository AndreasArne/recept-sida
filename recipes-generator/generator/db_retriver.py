#!/usr/bin/python3
"""
Retrieve recipes from database
"""
import configparser
import mysql.connector

class DataRetriever():
    """
    Class for retrieve receipes from database
    """

    def __init__(self, connection):
        self.db = connection

    @staticmethod
    def get_db_config():
        """
        Get databse config from config file
        """
        config = configparser.ConfigParser()
        config.read('/mnt/c/Users/aar/.my.cnf')
        return dict(config["mysql"])

    @staticmethod
    def create_dev_connection():
        """
        Create DB connection for dev environment
        """
        config = DataRetriever.get_db_config()

        mydb = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            passwd=config["password"],
            database=config["database"]
        )
        return mydb
    
    def get_recipes(self):
        """
        Query DB for recipes
        """
        mycursor = self.db.cursor()
        
        mycursor.execute("SELECT * FROM recipes;")

        for x in mycursor:
            print(x)



if __name__ == "__main__":
    dr = DataRetriever(DataRetriever.create_dev_connection())
    dr.get_recipes()
