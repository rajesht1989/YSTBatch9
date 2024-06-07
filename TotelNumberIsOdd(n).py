#Write a Python program that calculates the sum of all the numbers in a given list.
def TotelNumberIsOdd(n):
    m=0
    for i in range(0,n+1):
        m+=i
    print(m)
n=int(input())
TotelNumberIsOdd(n)
