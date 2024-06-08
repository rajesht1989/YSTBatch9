def check_pet_adoption_eligibility(age, living_situation):
    
    if(age>=18)and(living_situvation=="house"):
        return ("they are eligible to adopt a pet")
    
    elif(age>=21)and(living_situvation=="apartment"):
        return ("they are eligible to adopt a pet")
    
    else:
        return ("they are not eligible to adopt a pet")
        
age=int(input ("enter your age in number: "))
living_situvation=input ("enter your living place (house, apartment) : ")

print (check_pet_adoption_eligibility(age, living_situvation))
