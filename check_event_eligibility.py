def check_event_eligibility(age, vaccinated):
    if (age>=12)and(vaccinated=="True"):
        return("They are eligible to attend the event ")
    elif (age>0)and(age<12):
        return("They are eligible to attend the event with parental supervision ")
    elif (age>=12)and(vaccinated=="False"):
        return("They are not eligible to attend the event ")
    else:
        return("invalid age and vaccination ")
        
user_age=int(input("Enter your age : "))
user_vaccinated=str(input("Enter your are vaccinated is say True or False : "))
result = check_event_eligibility(age = user_age, vaccinated = user_vaccinated)
print(type(user_vaccinated))
print(f"This your eligibility  : {result}")
