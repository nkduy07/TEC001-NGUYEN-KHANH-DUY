names = set()
while True:
    user_input = input("Please enter your name (press Enter to stop): ")
    if user_input in names:
        print("Existing name")
    else:
        print("New name")
        names.add(user_input)
    if user_input =="":
        break
for name in names:
    print(name)
