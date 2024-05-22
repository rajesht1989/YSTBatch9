def employee_money_increment(service):
    if service>0:
        if service>=10:
            return("25,000$")
        elif service>=8:
            return("20,000$")
        elif service>=6:
            return("15,000$")
        elif service>=3:
            return("10,000$")
        else:
            return("No increment")
    else:
        return("Not accepted")
input_year=int(input("Enter your years of services : "))
print(employee_money_increment(service=input_year))