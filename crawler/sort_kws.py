from pymongo import MongoClient
from user_func import re_parse_all
from statistical_parsing import increment_word, calculate_keywords

client = MongoClient('mongodb://127.0.0.1:3001/meteor')
db = client.meteor
db.word_count.drop()


#re_parse_all()

for i in db.keywords_coll.find():
	increment_word(i.get("keyword"))

calculate_keywords()
