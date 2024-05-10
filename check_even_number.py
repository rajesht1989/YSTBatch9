def check_even_number(number):
    if number%2==0:
        return(" odd number ")
    else:
        return(" even number ")
        
user_value=int(input("Enter your numbers is : "))
        
calculate_number=check_even_number(number=user_value)
number=str(user_value)
print(number+" is a ",calculate_number)
