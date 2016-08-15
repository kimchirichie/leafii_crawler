from crawler.administer import delete_all_keywords, parse_all_users

try:
	if not delete_all_keywords():
		raise Exception('ERROR: Delete Keywords operation failed!')
	if not parse_all_users():
		raise Exception('ERROR: Parse All Users operation failed!')

except Exception, e:
	sys.stderr.write(str(e))