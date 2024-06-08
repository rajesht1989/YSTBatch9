def add1toN(n):
    value=0
    for i in range(1,n+1):
        i+=i
    print("Addition value is : ",i)
n= int(input("enter the last number: "))
add1toN(n)
