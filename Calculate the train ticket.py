def calculate_train_ticket_fare(age, is_student):
    if 0<age<12:
        return ("Price of child ticket : 10$ ")
        if is_student=="yes":
            return ("ticket price 20% offer for you ")
        else:
            return ("no offer")
    elif 12<=age:
        return ("Price of adult ticket : 20$ ")
        if is_student=="yes":
            return ("ticket price 20% offer for you")
        else:
            return ("no offer")
    else :
        return ("enter correct age" )
age = int(input("enter your age : "))
is_student=input ("you're a student,say yes or no :")
print  (calculate_train_ticket_fare(age, is_student))
