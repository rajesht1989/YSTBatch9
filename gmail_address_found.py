def password(your_password):
    if your_password=="KARTHIC@126gmail.com":
        return("login")
    else:
        return ("error")
        
 
value=input("Enter your password in number ")
answer=password(your_password=value)
print("it is password ", answer)