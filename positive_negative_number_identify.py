def numbers_define(number):
    if number>0:
        return("It is positive number")
    elif number==0:
        return ("This number is not accepted")
    else:
        return("It is negative numbner")
input_number=int(input("Enter your number : "))
print(numbers_define(number=input_number))