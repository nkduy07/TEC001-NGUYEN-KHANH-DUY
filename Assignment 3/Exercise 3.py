largest = None
smallest = None
while True:
    a = input("Enter a number: ")
    if a == "":
        break
    number = float(a)
    if largest == None or number > largest:
        largest = number
    if smallest == None or number < smallest:
        smallest = number
if largest != None and smallest != None:
    print("The largest number is ", largest)
    print("The smallest number is ", smallest)