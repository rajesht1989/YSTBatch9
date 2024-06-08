def recommend_travel_insurance(age, pre_existing_conditions):
    
    if (0<age<30)and(pre_existing_conditions=="no"):
        return ("recommend to use Standard plan")
        
    elif(age>=30)and(pre_existing_conditions=="no"):
        return ("recommend to use Comprehensive plan")
    
    elif(pre_existing_conditions=="yes"):
        return ("recommend to use Enhanced plan")
        
    else:
        return ("you are enter correct details")
        
age=int(input ("enter your age in number: "))
pre_existing_conditions=input ("you are pre_existing_conditions, say yes or no: ")

print (recommend_travel_insurance(age, pre_existing_conditions))
