def password_define(numbers):
    if numbers=="1234":
        return("Your password accepted")
    elif numbers=="vishwa":
        return("Your password accepted")
    else:
        return("Your password not accepted")
input_password=input("Enter your password : ")
print(password_define(numbers=input_password))
        
        