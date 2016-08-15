from crawler.administer import re_parse_all

try:
	
	if not re_parse_all()
		raise Exception('ERROR: Reparse operation failed!')

except Exception, e:
	sys.stderr.write(str(e))