"""This module is to configure the app to connect with the database."""

from pymongo import MongoClient

DATABASE = MongoClient()
DEBUG = True
client = MongoClient('localhost', 27017)
