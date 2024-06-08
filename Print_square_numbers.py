def printSquareOfTheNumber(number):
    for i in range(number,number+1):
        i*=i
        print(number,"square is :",i)
number=int(input("enter a number: "))
printSquareOfTheNumber(number)
