def check_learner_permit_eligibility(age, has_license):
    if (age>=16) and (has_license=="True"):
        return ("They are eligible to apply for learner permit ")
    elif (16<age)and(age<18) and (has_license=="False"):
        return ("dose not have a valid driver license they ")
    elif(age>0)and(age<16):
        return ("They are not eligible for a learnar permit with parental consent ")
    else:
        return ("invalid age and license")
        
user_age=int(input("Enter your age : "))
user_has_license=str(input("Enter your has license say True or False : "))
result = check_learner_permit_eligibility(age = user_age, has_license = user_has_license)
print(f"learner permit eligibility {result}")
