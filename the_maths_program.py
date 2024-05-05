def The_maths_function(num_1,num_2,num_3):
    maths_variable_1=num_1+num_2
    maths_variable_2=maths_variable_1*num_3
    return maths_variable_2
 
number_1_input=int(input("enter first number value : "))
number_2_input=int(input("enter second number : "))
number_3_input=int(input("enter third number : "))

print ("The maths function value is : ",The_maths_function(num_1=number_1_input,num_2=number_2_input,num_3=number_3_input))
