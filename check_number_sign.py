def check_number_sign(number):
    if number>0:
        return("positive number")
    else:
        return("negative number")
        
user_value=int(input("Enter your value  : "))


print ("check number ", check_number_sign(number=user_value))
