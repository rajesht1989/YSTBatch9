def calculate_admission_fee(age,is_member):
    if (age>0)and(age<12):
        return ("They have free admission ")
    elif (age>=12)or(is_member=="True"):
        return ("They receive a discount admission fee of $5 ")
    elif (age>=12)and(is_member=="False"):
        return ("They pay the regular admission fee of $10 ")
    else:
        return("invalid age and membership ")
        
user_age=int(input("Enter your age : "))
user_membership=str(input("Enter your membership only True or False "))
result = calculate_admission_fee(age = user_age,is_member = user_membership)
print(f"admission fee is {result}")
