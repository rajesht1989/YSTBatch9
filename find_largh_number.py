def find_largh_number(num1,num2):
    if num1>num2:
        return("biggest number")
    else:
        return("smallest number")
        
user_value1=int(input("Enter your value number 1 : "))
user_value2=int(input("Enter your value number 2 : "))


print ("check numbers is biggest or smallest : ", find_largh_number(num1=user_value1,num2=user_value2))
