from pymongo import MongoClient
import datetime
#import pprint
#import string
from WebCrawlLeafiipdf import get_html

client = MongoClient('mongodb://127.0.0.1:3001/meteor')

db = client.meteor

data = ["your data here"]

key_dict = db.keywords
for i in range(len(data)):
	data_temp = data[i]
	url_temp = (data_temp.get("profile").get("url"))
	id_temp = (data_temp.get("_id"))

	tags = get_html(url_temp)

	key_db = {"keywords": tags, "url": url_temp, "user_id": id_temp}

	key_dict_id = key_dict.insert_one(key_db).inserted_id
	#print (key_dict_id)




