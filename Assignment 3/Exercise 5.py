user_name = "python"
password = "rules"
attempts = 5
a = input("Enter username: ")
b = input("Enter password: ")
while True:
    if a == user_name and b == password:
        print("Welcome")
        break
    else:
        print ("Incorrect username or password")
        attempts -= 1
        a = input("Enter username: ")
        b = input("Enter password: ")
    if attempts == 0:
        print("Incorrect username or password")
        print("Access Denied")
        break
