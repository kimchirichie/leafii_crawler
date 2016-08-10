import urllib2
import urllib
from cStringIO import StringIO
import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pymongo import MongoClient
import re
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

client = MongoClient('mongodb://127.0.0.1:3001/meteor')

db = client.meteor

class bcolors:
	HEAD = '\033[95m'
	OKGREEN = '\033[92m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	OKBLUE = '\033[94m'

def is_number(number):
	try:
		float(number)
		return True
	except ValueError:
		return False

# Download the .pdf resume and parse it
def get_pdf_content(url, page_nums=[0]):
	resume = urllib.URLopener()
	# Just in case, try opening the .pdf with
	# the url found
	try:
		if type(url) != str and type(url) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure to input the url as a string" + bcolors.ENDC) 
	try:
		# If we are redirected, follow it
		r = requests.get(url)
		# Call the download file, "resume.pdf"
		resume.retrieve(r.url, "resume.pdf")
		content = ""

		# Use the PDFMiner package to grab the
		# text from the .pdf file
		rsrcmgr = PDFResourceManager()
		retstr = StringIO()
		codec = 'utf-8'
		laparams = LAParams()
		device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
		# Open the downloaded file here,
		# ---> 'rb' means hard read, regardless of the unicode
		pdf = file("resume.pdf", 'rb')
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		password = ""
		maxpages = 1
		caching = True
		pagenos = set()
		for page in PDFPage.get_pages(pdf, pagenos, maxpages=maxpages, password=password, caching=caching,
									  check_extractable=True):
			interpreter.process_page(page)
		# Store the text as a string here
		text = retstr.getvalue()

		# Lower the text, for easier parse
		text = text.lower()
		# p = file("resume.pdf", "rb")
		# pdf = PyPDF2.PdfFileReader(p)
		# for page_num in page_nums:
		#   content += pdf.getPage(page_num).extractText()

		# Use find_skills function, to parse the
		# text as it would with the HTML
		lstSkills = find_skills(text)

		# Return the string of Skills
		return lstSkills
	# If we run into an error, continue on, and
	# move onto the next try statement
	except:
		pass
	# We found that some people don't like to
	# add "www" with their http://, which we
	# then attempt to fix here
	try:

		# Add www. to the string here
		url = url[:7] + "www." + url[7:]  #######################Try request

		# Do the same as the above try statement
		resume.retrieve(url, "resume.pdf")
		content = ""

		rsrcmgr = PDFResourceManager()
		retstr = StringIO()
		codec = 'utf-8'
		laparams = LAParams()
		device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
		pdf = file("resume.pdf", 'rb')
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		password = ""
		maxpages = 1
		caching = True
		pagenos = set()
		for page in PDFPage.get_pages(pdf, pagenos, maxpages=maxpages, password=password, caching=caching,
									  check_extractable=True):
			interpreter.process_page(page)
		text = retstr.getvalue()
		text = text.lower()
		# p = file("resume.pdf", "rb")
		# pdf = PyPDF2.PdfFileReader(p)
		# for page_num in page_nums:
		#   content += pdf.getPage(page_num).extractText()
		lstSkills = find_skills(text)
		return lstSkills
	except:
		pass

	# Finally try a non-redirected route, and
	# parse the .pdf as we did in the first
	# try statement
	try:
		url = url[:7] + url[10:]
		resume.retrieve(url, "resume.pdf")
		content = ""
		rsrcmgr = PDFResourceManager()
		retstr = StringIO()
		codec = 'utf-8'
		laparams = LAParams()
		device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
		pdf = file("resume.pdf", 'rb')
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		password = ""
		maxpages = 1
		caching = True
		pagenos = set()
		for page in PDFPage.get_pages(pdf, pagenos, maxpages=maxpages, password=password, caching=caching,
									  check_extractable=True):
			interpreter.process_page(page)
		text = retstr.getvalue()
		text = text.lower()
		# p = file("resume.pdf", "rb")
		# pdf = PyPDF2.PdfFileReader(p)
		# for page_num in page_nums:
		#   content += pdf.getPage(page_num).extractText()
		lstSkills = find_skills(text)
		return lstSkills
	# Return an empty array, indicating that
	# we were unable to retrieve any
	# information from your resume
	except:
		print bcolors.FAIL + "Error in get_pdf_content, double check pdf link" + bcolors.ENDC
		return []


# Find the the .pdf link
def find_pdf(str, urlStr):
	# If we find a .pdf in the html
	# String, then try to find the
	# entire link here
	try:
		if (type(str) != str and type(str) != unicode) or (type(urlStr) != str  and type(urlStr) != unicode):
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure both input fields are strings" + bcolors.ENDC)

	if (".pdf" in str):
		# print "PDF file was found"
		# a = Str[Str.find(".pdf")]
		# print a
		loop = True

		# Create a pivot point, from where
		# the "." starts in ".pdf", then
		# work backwards
		pivotPoint = str.find(".pdf")
		counter = 0
		pdfURL = ""
		temp_urlStr = urlStr

		# Remove hard carraige, and hard character
		# returns in the
		temp_urlStr = temp_urlStr.replace("\r", "")
		temp_urlStr = temp_urlStr.replace("\n", "")

		# Make a loop that will find the link from
		# the ".pdf" point to the href link
		while loop:
			if (("f" == str[pivotPoint - counter]) and
					("e" == str[pivotPoint - counter - 1]) and
					("r" == str[pivotPoint - counter - 2]) and
					("h" == str[pivotPoint - counter - 3])):

				# Set a variable that will contain the pdfURL
				pdfURL = str[pivotPoint - counter + 3:pivotPoint + 4]

				# return the pdfURL we have found
				if not pdfURL.find(temp_urlStr) == -1:
					return pdfURL

				# return the pdfURL stopping at the http
				if not pdfURL.find("http") == -1:
					return pdfURL

				if not pdfURL.find(".com") == -1:
					return pdfURL

				if not pdfURL.find(".org") == -1:
					return pdfURL

				# return the pdfURL, by adding the
				# original url link given by the user
				# (their online portfolio link) and
				# add it to the pdfURL
				else:
					urlStr = urlStr.replace("\r", "")
					urlStr = urlStr.replace("\n", "")
					pdfURL = urlStr + "/" + pdfURL
					return pdfURL
			else:
				counter += 1
	else:
		return False


def find_degree(bodyStr):
	
	try:
		if type(bodyStr) != str and type(bodyStr) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Input should be a string" + bcolors.ENDC)
	keywords_body = []

	# find words that are matching with our degree vocabulary
	#degreeFile = open("degree_lists.txt", "r")
	data = []
	degreeFile = []
	for i in db.degree_coll.find():
		data = data + [i]
	#print data
	for j in range(len(data)):
		degreeFile = degreeFile + data[j].get("degree")
	#print degreeFile

	for i in degreeFile:
		a = i
		a = a.replace('\r', "")
		a = a.replace('\n', "")
		a = str(a)
		# fixed formatting of vocabularies, it is unable to find if not fixed.
		if a.lower() in bodyStr:
			keywords_body = keywords_body + [a]
		else:
			#print "error in find_degree"
			() # do nothing
	#degreeFile.close()
	return keywords_body


def find_skills(bodyStr):
	try:
		if type(bodyStr) != str and type(bodyStr) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure input is a string" + bcolors.ENDC)
	skill_words = []

	# find words that are matching with our skills vocabulary
	#lstSkills = open("skills_list.txt", "r")
	data = []
	lstSkills = []
	for i in db.skill_coll.find():
		data = data + [i]
	for j in range(len(data)):
		lstSkills = lstSkills + data[j].get("skill")

	counter = True

	# we will first check if the person has "skill" defined,
	# and if "skill" is not found, then try to collect all the vocabularies appearing in the body.
	if ("skill" in bodyStr):
		skill_tag = bodyStr[bodyStr.find("skill"):]

		# if "skill" was defined, then it will collect vocabularies after the definition
		for i in lstSkills:
			temp_i = i
			temp_i = temp_i.replace('\n', "")
			temp_i = temp_i.replace('\r', "")
			temp_i = str(temp_i)
			# fix the format as usual

			if temp_i.lower() in skill_tag:
				skill_words = skill_words + [temp_i]

			# this is special case, when person has C and/or R skills.
			# those skills (one worded) can be found by adding spaces
			# eg. "c" -> " c "
			# Did not add "GO" language skill due to huge problem.
			if " c " in skill_tag and counter == True:
				skill_words = skill_words + ["C"]
				counter = False

			if " r " in skill_tag and counter == True:
				skill_words = skill_words + ["R"]
				counter = False

			else:
				()
	else:
		# it will do the same, but for entire bodyStr, which will take longer time.
		for i in lstSkills:
			temp_i = i
			temp_i = temp_i.replace('\n', "")
			temp_i = temp_i.replace('\r', "")
			temp_i = str(temp_i)
			if temp_i.lower() in bodyStr:
				skill_words = skill_words + [temp_i]

			if " c " in bodyStr and counter == True:
				skill_words = skill_words + ["C"]
				counter = False

			if " r " in bodyStr and counter == True:
				skill_words = skill_words + ["R"]
				counter = False

			else:
				()
	return skill_words


def search_meta_keywords(keywordStr):
	try:
		if type(keywordStr) != str and type(keywordStr) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure input is a string" + bcolors.ENDC)
	keyword_contents = []
	# print (keywordStr.find('meta name="keywords" '))
	# Check if meta tags are in the html
	# quotation within quotation...
	if (keywordStr.find("meta name=\"keywords\"") != -1):
		# find where the meta tags start, (position)
		starting_k_contents = keywordStr.find("meta name=\"keywords\"") + 30

		# find where the meta tags end, (position)
		ending_k_contents = keywordStr.find(">", starting_k_contents)

		temp_keywords = keywordStr[starting_k_contents:ending_k_contents - 2]

		# replace and fix some of the formatting
		temp_keywords = temp_keywords.replace("\"","")
		temp_keywords = temp_keywords.split(",") # now temp_keywords are junks of keywords.
		temp_keywords = temp_keywords.replace("", "")
		keyword_contents = keyword_contents + temp_keywords
		return keyword_contents

	else:
		# if meta tags are not found, return []
		return keyword_contents


def title_find(titleStr):
	try:
		if type(titleStr) != str and type(titleStr) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure input is a string" + bcolors.ENDC)
	keywords = []

	# It will collect "titles" in between headers
	# honestly we just collected things that are appearing frequently
	# if function finds it, (not -1) then add it to the keywords.

	if (titleStr.find("pc.user") != -1 or
				titleStr.find("pc user") != -1 or
				titleStr.find("pc_user") != -1 or
				titleStr.find("personalized computer user") != -1):
		keywords = keywords + ["PC User"]

	if titleStr.find("skeleton") != -1:
		keywords = keywords + ["Skeleton"]

	if titleStr.find("javascript") != -1:
		keywords = keywords + ["Javascript"]

	if titleStr.find("angular") != -1:
		keywords = keywords + ["Angular"]

	if titleStr.find("bootstrap") != -1:
		keywords = keywords + ["Bootstrap"]

	if titleStr.find("jquery") != -1:
		keywords = keywords + ["Jquery"]

	if titleStr.find("linux") != -1:
		keywords = keywords + ["Linux"]

	if titleStr.find("unix") != -1:
		keywords = keywords + ["Unix"]

	if titleStr.find("ubuntu") != -1:
		keywords = keywords + ["Ubuntu"]

	if titleStr.find("mac") != -1:
		keywords = keywords + ["Mac"]

	if titleStr.find("windows") != -1:
		keywords = keywords + ["Windows"]
	return keywords


def get_pdf(url):

	# try to get keywords from this function
	# if pdf was not found in the html, it will give us []
	try:
		if type(url) != str and type(url) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure the url is a string" + bcolors.ENDC)
	try:
		if not "http://" in url == False:
			url = "http://" + url
		usock = urllib2.urlopen(url)
		html = usock.read()
		print html
		# obtain pdf_url from find_pdf function
		pdf_url = find_pdf(html, url)
		pdfSkills = []

		# if pdf was not found, (== False)
		if pdf_url == False:
			print bcolors.OKBLUE + "pdf was not found in this site" + bcolors.ENDC
			pdf_url = []

		else:
			# get_pdf_content function will give us keywords we need.
			pdfSkills = get_pdf_content(pdf_url)
		return pdfSkills

	except:
		print bcolors.FAIL + "Error in Main func, get_pdf(). Check all the functions inside." + bcolors.ENDC
		return []


# Grab the html from the user
# inputted HTML
# THIS IS THE MAIN FUNCTION!!!
def get_html(url):
	try:
		if type(url) != str and type(url) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure input is a string" + bcolors.ENDC)
	try:
		url = url.lower()
		# keywords_title = 0
		# print url

		# If the url does not have
		# "http://" then add the
		# "http://" to the url
		if url.find("http://") == -1:
			url = "http://" + url
		# print url
		# url = requests.get(url)
		# print url

		# This part here acts as how
		# one would read in a regular
		# text file

		# Grab the url, using the
		# urllib2 package
		usock = urllib2.urlopen(url)

		# Read in the html, via read()
		html = usock.read()
		lowerCase_html = html.lower()
		#print html
		# Head tag - Grab the content in between
		# the header tags
		titleTag = lowerCase_html.find("<head>")
		end_titleTag = lowerCase_html.find("</head>")
		keywords_title = title_find(lowerCase_html[titleTag + 6:end_titleTag])

		#print keywords_title

		# Meta Tags
		keywords_meta = search_meta_keywords(lowerCase_html)

		#print keywords_meta

		# Body Education - Grab the content in
		# between the header tags
		bodyTag = lowerCase_html.find("<body>")
		end_bodyTag = lowerCase_html.find("</body>")
		#print lowerCase_html[bodyTag + 6:end_bodyTag]
		# print ("computer science" in lowerCase_html[bodyTag + 6:end_bodyTag])
		keywords_degree = find_degree(lowerCase_html[bodyTag + 6:end_bodyTag])

		#print keywords_degree

		# Skills
		keywords_skills = find_skills(lowerCase_html[bodyTag + 6:end_bodyTag])

		#print keywords_skills

		usock.close()

		# print html
		#print "Title  ", keywords_title
		#print "Meta   ", keywords_meta
		#print "Degree ", keywords_degree
		#print "Skills ", keywords_skills
		# print "Pdf    ", pdf_url
		# print "Pdf con", pdfSkills

		# Combine all of the keywords
		keywords = keywords_title + keywords_meta + keywords_degree + keywords_skills
		# except:
		# return "error"
		#print keywords
		return keywords

	# Return an empty array, if there
	# is an error
	except:
		print bcolors.FAIL + "Error in Main func, get_html(). Check all the functions inside." + bcolors.ENDC
		return []

		# Testing Purposes
		# /#####################################/#

def get_all_html(url):
	try:
		if type(url) != str and type(url) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure input is a string" + bcolors.ENDC)
	try:
		url = url.lower()
		# keywords_title = 0
		# print url

		# If the url does not have
		# "http://" then add the
		# "http://" to the url
		if url.find("http://") == -1:
			url = "http://" + url
		# print url
		# url = requests.get(url)
		# print url

		# This part here acts as how
		# one would read in a regular
		# text file

		# Grab the url, using the
		# urllib2 package
		usock = urllib2.urlopen(url)

		# Read in the html, via read()
		html = usock.read()
		lowerCase_html = html.lower()
		lowerCase_html = strip_tags(lowerCase_html)
		#print lowerCase_html
		#print html
		# Head tag - Grab the content in between
		# the header tags
		
		lowerCase_html = lowerCase_html.replace("\"", "")
		lowerCase_html = lowerCase_html.replace("'", "")
		
		lowerCase_html = lowerCase_html.replace(".", " ")
		lowerCase_html = lowerCase_html.replace(",", " ")
		lowerCase_html = lowerCase_html.replace("/>", " ")
		lowerCase_html = lowerCase_html.replace("<", " ")
		lowerCase_html = lowerCase_html.replace(">", " ")
		lowerCase_html = lowerCase_html.replace("#", " ")
		lowerCase_html = lowerCase_html.replace(":", " ")
		lowerCase_html = lowerCase_html.replace(";", " ")
		lowerCase_html = lowerCase_html.replace("/", " ")
		lowerCase_html = lowerCase_html.replace("-", " ")
		lowerCase_html = lowerCase_html.replace("(", " ")
		lowerCase_html = lowerCase_html.replace(")", " ")
		lowerCase_html = lowerCase_html.replace("&", " ")
		lowerCase_html = lowerCase_html.replace("\\", " ")
		lowerCase_html = lowerCase_html.replace("=", " ")
		lowerCase_html = lowerCase_html.replace("@", " ")
		lowerCase_html = lowerCase_html.replace("_", " ")
		lowerCase_html = lowerCase_html.replace("?", " ")
		lowerCase_html = lowerCase_html.replace("|", " ")
		lowerCase_html = lowerCase_html.replace("!", " ")
		lowerCase_html = lowerCase_html.replace("+", " ")		
		lowerCase_html = lowerCase_html.replace("[", " ")
		lowerCase_html = lowerCase_html.replace("]", " ")
		lowerCase_html = lowerCase_html.replace("{", " ")
		lowerCase_html = lowerCase_html.replace("}", " ")
		lowerCase_html = lowerCase_html.replace("*", " ")
		lowerCase_html = lowerCase_html.replace("/", " ")
		lowerCase_html = lowerCase_html.replace("@", " ")
		lowerCase_html = lowerCase_html.replace("%", " ")
		lowerCase_html = lowerCase_html.replace("$", " ")
		
		lowerCase_html = lowerCase_html.strip(' \u')
		lowerCase_html = re.sub('\s+', ' ', lowerCase_html)
		lowerCase_html = lowerCase_html.split(' ')
		word_list = []
		for i in lowerCase_html:
			if i not in word_list and " " not in i and "" != i and is_number(i) == False:
				word_list.append(i)
		return word_list


		#titleTag = lowerCase_html.find("<title>")
		#end_titleTag = lowerCase_html.find("</title>")
		#print lowerCase_html[titleTag + 7:end_titleTag]
		#print keywords_title
		# Meta Tags
		
	except:
		print bcolors.FAIL + "Error in Main func, get_all_html(). Check all the functions inside." + bcolors.ENDC
		return []

		# Testing Purposes
		# /#####################################/#

def get_all_pdf(url):
	try:
		if type(url) != str and type(url) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure the url is a string" + bcolors.ENDC)
	try:
		if not "http://" in url == False:
			url = "http://" + url

		url = url.lower()
		# keywords_title = 0
		# print url

		# If the url does not have
		# "http://" then add the
		# "http://" to the url
		if url.find("http://") == -1:
			url = "http://" + url

		usock = urllib2.urlopen(url)
		html = usock.read()
		# obtain pdf_url from find_pdf function
		pdf_url = find_pdf(html, url)
		print pdf_url
		pdfSkills = []

		# if pdf was not found, (== False)
		if pdf_url == False:
			print bcolors.OKBLUE + "pdf was not found in this site" + bcolors.ENDC
			pdf_url = []

		else:
			# get_pdf_content function will give us keywords we need.
			
			pdfSkills = get_pdf_content(pdf_url)
		return pdfSkills

	except Exception, e:
		print bcolors.FAIL + "Error in Main func, get_all_pdf(). Check all the functions inside." + bcolors.ENDC
		print e
		return []

#get_html("http://yljiang.github.io/")
#get_html("http://richardsin.com")
#get_pdf_content("resume.pdf")
