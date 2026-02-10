def cal_sum(integers):
    total = sum(integers)
    return total

#For testing:
def cal_sum():
    list = [1,2,3,4,5]
    total = sum(list)
    return total
print(cal_sum())

#For users to input
def cal_sum(integers):
    total = sum(integers)
    return total
integers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    integers.append(int(user_input))

print(cal_sum(integers))
