def recommend_home_insurance_plan(age, residence_type):
    
    if(18<=age<30)and(residence_type=="own_house"):
        return ("recommend the Standard plan")
        
    elif(age>=30)and(residence_type=="own_house"):
        return ("recommend the comprehensive plan")
        
    elif(age>=18)and(residence_type=="own_apartment"):
        return ("recommend the Appartment plan ")
    
    else:
        return ("they are not eligible to home insurance")
        
age=int(input ("enter your age in number: "))
residence_type=input ("enter your living place (own_house, own_apartment) : ")

print (recommend_home_insurance_plan(age, residence_type))
