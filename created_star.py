def create_star(number):
    for i in range(number):
        for j in range(i, number):
            print(' ', end=' ')
        for j in range(i+1): 
            print('*', end=' ')
        print()
input_number=int(input("Enter your number : "))
create_star(number=input_number)