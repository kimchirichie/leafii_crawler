from pymongo import MongoClient

DB_URL = 'mongodb://127.0.0.1:3001/meteor'

def database():
	client = MongoClient(DB_URL)
	return client.meteor