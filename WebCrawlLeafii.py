import urllib2
import PyPDF2

Framework = 0

#WORK ON GRABBIG THE .PDF FILES!!!

def parse_start():
    keywords = ""
    url_file = open("URLs.txt","r")
    loop = True 
    #type(url_file.readline())
    while(loop == True):
        website = url_file.readline()
        try:
            if(website != ""):
                
                keywords = get_html(website)
                #print keywords
                print website
            else:
                loop = False
        except:
            ()

def bodyFind_Degree(bodyStr):
    keywords_body = []
    
    #Degrees
    degreeFile = open("degree_lists.txt", "r")
    for i in degreeFile:
        #print (type(i.lower()))
        a = i
        a = a.replace('\n', '')
        #print (a.lower() in bodyStr)
        if(a.lower() in bodyStr):
            keywords_body = keywords_body + [a]
        else:
            ()
    degreeFile.close()
    return keywords_body

def bodyFind_Skills(bodyStr):
    skill_words = []
    lstSkills = open("skills_list.txt", "r")
    if("skill" in bodyStr):
        skill_tag = bodyStr[bodyStr.find("skill"):]
        for i in lstSkills:
            temp_i = i.replace('\n','')
            if (temp_i.lower() in skill_tag):
                skill_words = skill_words + [temp_i]
            else:
                ()
    else:
        ()
    return skill_words
            
            
def search_meta_keywords(keywordStr):
    keyword_contents = []
    starting_k_contents = 0
    ending_k_contents = 0
    temp_keywords = ""
    #print (keywordStr.find('meta name="keywords" '))
    if (keywordStr.find("meta name=\"keywords\" ") != -1):
        starting_k_contents = keywordStr.find("meta name=\"keywords\" ") + 30
        ending_k_contents = keywordStr.find(">", starting_k_contents)
        temp_keywords = keywordStr[starting_k_contents:ending_k_contents-2]
        keyword_contents = keyword_contents + [temp_keywords.replace("\"","")]
        return keyword_contents
    else:
        return []
        

def title_find(titleStr):
    keywords = []
    versionNum = ""
    if (titleStr.find("pc.user") != -1 or
        titleStr.find("pc user") != -1 or
        titleStr.find("pc_user") != -1 or
        titleStr.find("personalized computer user") != -1):
        keywords = keywords + ["PC User"]
    if (titleStr.find("skeleton") != -1):
        #versionNum = titleStr[titleStr.find("skeleton") + 9:titleStr.find("skeleton") + 14]
        #print (titleStr[titleStr.find("skeleton") + 9:titleStr.find("skeleton") + 14])
        keywords = keywords + ["Skeleton"]
    if (titleStr.find("javascript") != -1):
        keywords = keywords + ["Javascript"]
    if (titleStr.find("angular") != -1):
        keywords = keywords + ["Frameworks Used: Angular"]
    if (titleStr.find("bootstrap") != -1):
        keywords = keywords + ["Bootstrap"]
    if (titleStr.find("jquery") != -1):
        keywords = keywords + ["Jquery"]
    
    return keywords

def get_html(url):
    keywords_title = 0
    usock = urllib2.urlopen(url)
    html = usock.read()
    lowerCase_html = html.lower()
    
    #Head tag
    titleTag = lowerCase_html.find("<head>")
    end_titleTag = lowerCase_html.find("</head>")
    keywords_title = title_find(lowerCase_html[titleTag + 6:end_titleTag])
    
    #Meta Tags
    keywords_meta = search_meta_keywords(lowerCase_html)
    
    #Body Education
    bodyTag = lowerCase_html.find("<body>")
    end_bodyTag = lowerCase_html.find("</body>")
    #print lowerCase_html[bodyTag + 6:end_bodyTag]
    #print ("computer science" in lowerCase_html[bodyTag + 6:end_bodyTag])
    keywords_degree = bodyFind_Degree(lowerCase_html[bodyTag + 6:end_bodyTag])
    
    #Skills
    keywords_skills = bodyFind_Skills(lowerCase_html[bodyTag + 6:end_bodyTag])
        
    usock.close()

    #print html
    #print keywords_title
    #print keywords_meta
    #print keywords_degree
    print keywords_skills
    #except:
        #return "error"