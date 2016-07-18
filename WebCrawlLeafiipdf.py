import urllib2
import urllib
from cStringIO import StringIO
import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import datetime
import pymongo


def parse_start():
    keywords = ""
    url_file = open("URLs.txt", "r")
    loop = True
    # type(url_file.readline())
    while loop:
        website = url_file.readline()
        try:
            if website != "":
                keywords = get_html(website)
                # print keywords
                print "website", website
            else:
                loop = False
        except:
            print "ERROR ", website, "\n"


def get_pdf_content(url, page_nums=[0]):
    resume = urllib.URLopener()
    try:
        r  = requests.get(url)
        resume.retrieve(r.url, "resume.pdf")
        content =""

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

        #p = file("resume.pdf", "rb")
        #pdf = PyPDF2.PdfFileReader(p)
        #for page_num in page_nums:
        #   content += pdf.getPage(page_num).extractText()
        lstSkills = find_skills(text)
        return lstSkills

    except:
        pass

    try:
        url = url[:7] + "www." + url[7:] #######################Try request
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

    except:
        return []


def find_pdf(str, urlStr):
    if (".pdf" in str):
        # print "PDF file was found"
        # a = Str[Str.find(".pdf")]
        # print a
        loop = True
        pivotPoint = str.find(".pdf")
        counter = 0
        pdfURL = ""
        temp_urlStr = urlStr
        temp_urlStr = temp_urlStr.replace("\r", "")
        temp_urlStr = temp_urlStr.replace("\n", "")
        while loop:
            if (("f" == str[pivotPoint - counter]) and
                    ("e" == str[pivotPoint - counter - 1]) and
                    ("r" == str[pivotPoint - counter - 2]) and
                    ("h" == str[pivotPoint - counter - 3])):
                pdfURL = str[pivotPoint - counter + 3:pivotPoint + 4]

                if not pdfURL.find(temp_urlStr) == -1:
                    return pdfURL

                if not pdfURL.find("http") == -1:
                    return pdfURL

                if not pdfURL.find(".com") == -1:
                    return pdfURL

                if not pdfURL.find(".org") == -1:
                    return pdfURL

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
    keywords_body = []
    lst = []
    # Degrees
    degreeFile = open("degree_lists.txt", "r")
    for i in degreeFile:
        # print (i.lower())
        a = i
        a = a.replace('\r', "")
        a = a.replace('\n', "")
        # print ("computer science" in bodyStr)
        lst = lst + [a]
        # print lst
        # print (a.lower() in bodyStr)
        if (a.lower() in bodyStr):
            keywords_body = keywords_body + [a]
        else:
            ()
    degreeFile.close()
    return keywords_body


def find_skills(bodyStr):
    skill_words = []
    lstSkills = open("skills_list.txt", "r")
    counter = True

    if ("skill" in bodyStr):
        skill_tag = bodyStr[bodyStr.find("skill"):]
        for i in lstSkills:
            temp_i = i
            temp_i = temp_i.replace('\n', "")
            temp_i = temp_i.replace('\r', "")
            if (temp_i.lower() in skill_tag):
                skill_words = skill_words + [temp_i]

            if (" c " in skill_tag and counter == True):
                skill_words = skill_words + ["C"]
                counter = False

            if (" r " in skill_tag and counter == True):
                skill_words = skill_words + ["R"]
                counter = False

            else:
                ()
    else:
        for i in lstSkills:
            temp_i = i
            temp_i = temp_i.replace('\n', "")
            temp_i = temp_i.replace('\r', "")
            if (temp_i.lower() in bodyStr):
                skill_words = skill_words + [temp_i]

            if (" c " in bodyStr and counter == True):
                skill_words = skill_words + ["C"]
                counter = False

            if (" r " in bodyStr and counter == True):
                skill_words = skill_words + ["R"]
                counter = False

            else:
                ()
    return skill_words


def search_meta_keywords(keywordStr):
    keyword_contents = []
    # print (keywordStr.find('meta name="keywords" '))
    if (keywordStr.find("meta name=\"keywords\" ") != -1):
        starting_k_contents = keywordStr.find("meta name=\"keywords\" ") + 30
        ending_k_contents = keywordStr.find(">", starting_k_contents)
        temp_keywords = keywordStr[starting_k_contents:ending_k_contents - 2]
        temp_keywords = temp_keywords.replace("\"","")
        temp_keywords = temp_keywords.split(",")
        keyword_contents = keyword_contents + temp_keywords
        return keyword_contents
    else:
        return keyword_contents


def title_find(titleStr):
    keywords = []
    if (titleStr.find("pc.user") != -1 or
                titleStr.find("pc user") != -1 or
                titleStr.find("pc_user") != -1 or
                titleStr.find("personalized computer user") != -1):
        keywords = keywords + ["PC User"]
    if (titleStr.find("skeleton") != -1):
        keywords = keywords + ["Skeleton"]
    if (titleStr.find("javascript") != -1):
        keywords = keywords + ["Javascript"]
    if (titleStr.find("angular") != -1):
        keywords = keywords + ["Angular"]
    if (titleStr.find("bootstrap") != -1):
        keywords = keywords + ["Bootstrap"]
    if (titleStr.find("jquery") != -1):
        keywords = keywords + ["Jquery"]
    if (titleStr.find("linux") != -1):
        keywords = keywords + ["Linux"]
    if (titleStr.find("unix") != -1):
        keywords = keywords + ["Unix"]
    if (titleStr.find("ubuntu") != -1):
        keywords = keywords + ["Ubuntu"]
    if (titleStr.find("mac") != -1):
        keywords = keywords + ["Mac"]
    if (titleStr.find("windows") != -1):
        keywords = keywords + ["Windows"]

    return keywords


def pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    pdf = file(path, 'rb')
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

    pdf.close()
    device.close()
    retstr.close()
    print ("ruby" in text)
    #print text
    return text

def get_pdf(url):
    try:
        if not "http://" in url == False:
            url = "http://" + url
            #print url
        #url = requests.get(url)
        #print url
        usock = urllib2.urlopen(url)
        html = usock.read()

        # PDFS
        pdf_url = find_pdf(html, url)
        pdfSkills = []
        if (pdf_url == False):
            pdf_url = []
        else:
            pdfSkills = get_pdf_content(pdf_url)

        return pdfSkills
    except:
        return []


def get_html(url):
    try:
        # keywords_title = 0
        #print url
        if url.find("http://") == -1:
            url = "http://" + url
            #print url
        #url = requests.get(url)
        #print url
        usock = urllib2.urlopen(url)
        html = usock.read()
        lowerCase_html = html.lower()

        # Head tag
        titleTag = lowerCase_html.find("<head>")
        end_titleTag = lowerCase_html.find("</head>")
        keywords_title = title_find(lowerCase_html[titleTag + 6:end_titleTag])
        #print keywords_title

        # Meta Tags
        keywords_meta = search_meta_keywords(lowerCase_html)

        # Body Education
        bodyTag = lowerCase_html.find("<body>")
        end_bodyTag = lowerCase_html.find("</body>")
        # print lowerCase_html[bodyTag + 6:end_bodyTag]
        # print ("computer science" in lowerCase_html[bodyTag + 6:end_bodyTag])
        keywords_degree = find_degree(lowerCase_html[bodyTag + 6:end_bodyTag])

        # Skills
        keywords_skills = find_skills(lowerCase_html[bodyTag + 6:end_bodyTag])

        usock.close()

        # print html
        #print "Title  ", keywords_title
        #print "Meta   ", keywords_meta
        #print "Degree ", keywords_degree
        #print "Skills ", keywords_skills
        #print "Pdf    ", pdf_url
        #print "Pdf con", pdfSkills
        #print "Date   ", datetime.datetime.utcnow()

        keywords = keywords_title + keywords_meta + keywords_degree + keywords_skills
        # except:
        # return "error"
        #print keywords
        return keywords
    except:
        return []

#get_html("http://yljiang.github.io")


#parse_start()
#get_pdf_content("resume.pdf")
