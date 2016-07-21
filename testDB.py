from pymongo import MongoClient
from WebCrawlLeafiipdf import get_html, get_pdf

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

print "Running through data now"
for i in range(len(data)):
    data_temp = data[i]

    # obtain url and id from user data

    url_temp = (data_temp.get("profile").get("url"))
    print ("Running through:" + url_temp)
    id_temp = (data_temp.get("_id"))

    # there will be 2 types of html,
    # from website, and from pdf

    tags = get_html(url_temp) # this is keywords from the html
    tagsPDF = get_pdf(url_temp) # this is keywords from the pdf

    # update the mongoDB with html keywords, with another id generated

    for k in range(len(tags)):
        print ("Keywords Website:" + url_temp)
        seperateTags = tags[k].split(" ")
        for l in range(len(seperateTags)):
            key_db = {"Keyword": seperateTags[l].lower(), "url": url_temp, "user_id": id_temp, "type": "web"}
            print key_db

            key_dict_id = key_dict.insert_one(key_db).inserted_id

    # update the mongoDB with pdf keywords, with another id generated

    for j in range(len(tagsPDF)):
        print ("Keywords PDF:" + url_temp)
        seperateTagspdf = tagsPDF[j].split(" ")
        for h in range(len(seperateTagspdf)):
            key_db = {"Keyword": seperateTagspdf[h].lower(), "url": url_temp, "user_id": id_temp, "type": "pdf"}
            print key_db

            key_dict_id = key_dict.insert_one(key_db).inserted_id
