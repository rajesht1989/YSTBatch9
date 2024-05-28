def check_fitness_class_eligibility(age,class_type):
    if (age>16)and(class_type=="yoga")or(class_type=="pilates")or(class_type=="crossfit"):
        return("You are eligible for the class")
    elif (age<16)and(class_type=="yoga")or(class_type=="pilates"):
        return("You are eligible for the class")
    elif (age<16)and(class_type=="crossfit"):
        return("You are not eligible")
    else:
        return("This class is not")
input_age=int(input("Enter your age : "))
input_class=input("Enter your class : ")
print(check_fitness_class_eligibility(age=input_age,class_type=input_class))
        
    
        
    