import random
print("Your 3-digit code is: ", end = "")
for i in range(3):
    a = random.randint(0,9)
    print(a, end=" ")
print()
print("Your 4-digit code is: ", end = "")
for i in range(4):
    b = random.randint(1,6)
    print(b, end=" ")
