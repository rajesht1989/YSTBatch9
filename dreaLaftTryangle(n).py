def dreaLaftTryangle(n):
    for row in range(0,n):
        for col in range(0,n):
            if row > col :
                print("\t",end='')
            else :
                print("*\t",end='')
        print("\n")

n =int(input())
dreaLaftTryangle(n)
