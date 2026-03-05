import re

def hide_phone_number(para):
    numbers = r'\+84\d+|\d{10}'
    result = re.sub(numbers,"[REDACTED]", para)
    return result

a = input("Enter a paraghraph: ")
print(f"Output: {hide_phone_number(a)}")