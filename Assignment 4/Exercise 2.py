number = int(input("Enter a number: "))
if number > 1:
    prime = True
    for x in range(2,number):
        if number % x == 0:
            prime = False
            break
    if prime == True:
        print(f"{number} is the prime number")
    else:
        print(f"{number} is not the prime number")
else:
    print("The number is not prime")
