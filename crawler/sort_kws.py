from pymongo import MongoClient
from user_func import re_parse_all, delete_all_keywords
from parser import get_all_urls, increment_word, calculate_keywords, count_total_words
from crawler import get_all_html
import time

class bcolors:
    HEAD = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    OKBLUE = '\033[94m'

client = MongoClient('mongodb://127.0.0.1:3001/meteor')
db = client.meteor
db.word_count.drop()

url_list = get_all_urls()
start_time = time.time()
delete_all_keywords()
#increments each word in the html to word_count, storing the word and the number of repititions
for i in url_list:
	
	print bcolors.HEAD + ("Running through..... " + i) + bcolors.ENDC
	temp_list = get_all_html(i)
	for k in temp_list:
		try:
			print bcolors.OKGREEN + "Incrementing: " + k + bcolors.ENDC
			increment_word(k)
		except Exception, e:
			print bcolors.FAIL + "Invalid Entry" + bcolors.ENDC
			print e

#goes through the html and updates their weightage based on repititions in word_count, to keywords_coll, storing the word, user info, and weightage 

time_taken = time.time() - start_time
total = count_total_words()

start_time2 = time.time()
re_parse_all()
time_taken2 = time.time() - start_time2
#print bcolors.OKBLUE + "Now reparsing all users to update keyword weightage" + bcolors.ENDC

#sorts the bottom 80% of keywords in descending order
print calculate_keywords()

print bcolors.OKBLUE + "Took " + str(time_taken) + " seconds to calculate " + str(total) + " incrementations" + bcolors.ENDC
avg = time_taken / total
print bcolors.OKBLUE + "That is " + str(avg) + "seconds per increment" + bcolors.ENDC
print bcolors.OKGREEN + "Took " + str(time_taken2) + " seconds to calculate weightages for each word" + bcolors.ENDC
