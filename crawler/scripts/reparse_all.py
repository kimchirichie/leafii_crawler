from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

from administer import delete_all_keywords, parse_all_users
sys.path.pop(0)

try:
	if not delete_all_keywords():
		raise Exception('ERROR: Delete Keywords operation failed!')
	if not parse_all_users():
		raise Exception('ERROR: Parse All Users operation failed!')

except Exception, e:
	sys.stderr.write(str(e))