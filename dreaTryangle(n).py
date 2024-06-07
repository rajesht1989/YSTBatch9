def dreaTryangle(n):
    for row in range (0,n):
        for col in range (0,n-row):
            print("*",end="")
        print("\n")        
n =int(input())
dreaTryangle(n)
