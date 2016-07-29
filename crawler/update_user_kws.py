from user_func import parse_user_site, delete_user_keywords
import sys

userID = sys.argv[1]
delete_user_keywords(userID)
parse_user_site(userID)