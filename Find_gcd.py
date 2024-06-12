#write a program to get the values from the user and calculate gcd on the values

def findgcd(a, b):
    minimum = min(a, b)
    findgcd = 1
    for i in range(1,minimum+1):
        if(a%i==0)and(b%i==0):
            findgcd = i
    return findgcd
a=int(input("enter a first number : "))
b=int(input("enter a second number : "))
print(findgcd(a,b))
