def age_qualification(age):
    if ((age>=10) and (age<=18)):
        return("Allowed")
    else:
         return("Not allowed")
input_age=int(input("Enter your age : "))
print(age_qualification(age=input_age))
 