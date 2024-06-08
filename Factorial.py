def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
number = int(input("Enter a number: "))
print("Factorial of", number, "is", factorial(number))
