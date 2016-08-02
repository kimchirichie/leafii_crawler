from pymongo import MongoClient
from WebCrawlLeafiipdf import get_html, get_pdf
import time
from collections import Counter

def get_all_urls():
	start_time = time.time()
	client = MongoClient('mongodb://127.0.0.1:3001/meteor')
	db = client.meteor
	url_list = []
	data = []

	for i in db.users.find():
		data = data + [i]
	
	for i in range(len(data)):
		data_temp = data[i]
		url_list.append(data_temp.get("profile").get("url"))
		print url_list[i]
	return url_list

def insert_word(word):
	start_time = time.time()
	client = MongoClient('mongodb://127.0.0.1:3001/meteor')
	db = client.meteor
	key_dict = db.word_count
	data = []

	for i in db.word_count.find():
		data = data + [i]

	word_list = []
		
	for i in range(len(data)):
		word_list.append(data[i].get("word"))

	if word not in word_list:
		db.word_count.insert({"word": word, "total": 0})
		return True
	else:
		return False
	
def increment_word(word):
	start_time = time.time()
	client = MongoClient('mongodb://127.0.0.1:3001/meteor')
	db = client.meteor
	key_dict = db.word_count
	data = []	

	for i in db.word_count.find():
		data = data + [i]

	word_list = []
		
	for i in range(len(data)):
		word_list.append(data[i].get("word"))

	if word not in word_list:
		db.word_count.insert({"word": word, "total": 1})
		return 1
	else:
		for i in range(len(data)):
			if data[i].get("word") == word:
				temp_count = data[i].get("total") + 1
				db.word_count.update({ "word": word}, {"word": word, "total": temp_count})  
		return temp_count

#def count_words(word):

#def count_total_words():

#def count_distinct_words():

#def average_count():

#def std_count():

#def calulate_keywords()


start_time = time.time()
client = MongoClient('mongodb://127.0.0.1:3001/meteor')
db = client.meteor
key_dict = db.word_count
data = []
#db.createCollection("word_count")

for i in db.word_count.find():
	data = data + [i]

for i in range(len(data)):
	print data[i]