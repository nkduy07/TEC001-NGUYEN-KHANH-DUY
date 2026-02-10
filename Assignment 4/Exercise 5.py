def remove_uneven(integers):
    for x in integers:
        if x % 2 == 0:
            integers.remove(x)
    return integers
# For testing
def remove_uneven(integers):
    for x in integers:
        if x % 2 == 0:
            integers.remove(x)
    return integers
integers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    integers.append(int(user_input))
print(f"The original list: {integers}")
print(f"The edited list: {remove_uneven(integers)}")