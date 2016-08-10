from pymongo import MongoClient
from user_func import re_parse_all
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
#Runs through a list of all the urls, getting a list of all the words and incrementing them 
user_list= []
invalid_list = []
for i in url_list:
	print bcolors.HEAD + ("Running through..... " + i) + bcolors.ENDC
	temp_list = get_all_html(i)
	for k in temp_list:
		try:
			print bcolors.OKGREEN + "Incrementing: " + k + bcolors.ENDC
			increment_word(k)
		except Exception, e:
			print bcolors.FAIL + "Invalid Entry" + bcolors.ENDC
			invalid_list.append(k)
			print e
#sorts the bottom 80% of keywords in descending order
print calculate_keywords()
time_taken = time.time() - start_time
total = count_total_words()
print invalid_list
print bcolors.OKBLUE + "Took " + str(time_taken) + " seconds to calculate " + str(total) + " incrementations" + bcolors.ENDC
avg = time_taken / total
print bcolors.OKBLUE + "That is " + str(avg) + "seconds per increment"