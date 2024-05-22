def ticket_offers(age):
    if age>0:
        if age>=50:
            return("25$")
        elif age>=40:
            return("15$")
        elif age>=30:
            return("10$")
        elif age>=18:
            return("5$")
        else:
            return("You are not eligible")
    else:
        return("Your age is not accepted")
input_age=int(input("Enter your age : "))
print(ticket_offers(age=input_age))