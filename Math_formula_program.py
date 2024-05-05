def math_formula_function(a,b):
    formula_variable=(a**2)+(b**2)+(2*a*b)
    return formula_variable
    
parameter_1_input=int(input("Enter the a perameter value : "))
perameter_2_input=int(input("Enter the b perameter value : "))

print ("The formula fubction value is : ",math_formula_function(a=parameter_1_input,b=perameter_2_input))
