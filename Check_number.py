def check_number(number):
    
    if number==(2**3)-2:
        return ("The number is 6")
        
    elif number<6 :
        return ("The number is less than 6")
        
    else :
        return ("The number is greater than 6")
        
Number=int(input ("enter the number : "))
print (check_number(number=Number))
