from collections import Counter
from connector import database
import time
import numpy

def _insert_word(word):
	"""
	(string) --> boolean

	Inserts a word into the database with a count of zero, and returns true, unless it already exists, in which case it returns false.
	"""
	db = database()

	data = db.word_count.find_one({"word" : word})
	
	if data:
		raise LookupError("Word: %s already exists in database" % word)

	else:
		db.word_count.insert({"word": word, "total": 0})
		return True

def increment_word(word):
	"""
	(string) --> integer

	Adds one to the total number of a word unless it doesn't exist in the database, in which case it adds it, with an initial count of 1, returning an integer of it's count.
	"""
	db = database()
	word = str(word)
	data = db.word_count.find_one({"word" : word})

	if not data:
		_insert_word(word)
	
	data = db.word_count.find_one({"word" : word})
	if data:
		count = data.get("total") + 1
		#assigns a weightage that decreases the more time a word is incremented
		weightage = (float(1) / float(count)) * 100
		db.word_count.update({ "word": word}, {"word": word, "total": count, "weightage": weightage}) ### can this be more efficient without updating word? can weight be calculated onthego instead?
	return count

def count_total_words():
	"""
	() --> integer

	Counts the total number of words in the database that have been counted more than once, and returns an integer value.
	"""
	db = database()
	counter = 0

	for i in db.word_count.find({"total" : {'$gt' : 1} }):
		counter += i.get("total")
	
	return counter

def count_distinct_words():
	"""
	() --> integer

	Counts the number of distinct words in the database which have appeared more than once, and returns an integer value.
	"""
	db = database()
	counter = 0

	for i in db.word_count.find({"total" : {'$gt' : 1} }):
		counter += 1
	
	return counter

def _average_count():
	"""
	() --> integer

	Calculates the average number of repititions a words has in the database and returns an integer value.
	"""
	total = float(count_total_words()) 
	distinct = float(count_distinct_words())
	average = total / distinct
	print "Average: " + str(average)
	return average
	
def _std_count():
	"""
	() --> integer

	Calculates the standard deviation of the number of repititions a words has in the database and returns an integer value.
	"""
	
	db = database()
	data = []	
	count_list = []
	for i in db.word_count.find():
		if i.get("total"):
			count_list.append(i.get("total"))

	print "Standard Deviation: " + str(numpy.std(count_list))
	return numpy.std(count_list)

def calculate_keywords():
	"""
	() --> list

	Returns a list of all the keywords in the database which are less than 0.8414 standard deviations
	above the mean (bottom 80%)
	"""
	db = database()
	data = []

	for i in db.word_count.find():
		data.append(i)

	sorted_list = []
	avg_val = _average_count()
	std_dev = _std_count()
	num_list = []

	# creates a list with all the total values
	for i in range(len(data)):
		num_list = num_list + [data[i].get("total")]

	#print num_list
	#creates a list that lists the number of standard deviations from the mean each index is

	std_list = []
	for i in num_list:
		std_list.append((avg_val-i)/std_dev)
	
	#filters out any values greater than 0.8416 standard deviations above the mean from num_list
	for i in range(len(std_list)):
		if std_list[i] < -60.8416:
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
	print sorted_list
	return sorted_list