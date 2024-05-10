def check_leap_year(year):
    if year%4==0:
        return("Leap year ")
    else:
        return("not leap year ")
        
user_value=int(input("Enter your year is : "))
        
calculate_year=check_leap_year(year=user_value)
year=str(user_value)
print(year+" is a ",calculate_year)
