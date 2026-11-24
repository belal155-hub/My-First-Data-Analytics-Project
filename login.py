password = input("Enter your password: ")
attempts = 0

while password != "pycharm987" and attempts <3:
    attempts = attempts + 1
    print("Invalid Credentials. Try Again.")

    if attempts <3:
        password = input("Enter your password: ")

if password == "pycharm987":
    print("Login Successful")
else:
    print("Account Locked")