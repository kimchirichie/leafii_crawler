from pymongo import MongoClient
from WebCrawlLeafiipdf import get_html, get_pdf

def user_info(user_id)
	try:
		# define our DB, collection
		client = MongoClient('mongodb://127.0.0.1:3001/meteor')

		db = client.meteor

		data = []

		# data is user data from user collection.
		# we will be uploading our keywords to
		# keywords collection.
		user_data = db.users.find({"user_id": user_id}):
		return user_data


def parse_user_site(user_id)
	try:
		delete_user_keywords(user_id)

				# define our DB, collection
		client = MongoClient('mongodb://127.0.0.1:3001/meteor')

		db = client.meteor

		data = []

		# data is user data from user collection.
		# we will be uploading our keywords to
		# keywords collection.
		for i in db.users.find({"user_id": user_id}):
			data = data + [i]

		# Now, data[0] is data for 1st user.

		# our collection is called keywords
		key_dict = db.keywords_coll

		print bcolors.HEAD + "========= STARTING INITIAL PARSE =========" + bcolors.ENDC + "\n"
		print bcolors.OKBLUE + "run this program once to initialize MongoDB" + bcolors.ENDC
		print bcolors.OKBLUE + "operating multiple times will result in duplicating data" + bcolors.ENDC + '\n'

		for i in range(len(data)):
			data_temp = data[i]

			# obtain url and id from user data

			url_temp = (data_temp.get("profile").get("url"))
			print bcolors.OKGREEN + ("Running through..... " + url_temp) + bcolors.ENDC
			id_temp = (data_temp.get("_id"))

			# there will be 2 types of html,
			# from website, and from pdf

			tags = get_html(url_temp) # this is keywords from the html
			tagsPDF = get_pdf(url_temp) # this is keywords from the pdf

			# update the mongoDB with html keywords, with another id generated

			for k in range(len(tags)):
				# print ("Keywords Website:" + url_temp)
				seperateTags = tags[k].split(" ")
				for l in range(len(seperateTags)):
					key_db = {"keyword": seperateTags[l].lower(), "url": url_temp, "user_id": id_temp, "type": "web"}
					print key_db

					key_dict_id = key_dict.insert_one(key_db).inserted_id

			# update the mongoDB with pdf keywords, with another id generated

			for j in range(len(tagsPDF)):
				# print ("Keywords PDF:" + url_temp)
				seperateTagspdf = tagsPDF[j].split(" ")
				for h in range(len(seperateTagspdf)):
					key_db = {"keyword": seperateTagspdf[h].lower(), "url": url_temp, "user_id": id_temp, "type": "pdf"}
					print key_db

					key_dict_id = key_dict.insert_one(key_db).inserted_id

			print bcolors.OKBLUE + "--------------------------------------------" + bcolors.ENDC + '\n'
			return true

	except:
		print "Can't find user"
		return false

def parse_all_users()
	try:
		# define our DB, collection
		client = MongoClient('mongodb://127.0.0.1:3001/meteor')

		db = client.meteor

		data = []

		# data is user data from user collection.
		# we will be uploading our keywords to
		# keywords collection.
		for i in db.users.find():
			data = data + [i]

		# Now, data[0] is data for 1st user.

		# our collection is called keywords
		key_dict = db.keywords_coll

		print bcolors.HEAD + "========= STARTING INITIAL PARSE =========" + bcolors.ENDC + "\n"
		print bcolors.OKBLUE + "run this program once to initialize MongoDB" + bcolors.ENDC
		print bcolors.OKBLUE + "operating multiple times will result in duplicating data" + bcolors.ENDC + '\n'

		for i in range(len(data)):
			data_temp = data[i]

			# obtain url and id from user data

			url_temp = (data_temp.get("profile").get("url"))
			print bcolors.OKGREEN + ("Running through..... " + url_temp) + bcolors.ENDC
			id_temp = (data_temp.get("_id"))

			# there will be 2 types of html,
			# from website, and from pdf

			tags = get_html(url_temp) # this is keywords from the html
			tagsPDF = get_pdf(url_temp) # this is keywords from the pdf

			# update the mongoDB with html keywords, with another id generated

			for k in range(len(tags)):
				# print ("Keywords Website:" + url_temp)
				seperateTags = tags[k].split(" ")
				for l in range(len(seperateTags)):
					key_db = {"keyword": seperateTags[l].lower(), "url": url_temp, "user_id": id_temp, "type": "web"}
					print key_db

					key_dict_id = key_dict.insert_one(key_db).inserted_id

			# update the mongoDB with pdf keywords, with another id generated

			for j in range(len(tagsPDF)):
				# print ("Keywords PDF:" + url_temp)
				seperateTagspdf = tagsPDF[j].split(" ")
				for h in range(len(seperateTagspdf)):
					key_db = {"keyword": seperateTagspdf[h].lower(), "url": url_temp, "user_id": id_temp, "type": "pdf"}
					print key_db

					key_dict_id = key_dict.insert_one(key_db).inserted_id

			print bcolors.OKBLUE + "--------------------------------------------" + bcolors.ENDC + '\n'


		print bcolors.OKGREEN + ("Took %s seconds total" % (time.time() - start_time)) + bcolors.ENDC
		print bcolors.OKGREEN + "Went through " + str(len(data)) + " web pages" + bcolors.ENDC
		print bcolors.OKGREEN + "Generated " + str(db.keywords_coll.count()) + " keywords" + bcolors.ENDC
		return true

	except:
		print "ERROR: Can't parse users"
		return false

def delete_user_keywords(user_id)
	try:
		# adds all of a user's keywords to users_keywords
		user_keywords = []
		for i in range(len(key_dict))
			if user_id in key_dict[i]
				user_keywords.append(key_dict[i])

		#deletes existing user data
		result = key_dict.delete_many({"user_id": user_id})
        print result "entries deleted"
        return user_keywords
	except:
		print "Can't delete keyword"

def delete_all_keywords()
	try:
		#deletes existing data
		result = key_dict.delete_many({})
        print result "Entries deleted"
        return true

	except:
		print "Can't delete keyword from all users"
		return false

def re_parse_all()
	try:
		#wipes existing keywords
		delete_all_keywords()

		# define our DB, collection
		client = MongoClient('mongodb://127.0.0.1:3001/meteor')

		db = client.meteor

		data = []

		# data is user data from user collection.
		# we will be uploading our keywords to
		# keywords collection.
		for i in db.users.find():
			data = data + [i]

		# Now, data[0] is data for 1st user.

		# our collection is called keywords
		key_dict = db.keywords_coll

		print bcolors.HEAD + "========= REPARSING DATA=========" + bcolors.ENDC + "\n"
		print bcolors.OKBLUE + "run this program once to initialize MongoDB" + bcolors.ENDC
		print bcolors.OKBLUE + "operating multiple times will result in duplicating data" + bcolors.ENDC + '\n'

		for i in range(len(data)):
			data_temp = data[i]

			# obtain url and id from user data

			url_temp = (data_temp.get("profile").get("url"))
			print bcolors.OKGREEN + ("Running through..... " + url_temp) + bcolors.ENDC
			id_temp = (data_temp.get("_id"))

			# there will be 2 types of html,
			# from website, and from pdf

			tags = get_html(url_temp) # this is keywords from the html
			tagsPDF = get_pdf(url_temp) # this is keywords from the pdf

			# update the mongoDB with html keywords, with another id generated

			for k in range(len(tags)):
				# print ("Keywords Website:" + url_temp)
				seperateTags = tags[k].split(" ")
				for l in range(len(seperateTags)):
					key_db = {"keyword": seperateTags[l].lower(), "url": url_temp, "user_id": id_temp, "type": "web"}
					print key_db

					key_dict_id = key_dict.insert_one(key_db).inserted_id

			# update the mongoDB with pdf keywords, with another id generated

			for j in range(len(tagsPDF)):
				# print ("Keywords PDF:" + url_temp)
				seperateTagspdf = tagsPDF[j].split(" ")
				for h in range(len(seperateTagspdf)):
					key_db = {"keyword": seperateTagspdf[h].lower(), "url": url_temp, "user_id": id_temp, "type": "pdf"}
					print key_db

					key_dict_id = key_dict.insert_one(key_db).inserted_id

			print bcolors.OKBLUE + "--------------------------------------------" + bcolors.ENDC + '\n'
			return true
			
	except:
		print "ERROR: Wipe and Parse Failed"
		return false

def find_user_by_name
	
	return user_info(user_id)

def find_user_by_email
	
	return user_info(user_id)

