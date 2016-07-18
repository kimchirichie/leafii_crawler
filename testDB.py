from pymongo import MongoClient
import datetime
#import pprint
#import string
from WebCrawlLeafiipdf import get_html, get_pdf

client = MongoClient('mongodb://127.0.0.1:3001/meteor')

db = client.meteor
data = []

for i in  db.users.find():
	data = data + [i]
	#print i
#print data[0]
key_dict = db.keywords

for i in range(len(data)):
		data_temp = data[i]
		url_temp = (data_temp.get("profile").get("url"))
		id_temp = (data_temp.get("_id"))
		tags = get_html(url_temp)
		tagsPDF = get_pdf(url_temp)

		for k in range(len(tags)):

			key_db = {"keywords": tags[k], "url": url_temp, "user_id": id_temp, "pdf": "False"}

			print key_db

			key_dict_id = key_dict.insert_one(key_db).inserted_id

			#print (key_dict_id)

		for j in range(len(tagsPDF)):

			key_db = {"keywords": tagsPDF[j], "url": url_temp, "user_id": id_temp, "pdf": "True"}

			#print key_db

			key_dict_id = key_dict.insert_one(key_db).inserted_id

			#print (key_dict_id)



