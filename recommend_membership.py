def recommend_membership(age,preferred_activity):
    if (age<=18)and(preferred_activity=="yoga"):
        return("Yoga senior membership")
    elif (age<=18)and(preferred_activity=="pilates"):
        return("Pilates senior membership")
    elif (age<=18)and(preferred_activity=="crossfit"):
        return("Crossfit senior membership")
    elif (age<=18)and(preferred_activity=="aerobics"):
        return("Aerobics senior membership")
    elif (age>=18)and(preferred_activity=="yoga"):
        return("Yoga junior membership")
    elif (age>=18)and(preferred_activity=="pilates"):
        return("Pilates junior membership")
    elif (age>=18)and(preferred_activity=="crossfit"):
        return("Crossfit junior membership")
    elif (age>=18)and(preferred_activity=="aerobics"):
        return("Aerobics junior membership")
    else:
        return("Not accepted")
input_age=int(input("Enter your age : "))
input_preferred_activity=input("Enter your preferred activity : ")
print(recommend_membership(age=input_age,preferred_activity=input_preferred_activity))