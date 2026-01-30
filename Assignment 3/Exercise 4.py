import random
a = random.randint(1,10)
try:
    while True:
        b = int(input("Enter a number between 1 and 10: "))
        if b > a:
            print("Too high")
        elif b < a:
            print("Too low")
        else:
            print("Correct")
            break
except:
    print("Invalid input")

