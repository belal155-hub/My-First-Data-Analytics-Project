def factorial(number):
    if number < 0:
        print("Factorial of negative number does not exist")
        return None


    elif number == 0:
        return 1

    else:
        result = 1

        for i in range(1, number +1):
            result = result * i

        return result

number = int(input("Enter a number: "))

if number < 0:
    factorial(number)

else:
    print(factorial(number))