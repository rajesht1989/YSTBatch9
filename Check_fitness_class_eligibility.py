def check_fitness_class_eligibility(age, class_type):
    
    if (0<age<16)and(class_type=="yoga"):
        return ("they are eligible to enroll in yoga classes")
        
    elif (0<age<16)and(class_type=="pilates"):
         return ("they are eligible to enroll in pilates classes")
         
    elif (0<age<16)and(class_type=="crossfit"):
         return ("they are not eligible to enroll in crossfit classes")

    if (age>=16)and(class_type=="yoga"):
        return ("they are eligible to enroll in yoga classes")
        
    elif (age>=16)and(class_type=="pilates"):
         return ("they are eligible to enroll in pilates classes")
         
    elif (age>=16)and(class_type=="crossfit"):
         return ("they are eligible to enroll in crossfit classes")
         
    else:
        return ("enter correct datails")
        
age=int(input ("enter your age in number: "))
class_type=input ("enter your class type (yoga, pilates,crossfit) : ")

print (check_fitness_class_eligibility(age, class_type))
