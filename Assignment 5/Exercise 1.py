import re

def check_code(code):
    pattern = r'^[A-Z]{2,3}\d{3}$'

    if re.match(pattern, code):
        return True
    return False

a = input("Enter course code: ")
print (f"{a} is a valid course code? {check_code(a)}")



