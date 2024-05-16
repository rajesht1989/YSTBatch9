def age_calculation(user_name,user_age):
    ourage=user_name,user_age+6
    return ourage
     
name=input ("enter your name:")
age=int(input("enter your age:"))
result=age_calculation(user_name=name,user_age=age)
    
print(result )
