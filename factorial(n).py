#Write a Python function that takes a positive integer n as an argument and returns the factorial of n using a for loop.
def factorial(n):
    f=1
    for i in range(2,n+1):
        f=f*i
        print(f)
n = int(input())
factorial(n)
