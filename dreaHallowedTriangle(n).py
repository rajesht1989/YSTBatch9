def dreaHallowedTriangle(n):
    for i in range (0,n):
        for j in range (0,n):
            if i == 0 or j == 0 or i == 0 and j == 0:
                print("*",end='')
            else:
                print(" ",end='')
        print("\n")
n=int(input("Enter a number : "))
dreaHallowedTriangle(n)
