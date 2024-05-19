def password_verification(p):
    if p=="vishwa":
        return("your password accepted")
    elif p=="1234":
        return("your password accepted")
    elif p=="@":
        return("your password accepted")
    else:
        return("your password not accepted")
input_password=input("Enter your password : ")
print(password_verification(p=input_password))