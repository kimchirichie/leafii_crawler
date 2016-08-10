from user_func import parse_user_site, delete_user_keywords
import sys

try:
	
	userID = sys.argv[1]
	delete = delete_user_keywords(userID)
	parse = parse_user_site(userID)
	if delete == False and parse == False:
		raise Exception('ERROR: Delete and Parse operations failed!')
	if delete == False:
		raise Exception('ERROR: Delete operation failed!')
	if parse == False:
		raise Exception('ERROR: Parse operation failed!')
except ValueError:
	print ("Invalid UserID found")
except TypeError:
	print ("UserID not string")
except Exception, e:
	sys.stderr.write(str(e))