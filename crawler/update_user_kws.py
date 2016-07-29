from user_func import parse_user_site, delete_user_keywords
import sys

try:
	
	userID = sys.argv[1]
	delete_user_keywords(userID)
	parse_user_site(userID)

except Exception, e:
	print e