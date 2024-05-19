def gmail_verification(g):
    if g=="vishwa@5gmail.com":
        return("your id accepted")
    else:
        return("your id not accepted")
def password_verification(p):
    if p=="1234":
        return("your password accepted")
    else:
        return("your password not accepted")
input_id=input("Enter your gmail id : ")
input_password=input("Enter your password : ")
print(gmail_verification(g=input_id))
print(password_verification(p=input_password))