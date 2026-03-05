import re

def check_color(color):
    pattern = r'^#[0-9a-fA-F]{6}$'

    if re.match(pattern, color):
        return True
    return False

a = input("Enter color code: ")
print (f"{a} is a valid color code? {check_color(a)}")