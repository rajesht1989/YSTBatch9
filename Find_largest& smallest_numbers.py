#Write a program to find the largest and smallest numbers in a list using a for loop.

def findLargestAndSmallestNumbers():
    numbers=[489,32,78,75,751,78,983,37,320,574,58,174]
    for i in numbers:
        numbers.sort()
    print("numbers =",numbers)
    print("Smallest number is : ",min(numbers))
    print("Largest number is : ",max(numbers))
findLargestAndSmallestNumbers()
