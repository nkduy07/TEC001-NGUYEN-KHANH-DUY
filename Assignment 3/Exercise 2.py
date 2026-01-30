inch = float(input("Enter the inch: "))
while True:
    if inch >= 0:
        print("Inch to cm:", inch * 2.54)
        inch = float(input("Enter the inch: "))
    else:
        print("Invalid")
        break

