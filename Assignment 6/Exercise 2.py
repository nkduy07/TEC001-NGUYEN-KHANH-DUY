seasons = ("Winter", "Spring", "Summer", "Autumn")
month = int(input("Enter a month (1-12): "))
if month == 12 or month == 1 or month == 2:
    print(f"It is {seasons[1]}")
elif 3<=month<=5:
    print(f"It is {seasons[2]}")
elif 6<=month<=9:
    print(f"It is {seasons[3]}")
else:
    print(f"It is {seasons[4]}")