def The_avarage_function(value_1,value_2,value_3):
    avarage_variable=value_1+value_2+value_3/3
    return avarage_variable
    
first_value_input=int(input("Enter the first value : "))
second_value_input=int(input("Enter the second value : "))
third_value_input=int(input("Enter the third value : "))

print ("avarage value is : ",The_avarage_function(value_1=first_value_input,value_2=second_value_input,value_3=third_value_input))
