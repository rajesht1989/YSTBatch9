def calculate_movie_ticket_price(age, time_of_day):
    if (0<age)and (age<13):
        return ("They pay $5 regardless of the time of day")
    elif (age>=13) and (time_of_day=="morning"):
        return ("They pay $7")
    elif (age>=13) and (time_of_day=="afternoon"):
        return ("They pay $10")
    elif (age>=13)and (time_of_day=="evening"):
        return ("They pay $12")
    else:
        return ("Invalid movie ticket price")

try:
    user_age = int(input("Enter your age: "))
    if user_age < 0:
        raise ValueError("Age cannot be negative")
    user_time_of_day = input("Enter the time of day (morning/afternoon/evening): ").lower() 
    if user_time_of_day not in { "morning","afternoon","evening" }:
        raise ValueError("invaild time of day")
    
    result = calculate_movie_ticket_price(age=user_age, time_of_day=user_time_of_day)
    print(result)
except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("Something wrong:", e)
