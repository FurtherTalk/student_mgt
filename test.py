import re

email_patt = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = '21341234@qq.com'
print( not re.match(email_patt, email))