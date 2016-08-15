from connector import database
from cStringIO import StringIO
from HTMLParser import HTMLParser
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import re
import requests
import urllib
import urllib2
import os

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

class bcolors:
	HEAD = '\033[95m'
	OKGREEN = '\033[92m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	OKBLUE = '\033[94m'

# Helps remove XML tags from HTML document
def _strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# Checks if param is number
def _is_number(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

### not sure what this is
def _number_composition(word):
	length = len(word)
	word = list(word)
	number = 0
	for i in word:
		if _is_number(i):
			number += 1
	return number

# Download the .pdf resume and parse it
def _get_pdf_content(url, page_nums=[0]):
	resume = urllib.URLopener()
	# Just in case, try opening the .pdf with
	# the url found
	try:
		if type(url) != str and type(url) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Provided URL is bad type. URL must be a string" + bcolors.ENDC) 
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

		# Use find_skills function, to parse the
		# text as it would with the HTML
		lstSkills = _find_skills(text)
		os.remove("resume.pdf")

		# Return the string of Skills
		return lstSkills
	except:
		# If we run into an error, continue on, and
		# move onto the next try statement
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
		lstSkills = _find_skills(text)
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
		lstSkills = _find_skills(text)
		return lstSkills
	except:
		# Return an empty array, indicating that
		# we were unable to retrieve any
		# information from your resume
		print bcolors.FAIL + "Unable to parse pdf with given URL" + bcolors.ENDC
		return []

# Find the the .pdf link
def _find_pdf(html, url):
	# If we find a .pdf in the html
	# String, then try to find the
	# entire link here
	try:
		if (type(html) != str and type(html) != unicode) or (type(url) != str  and type(url) != unicode):
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "Invalid input. Make sure both input fields are string" + bcolors.ENDC)

	if (".pdf" in html):
		# print "PDF file was found"
		loop = True

		# Create a pivot point, from where
		# the "." starts in ".pdf", then
		# work backwards
		pivotPoint = html.find(".pdf")
		counter = 0
		pdfURL = ""
		temp_url = url

		# Remove hard carraige, and hard character
		# returns in the
		temp_url = temp_url.replace("\r", "")
		temp_url = temp_url.replace("\n", "")

		# Make a loop that will find the link from
		# the ".pdf" point to the href link
		while loop:
			if (("f" == html[pivotPoint - counter]) and
					("e" == html[pivotPoint - counter - 1]) and
					("r" == html[pivotPoint - counter - 2]) and
					("h" == html[pivotPoint - counter - 3])):

				# Set a variable that will contain the pdfURL
				pdfURL = html[pivotPoint - counter + 3:pivotPoint + 4]

				# return the pdfURL we have found
				if not pdfURL.find(temp_url) == -1:
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
					url = url.replace("\r", "")
					url = url.replace("\n", "")
					pdfURL = url + "/" + pdfURL
					return pdfURL
			else:
				counter += 1
	else:
		return False

### not used
def _find_degree(bodyStr):
	
	try:
		if type(bodyStr) != str and type(bodyStr) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "bodyStr must be a string" + bcolors.ENDC)

	db = database()
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

# Finds skills in the body
def _find_skills(bodyStr):
	try:
		if type(bodyStr) != str and type(bodyStr) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "bodyStr must be a string" + bcolors.ENDC)

	db = database()
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

### not used
def _search_meta_keywords(keywordStr):
	try:
		if type(keywordStr) != str and type(keywordStr) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "keywordStr must be a string" + bcolors.ENDC)
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

# Grabs html of url & returns list of keywords
def get_html(url):
	#print url
	try:
		if type(url) != str and type(url) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "url must be a string" + bcolors.ENDC)
	try:
		# If the url does not have
		# "http://" then add the
		# "http://" to the url
		if not "http://" in url:
			url = "http://" + url

		url = url.lower()

		# Grab the url, using the
		# urllib2 package
		usock = urllib2.urlopen(url)
		# Read in the html, via read()
		html = usock.read()
		lowerCase_html = html.lower()

		lowerCase_html = re.sub('<script[^<]*</script>','',lowerCase_html)
		lowerCase_html = re.sub('<script[^>]*>','',lowerCase_html)

		lowerCase_html = re.sub('<style[^<]*</style>','',lowerCase_html)
		lowerCase_html = re.sub('<style[^>]*>','',lowerCase_html)

		lowerCase_html = _strip_tags(lowerCase_html)

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
			if i not in word_list and " " not in i and "" != i and _is_number(i) == False and len(i) <= 20 and len(i) > 2 and _number_composition(i) == 0:
				word_list.append(i)
		
		return word_list


	except Exception as e:
		print bcolors.FAIL + "Error parsing HTML" + bcolors.ENDC
		print e
		return []

# Grabs pdf in url's html & returns list of keywords
### not grabbing everything
def get_pdf(url):
	try:
		if type(url) != str and type(url) != unicode:
			raise TypeError
	except TypeError:
		raise TypeError(bcolors.FAIL + "url must be a string" + bcolors.ENDC)
	try:
		# If the url does not have
		# "http://" then add the
		# "http://" to the url
		if not "http://" in url:
			url = "http://" + url

		url = url.lower()

		usock = urllib2.urlopen(url)
		html = usock.read()
		# obtain pdf_url from find_pdf function
		pdf_url = _find_pdf(html, url)
		print pdf_url
		pdfSkills = []

		# if pdf was not found, (== False)
		if not pdf_url:
			print bcolors.OKBLUE + "pdf was not found in this site" + bcolors.ENDC
			pdf_url = []
		else:
			# get_pdf_content function will give us keywords we need.
			pdfSkills = _get_pdf_content(pdf_url)

		return pdfSkills

	except Exception, e:
		print bcolors.FAIL + "Error parsing PDF" + bcolors.ENDC
		print e
		return []