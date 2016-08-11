from pymongo import MongoClient
from crawler import get_html, get_pdf
import time
from collections import Counter
import numpy

DB_URL = 'mongodb://127.0.0.1:3001/meteor'


def connect():
	client = MongoClient(DB_URL)
	return client.meteor	

def get_all_urls():

	#Returns a list of all the urls users have submitted.
	db = connect()
	url_list = []
	data = []

	for i in db.users.find():
		if i.get("profile").get("url"):
			url_list.append(i.get("profile").get("url"))

	return url_list

def insert_word(word):

	#Inserts a word into the database with a count of zero, and returns true, unless it already exists, in which case it returns false.
	
	db = connect()

	data = db.word_count.find_one({"word" : word})
	
	if data:
		raise LookupError("Word: %s already exists in database" % word)

	else:
		db.word_count.insert({"word": word, "total": 0})
		return True
	
	
def increment_word(word):

	#Adds one to the total number of a word unless it doesn't exist in the database, in which case it adds it, with an initial count of 1, returning an integer of it's count.
	
	db = connect()
	word = str(word)
	data = db.word_count.find_one({"word" : word})

	if not data:
		insert_word(word)
	
	data = db.word_count.find_one({"word" : word})
	if data:
		temp_count = data.get("total") + 1
		#assigns a weightage that decreases the more time a word is incremented
		weightage = (float(1) / float(temp_count)) * 100
		db.word_count.update({ "word": word}, {"word": word, "total": temp_count, "weightage": weightage})  
	return temp_count

def count_total_words():
	
	#Counts the total number of words in the database that have been counted more than once, and returns an integer value.

	db = connect()
	counter = 0

	for i in db.word_count.find({"total" : {'$gt' : 1} }):
		counter += i.get("total")
	
	return counter

def count_distinct_words():

	#Counts the number of distinct words in the database which have appeared more than once, and returns an integer value.
	
	db = connect()
	counter = 0

	for i in db.word_count.find({"total" : {'$gt' : 1} }):
		counter += 1
	
	return counter

def average_count():
	
	#Calculates the average number of repititions a words has in the database and returns an integer value.

	total = float(count_total_words()) 
	distinct = float(count_distinct_words())
	average = total / distinct
	print "Average: " + str(average)
	return average
	
def std_count():

	#Calculates the standard deviation of the number of repititions a words has in the database and returns an integer value.

	
	db = connect()
	data = []	
	count_list = []
	for i in db.word_count.find():
		if i.get("total"):
			count_list.append(i.get("total"))

	print "Standard Deviation: " + str(numpy.std(count_list))
	return numpy.std(count_list)

def calculate_keywords():
	
	#Returns a list of all the keywords in the database which are less than 0.8414 standard deviations
	above the mean (bottom 80%)
	db = connect()
	data = []

	for i in db.word_count.find():
		data.append(i)

	sorted_list = []
	avg_val = average_count()
	std_dev = std_count()
	num_list = []

	# creates a list with all the total values
	for i in range(len(data)):
		num_list = num_list + [data[i].get("total")]

	#creates a list that lists the number of standard deviations from the mean each index is

	std_list = []
	for i in num_list:
		std_list.append((avg_val-i)/std_dev)

	#filters out any values greater than 0.8416 standard deviations above the mean from num_list
	filtered_list = []
	for i in range(len(std_list)):
		if std_list[i] < -0.8416:
			#assigns 0 value to values out of range
			num_list[i] = 0
	
	sorted_list = []
	highest_val = max(num_list)
	word_list = []
	#adds the highest name/value pair from num_list to sorted list then removes it from num_list 
	while highest_val != 0:

		for i in range(len(data)):
			if data[i].get("total") == highest_val and data[i].get("word") not in word_list and num_list[i] != 0:
				sorted_list.append([data[i].get("word"),data[i].get("total")])
				word_list.append(data[i].get("word"))
				num_list[i] = 0
				
		highest_val = max(num_list)
	for i in sorted_list:
		print i[0] + ": " + str(i[1])
	return sorted_list
