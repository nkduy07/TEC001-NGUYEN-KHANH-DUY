numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    num = float(user_input)
    numbers.append(num)
    numbers.sort(reverse=True)
    top_5 = numbers[:5]
if top_5:
    print("The five greatest numbers are: ")
    for x in top_5:
        print(x, end=" ")
