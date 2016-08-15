from crawler.administer import parse_user_site, delete_user_keywords
import sys

try:
	
	user_id = sys.argv[1]
	delete = delete_user_keywords(user_id)
	parse = parse_user_site(user_id)
	if delete == False and parse == False:
		raise Exception('Delete and Parse operations failed!')
	if delete == False:
		raise Exception('Delete operation failed!')
	if parse == False:
		raise Exception('Parse operation failed!')
except ValueError:
	print ("Invalid user_id found")
except TypeError:
	print ("user_id not string")
except Exception, e:
	sys.stderr.write(str(e))