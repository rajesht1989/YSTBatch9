def reverseNumber(number):
    numbers = number
    value = 0
    while numbers > 0:
         value = numbers % 10
         numbers = int(numbers/10)
         print(value,end='')
         
numberValue = int(input("Enter your value : "))
reverseNumber(number=numberValue)
