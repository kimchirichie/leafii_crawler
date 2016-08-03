import os
from pymongo import MongoClient

# define our DB, collection
client = MongoClient('mongodb://127.0.0.1:3001/meteor')

db = client.meteor


skillList = open(os.path.join(os.path.dirname(__file__), 'skills_list.txt'),'r')
degreeList = open(os.path.join(os.path.dirname(__file__), 'degree_lists.txt'),'r')


# for skill list collection

key_skill = db.skill_coll

for i in skillList:
	key_db = {"skill": [i]}
	key_dict_id = key_skill.insert_one(key_db).inserted_id

# for degree list collection

key_degree = db.degree_coll

for i in degreeList:
	key_db = {"degree": [i]}
	key_dict_id = key_degree.insert_one(key_db).inserted_id

skillList.close()
degreeList.close()