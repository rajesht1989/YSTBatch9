def printArmstrongNumber(num):
    for num in range(153, num + 1):
        num_digits = len(str(num))
        sum_val = 0
        for digit_char in str(num):
            digit = int(digit_char)
            sum_val += digit ** num_digits
        if num == sum_val:
            print(num)

num = int(input("Enter the last number: "))
printArmstrongNumber(num)
