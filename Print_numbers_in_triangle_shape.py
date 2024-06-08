def print_numbers(n):
    i=1
    for i in range(1,n+2):
        for j in range(1,i):
            print(j,end='\t')
        print(end='\n')
        i+=1
n=int(input("enter the number of lines: "))
print_numbers(n)
