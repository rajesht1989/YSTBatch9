def  calculate_employee_bonus(years_of_service, performance_rating):
    
    if(0<years_of_service<5)and(performance_rating=="4"or"5"):
        return ("you will get bonus :1000$")
        
    elif(years_of_service>=5)and(performance_rating=="4"or"5"):
        return ("you will get bonus :2000$")
            
    else :
       return  ("you will not get bonus")
       
years_of_service=int(input("enter years of service in number :"))
performance_rating=float(input ("enter your  ratings in number:"))
print (calculate_employee_bonus(years_of_service, performance_rating))
