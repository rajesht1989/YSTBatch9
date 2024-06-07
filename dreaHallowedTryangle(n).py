def dreaHallowedTryangle(n):
    for row in range (n):
        for col in range (n):
            if row==0 or col==n-row or row==col:
                print("*",end="")
            else:
                print(" ",end="")
        print("\n")        
n =int(input())
dreaHallowedTryangle(n)
