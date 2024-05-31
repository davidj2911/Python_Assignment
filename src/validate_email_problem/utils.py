import re

def email_check(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\b[a-z]{3}\b$'
    if re.match(pattern, email):
        return True
    else:
        return False