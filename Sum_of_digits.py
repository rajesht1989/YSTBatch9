#write a program to get the number from user and add the digits

def sum_of_digits(number):
    digit_sum = 0
    number_str = str(number)
    for digit in number_str:
        digit_sum += int(digit)
    return digit_sum
number = int(input("Enter a positive integer: "))
print("Sum of digits:", sum_of_digits(number))
