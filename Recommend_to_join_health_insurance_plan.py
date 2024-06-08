def recommend_health_insurance_plan(age, smoke_status):
    if (0<age<30)and(smoke_status=="False"):
        return ("recommend to you are join Basic plan")
    elif (30<=age<=50)and(smoke_status=="False"):
        return ("recommend to you are join Standard plan")
    elif (50<age):
        return ("recommend not to join any plans")
    else:
        return ("recommend to you are join Premium plan")
        
age = int( input ("enter your age in number: "))
smoke_status=input ("enter your smoke status,say True or False :")
print (recommend_health_insurance_plan(age, smoke_status))
