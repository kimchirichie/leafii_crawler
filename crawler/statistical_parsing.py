from pymongo import MongoClient
from WebCrawlLeafiipdf import get_html, get_pdf
import time
from collections import Counter
import numpy

def get_all_urls():
	"""
	() --> list

	Returns a list of all the urls users have submitted.
	"""
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
	"""
	(string) --> boolean

	Inserts a word into the database with a count of zero, and returns true, unless it already exists, in which case it returns false.
	"""
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
	"""
	(string) --> integer

	Adds one to the total number of a word unless it doesn't exist in the database, in which case it adds it, with an initial count of 1, returning an integer of it's count.
	"""
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

def count_total_words():
	"""
	() --> integer

	Counts the total number of words in the database and returns an integer value.
	"""
	start_time = time.time()
	client = MongoClient('mongodb://127.0.0.1:3001/meteor')
	db = client.meteor
	key_dict = db.word_count
	data = []	

	for i in db.word_count.find():
		data = data + [i]

	counter = 0
	for i in range(len(data)):
		counter += data[i].get("total")

	print counter
	return counter

def count_distinct_words():
	"""
	() --> integer

	Counts the number of distinct words in the database which have appeared at least once, and returns an integer value.
	"""
	start_time = time.time()
	client = MongoClient('mongodb://127.0.0.1:3001/meteor')
	db = client.meteor
	key_dict = db.word_count
	data = []	

	for i in db.word_count.find():
		data = data + [i]

	counter = 0
	for i in range(len(data)):
		if data[i].get("total") > 0:
			counter += 1

	print counter
	return counter

def average_count():
	"""
	() --> integer

	Calculates the average number of repititions a words has in the database and returns an integer value.
	"""
	print "total:"
	total = float(count_total_words()) 
	print "distinct:"
	distinct = count_distinct_words()
	print "average:"
	average = total / distinct
	print average
	return average
	
def std_count():
	"""
	() --> integer

	Calculates the standard deviation of the number of repititions a words has in the database and returns an integer value.
	"""
	start_time = time.time()
	client = MongoClient('mongodb://127.0.0.1:3001/meteor')
	db = client.meteor
	key_dict = db.word_count
	data = []	

	for i in db.word_count.find():
		data = data + [i]

	count_list = []
	for i in range(len(data)):
		count_list.append(data[i].get("total"))

	print numpy.std(count_list)
	return numpy.std(count_list)

def order_keywords():
	"""
	() --> list

	Returns a list of all the keywords in the database which have appeared at least once, 
	in descending order of their repitions, displaying both the keywords and the number of times they've appeared.
	"""
	start_time = time.time()
	client = MongoClient('mongodb://127.0.0.1:3001/meteor')
	db = client.meteor
	key_dict = db.word_count
	data = []

	for i in db.word_count.find():
		data = data + [i]
	
	temp_list = []

	#creates a list containing only the number values
	for i in range(len(data)):
		temp_list = temp_list + [data[i].get("total")]

	sorted_list = []
	highest_val = max(temp_list)
	word_list = []
	
	#sorts through the list by adding the highest value and word to a sorted list then removing it from temp_list
	while highest_val != 0:
		temp_list.remove(highest_val)
		
		for i in range(len(data)):
			if data[i].get("total") == highest_val and data[i].get("word") not in word_list:
				sorted_list.append([data[i].get("word"),data[i].get("total")])
				word_list.append(data[i].get("word"))
				
		highest_val = max(temp_list)

	for i in sorted_list:
		print i[0] + ": " + str(i[1])

def calculate_keywords(total_words):
	"""
	(integer) --> list

	Returns a list of all the keywords in the database which have met a statistical criteria
	"""
	start_time = time.time()
	client = MongoClient('mongodb://127.0.0.1:3001/meteor')
	db = client.meteor
	key_dict = db.word_count
	data = []

	for i in db.word_count.find():
		data = data + [i]

	sorted_list = []
	avg_val = average_count()
	std_dev = std_count()

	