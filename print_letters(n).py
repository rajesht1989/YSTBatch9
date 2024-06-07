def print_letters(n):

    for i in range(1,n+1):
        ch=65
        for j in range(ch,ch+i):
            a=chr(j)
            print(a,end='\t')
        print()
n=int(input("enter the number of lines : "))
print_letters(n)
