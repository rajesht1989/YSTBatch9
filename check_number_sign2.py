def check_number_sign(number):
    if number >0:
        return("pasitive")
    else:
        return("negative")
number_value_input=int(input("enter the number : "))
value = check_number_sign(number=number_value_input)
print("The resul  "+str(number_value_input)+" is",value)
