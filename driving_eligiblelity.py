def driving_eligiblelity(a,l):
    if a>18:
        if l=="yes":
            return("You are eligible for driving")
        else:
            return("Must have driving license")
    else:
        return("Your age is unacceptable")
input_age=int(input("Enter your age : "))
input_license=input("Do you have a license? : ")
print(driving_eligiblelity(a=input_age,l=input_license))
        