def  check_car_rental_eligibility(age, car_type):
    if (age<20):
        return("They are not eligible to rent a \"luxury\" car")
    else:
        return(" they are eligible to rent any type of car.")
try:
    user_age=int(input("Enter your age : "))
    if user_age<0:
        raise ValueError("Age is cannot be negative")
    user_car_type=input ("Enter your value in (economy/standard/luxury) : ")
    if user_car_type not in ("economy","standard","luxury"):
        raise ValueError("your car type is enter on economy/standard/luxury ")
    result = check_car_rental_eligibility(age=user_age,car_type=user_car_type)
    print(result)
except Exception as e:
    print("something wrong",e)
