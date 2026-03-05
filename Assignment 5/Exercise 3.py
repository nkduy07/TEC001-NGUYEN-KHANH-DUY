import re

def sum_number(para):
    numbers = re.findall(r'\d+', para)
    total_sum = sum(int(num) for num in numbers)
    return total_sum

a = input("Enter a paraghraph: ")
print(f"The sum of the numbers in the paragraph: {sum_number(a)}")