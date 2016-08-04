from user_func import re_parse_all

try:
	
	reparse = re_parse_all()
	if reparse == False:
		raise Exception('ERROR: Reparse operation failed!')

except Exception, e:
	sys.stderr.write(str(e))