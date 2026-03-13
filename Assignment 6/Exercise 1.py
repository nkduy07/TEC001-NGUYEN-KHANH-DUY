numbers = []
while True:
    user_input = input("Enter a number (press ENTER to quit): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input")
numbers.sort(reverse=True)
top_five = numbers[:5]
print(top_five)