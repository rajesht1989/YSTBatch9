def theme_park_admission(age):
    if (age>0)and(age<=12):
        return("get free admission")
    elif(age>=13)and(age<=17):
        return("discounted fee of $ 10 ")
    elif(age>=18):
        return("ragular fee of $ 20 ")
    else:
        return(" invalid age ")
   
        
user_age=int(input("Enter your age : "))
result = theme_park_admission(age=user_age)
print(f"your admission age for{result}")
