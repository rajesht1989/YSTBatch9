def calculate_compound_interest(p,r,t):
    formula = p*(1+r/100)**t-p
    return formula 
    
user_value1 = int(input("Enter your value for p is : "))
user_value2 = int(input("Enter your value for r is : "))
user_value3 = int(input("Enter your value for t is : "))

print("It is your compound interest is : ",calculate_compound_interest(r=user_value2,p=user_value1,t=user_value3))
