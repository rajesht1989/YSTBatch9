def  recommend_health_insurance_plan(age, smoke_status):
    if (0<age)and(age<30)and(smoke_status=="False"):
        return("Recommend the \"Baise\" plan")
    elif (age>=30)and(smoke_status=="True"):
        return("Recommend the \"Standard\" plan")
    elif (smoke_status=="True"):
        return( "recommend the \"Premium\" plan regardless of age")
    else:
        return("invalid recommend health insurance plan")
try:
    user_age = int(input("Enter your age : "))
    if user_age<0:
        raise ValueError(" Age is cannot be negative ")
    user_smoke_status = input("you\'r smokeing and not smokeing say (True/False) : ").capitalize()
    if user_smoke_status not in ("True","False"):
        raise ValueError("you\'r smokeing in say True you\r not smoke in say False")
    result=recommend_health_insurance_plan(age = user_age, smoke_status = user_smoke_status)
    print(result)
except ValueError as va:
    print("ValueError",va)
except Exception as e:
    print("something Error",e)
