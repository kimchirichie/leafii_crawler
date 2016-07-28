from pymongo import MongoClient
from WebCrawlLeafiipdf import get_html, get_pdf
import time

start_time = time.time()

class bcolors:
    HEAD = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    OKBLUE = '\033[94m'

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

    tags_temp = get_html(url_temp) # this is keywords from the html
    tagsPDF_temp = get_pdf(url_temp) # this is keywords from the pdf

    seen=set()
    tags = []
    tagsPDF = []

    for item in set(tags_temp):
        if item not in seen:
            seen.add(item)
            tags.append(item)

    for item in set(tagsPDF_temp):
        if item not in seen:
            seen.add(item)
            tagsPDF.append(item)

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
