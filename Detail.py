def user_details(name,quality,age):
    result=age+1,name, quality 
    return result 
    
    
user_name = input("Enter your name : ")
user_quality = input("Enter your quality : ")
user_age = int(input("Enter your age  : "))



print("That is your details : ",
user_details(name=user_name, quality=user_quality,age=user_age))
