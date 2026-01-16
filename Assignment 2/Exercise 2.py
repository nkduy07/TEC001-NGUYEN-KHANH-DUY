try:
    def cabin_class():
        cabin = input("Enter cabin class: ").upper()
        if cabin == "LUX":
            description = print("upper-deck cabin with a balcony.")
        elif cabin == "A":
            description = print("above the car deck, equipped with a window.")
        elif cabin == "B":
            description = print("windowless cabin above the car deck.")
        elif cabin == "C":
            description = print("windowless cabin below the car deck.")
        else:
            description = print("Invalid cabin class")
    cabin_class()
except ValueError:
    print("Invalid cabin class")