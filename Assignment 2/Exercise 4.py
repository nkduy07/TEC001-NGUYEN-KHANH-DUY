def check_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    elif year % 4 == 0:
        print("Leap year")
    else:
        print("Not leap year")
year = int(input("Enter a year: "))
check_leap_year(year)
