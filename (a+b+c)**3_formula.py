def mathematics_formula(a,b,c):
    formula = (a+b+c)**3
    return formula 
    
user_value1=int(input("Enter your value for a : "))
user_value2=int(input("Enter your value for b : "))
user_value3=int(input("Enter your value for c : "))
result1=mathematics_formula(a=user_value1, b=user_value2, c=user_value3)

def mathematics_detail_formula(a,b,c):
    formula_in_detail = a**3+b**3+c**3+3*(a+b)*(b+c)*(c+a)
    return formula_in_detail
    
result2=mathematics_detail_formula(a=user_value1, b=user_value2, c=user_value3)
print("The simple formula result : ", result1)
print("The detail formula results :  ", result2)