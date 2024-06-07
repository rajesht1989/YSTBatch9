def calculate_employee_bonus(years_of_service, performance_rating):
    if (years_of_service>0)and(years_of_service<5)and(performance_rating==4)or(performance_rating==5):
        return("They receive a bonus of $1000")
    elif (years_of_service>=5)and(performance_rating==4)or(performance_rating==5):
        return("They receive a bonus of $2000")
    else:
        return("The employee does not receive a bonus")
try:
    user_years_of_service = int(input("Enter your service year : "))
    if user_years_of_service<0:
        raise ValueError("service year is not negative")
    user_performance_rating = int(input("Enter your performance rating 4 and 5 : "))
    if  user_performance_rating not in (4,5):
        raise ValueError("your performance rating in 4 and 5")
    result=calculate_employee_bonus(years_of_service = user_years_of_service , performance_rating =  user_performance_rating)
    print(result)
except Exception as e:
    print("something woring",e)
