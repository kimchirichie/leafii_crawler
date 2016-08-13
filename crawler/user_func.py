from pymongo import MongoClient
from crawler import get_html, get_pdf, get_all_html
import time
import re

DB_URL = 'mongodb://127.0.0.1:3001/meteor'


def connect():
	client = MongoClient(DB_URL)
	return client.meteor	

class bcolors:
	HEAD = '\033[95m'
	OKGREEN = '\033[92m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	OKBLUE = '\033[94m'

def find_user_by_id(user_id):
	#returns a user's info with their id
	try:
		db = connect()
		#data = []
		if type(user_id) != str:
			raise TypeError 

		data = db.users.find_one({"_id" : user_id})
		if data:
			print data
			return data
		else:
			raise ValueError

	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid Input. Enter a valid user id as a string to use this function" + bcolors.ENDC)
		return False
	except ValueError:
		raise ValueError(bcolors.FAIL + "Invalid User ID" + bcolors.ENDC)
		return False

def find_user_by_email(email):
	#returns a user's info with their email
	try:
		db = connect()
		data = []

		if type(email) != str:
			raise TypeError 

		data = db.users.find_one({"emails.address" : email})
		if data:
			print data
			return data
		else:
			raise ValueError

	except TypeError:
		raise TypeError(bcolors.FAIL +"Invalid Input. Enter a valid email as a string to use this function" + bcolors.ENDC)
		return False
	except ValueError:
		raise ValueError(bcolors.FAIL + "No user found with that email" + bcolors.ENDC)
		return False

def find_user_by_name(name):
	#returns a list of all user's who have the input name as their first or last name
	try:
		start_time = time.time()
		
		db = connect()
		data = []
		if type(name) != str:
			raise TypeError 
		name = name.lower()

		for i in db.users.find():
			data.append(i)

		#seperates string into array of words	
		temp_name = re.findall(r'\w+', name)
		#temp_name_list = []
		user_list = []
		#changes search parameters based on number of words in search
		if len(temp_name) == 1:
			#searches for name in the first and last names of people in the profile
			for i in range(len(data)):
				temp_profile = data[i].get("profile")
				#print temp_profile.get("firstName")
				if name in temp_profile.get("firstName").lower() or name in temp_profile.get("lastName").lower() :
					#print temp_profile
					user_list = user_list + [data[i]]

		elif len(temp_name) == 2:
			#searches for the full name with exact match
			temp_firstName = temp_name[0]
			temp_lastName = temp_name[1]
			for i in range(len(data)):
				temp_profile = data[i].get("profile")
				if temp_firstName in temp_profile.get("firstName").lower() and temp_lastName in temp_profile.get("lastName").lower():  
					user_list = user_list + [data[i]]

		elif len(temp_name) > 2:
			#if more than three words are in name search, checks each word against first and last name 
			for i in range(len(data)):
				for c in range(len(temp_name)):
					temp_profile = data[i].get("profile")
					if temp_name[c] in temp_profile.get("firstName").lower() or temp_name[c] in temp_profile.get("lastName").lower():
						user_list = user_list + [data[i]]

		if len(user_list) == 0:
			raise ValueError

		for i in range(len(user_list)):
			print user_list[i]
			print ""
		return user_list

	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid Input. Enter a valid name as a string to use this function" + bcolors.ENDC)
		return False
	except ValueError:
		raise ValueError(bcolors.FAIL + "Name not found in database" + bcolors.ENDC)

def parse_user_site(user_id):
	#parses through a user's site 
	try:
		start_time = time.time()
		db = connect()
		if type(user_id) != str and type(user_id) != unicode:
			raise TypeError 
		user_id = str(user_id)
		key_dict = db.keywords_coll
		# data is user data from user collection.
		# we will be uploading our keywords to
		# keywords collection.
		data_temp = db.users.find_one({"_id" : user_id})
		if data_temp:
 			url_temp = data_temp.get("profile").get("url")
		else:
			raise ValueError

		#url_temp = (data_temp.get("profile").get("url"))
		print bcolors.OKGREEN + ("Running through..... " + url_temp) + bcolors.ENDC
		id_temp = (data_temp.get("_id"))
		#lastName_temp = (data_temp.get("profile").get("lastName"))
		#firstName_temp = (data_temp.get("profile").get("firstName"))
		#location_temp = (data_temp.get("profile").get("location"))
		#title_temp = (data_temp.get("profile").get("occupation"))

		# there will be 2 types of html,
		# from website, and from pdf
		tags_temp = get_all_html(url_temp) # this is keywords from the html
		#print tags_temp
		tagsPDF_temp = get_pdf(url_temp) # this is keywords from the pdf
		# print tagsPDF_temp

		seen = set()
		tags = []
		tagsPDF = []

		for item in tags_temp:
			if item not in seen:
				seen.add(item)
				tags.append(item)
				# print "seen:", seen
				# print "tags:", tags, "\n"

		for item in tagsPDF_temp:
			if item not in seen:
				seen.add(item)
				tagsPDF.append(item)
				# print "seen:", seen
				# print "tags:", tagsPDF, "\n"
		key_count = 0
		# update the mongoDB with html keywords, with another id generated
		seen2 = set()
		for k in range(len(tags)):
			#print ("Keywords Website:" + url_temp)
			seperateTags = tags[k].split(" ")
			for l in range(len(seperateTags)):
				if seperateTags[l] not in seen2:
					try:
						keyword_weightage = db.word_count.find({"word" : seperateTags[l].lower()})[0].get("weightage")
						seen2.add(seperateTags[l])
						key_db = {"keyword": seperateTags[l].lower(), "keyword_weightage": str(keyword_weightage), "url": url_temp, "user_id": id_temp, "type": "web"}
						key_count += 1
						print key_db
						# print seen2

						key_dict_id = key_dict.insert_one(key_db).inserted_id
					except:
						print bcolors.FAIL + "Unable to add keyword:" + seperateTags[l] + bcolors.ENDC
		# update the mongoDB with pdf keywords, with another id generated

		for j in range(len(tagsPDF)):
			#print ("Keywords PDF:" + url_temp)
			seperateTagspdf = tagsPDF[j].split(" ")
			for h in range(len(seperateTagspdf)):
				if seperateTagspdf[h] not in seen2:
					seen2.add(seperateTagspdf[h])
					key_db = {"keyword": seperateTagspdf[h].lower(), "url": url_temp, "user_id": id_temp, "type": "pdf"}
					key_count += 1
					print key_db

					key_dict_id = key_dict.insert_one(key_db).inserted_id

		

		print ""
		print bcolors.OKGREEN + ("Took %s seconds total" % (time.time() - start_time)) + bcolors.ENDC
		print bcolors.OKGREEN + "Went through one web page" + bcolors.ENDC
		print bcolors.OKGREEN + "Generated " + str(key_count) + " keywords" + bcolors.ENDC
		print bcolors.OKBLUE + "--------------------------------------------" + bcolors.ENDC + '\n'


	except Exception, e:
		print e
		print type(user_id)
		print user_id
		raise TypeError(bcolors.FAIL + "Invalid input type. Enter a valid user id as a string to use this function" + bcolors.ENDC)
		return False
	except ValueError:
		if user_exists == True:
			raise ValueError(bcolors.FAIL + "User has no url assosciated with account" + bcolors.ENDC)
		else:
			raise ValueError(bcolors.FAIL + "Invalid User ID" + bcolors.ENDC)
		return False

def parse_all_users():
	#parses through all the users' sites
	try:
		db = connect()
		data = []
		
		#gets a list of all user ids
		for i in db.users.find():
			parse_user_site(i.get("_id"))

		
		return True

	except Exception, e:
		print e
		return False

def delete_user_keywords(user_id):
	#deletes all of a single user's keywords
	try:
		db = connect()
		if type(user_id) != str:
			raise TypeError 
		data = db.users.find({"_id" : user_id})
		if data:
			db.keywords_coll.delete_many({"user_id": user_id})
		else:
			raise ValueError	

		return

	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid Input. Enter a valid user id as a string to use this function" + bcolors.ENDC)
		return False
	except ValueError:
		raise ValueError(bcolors.FAIL + "Invalid User ID" + bcolors.ENDC)
		return False

def delete_all_keywords():
	#deletes all keywords of all users
	try:
		db = connect()
		
		db.keywords_coll.delete_many({})
		#deletes existing data
		print "Entries Deleted"
		return True

	except Exception, e:
		print e
		return False

def re_parse_all():
	#deletes existing keywords and reparses through them all
	try:
		
		#wipes existing keywords
		delete_all_keywords()
		#parse all users
		parse_all_users()

	except Exception, e:
		print e
		return False
