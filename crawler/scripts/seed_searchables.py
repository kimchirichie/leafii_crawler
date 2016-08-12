from crawler.connector import database
import os

# define our DB, collection
db = database()

db.skill_coll.drop()
db.degree_coll.drop()

skillList = open(os.path.join(os.path.dirname(__file__), 'lists/skills_list.txt'),'r')
degreeList = open(os.path.join(os.path.dirname(__file__), 'lists/degree_lists.txt'),'r')


# for skill list collection
for i in skillList:
	key_db = {"skill": [i]}
	db.skill_coll.insert_one(key_db)

# for degree list collection
for i in degreeList:
	key_db = {"degree": [i]}
	db.degree_coll.insert_one(key_db)

skillList.close()
degreeList.close()