def bonus_calculation(service_year, salary ):
    if service_year>5:
        return ("you will get bonus",0.05*bonus)
    else :
       return  ("you will not get bonus")
service_year=int(input("enter the number :"))
salary =float(input ("enter your  salary:"))
print (bonus_calculation(service_year, salary ))
