#Write a Python program that uses a for loop to find the sum of all even numbers between 1 and 100 (inclusive).
def evenNumbers(n):
    for i in range(1,n+1):
        if(i%2==0):
            print(i)
evenNumbers(100)
