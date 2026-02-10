cities = []
a = 5
while True:
    user_input = input("Enter city: ")
    a -= 1
    if a == 0:
        break
    cities.append(user_input)
for city in cities:
    print(city)