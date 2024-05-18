def license_eligibility(age):
    if age>=18:
        return("you are eligible for license")
    else:
        return("You are not eligible for license")
input_age=int(input("Entre your age : "))
print(license_eligibility(age=input_age))