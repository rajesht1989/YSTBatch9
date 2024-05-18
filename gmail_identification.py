def gmail_identification(gmail,password):
    if gmail=="vishwa@5gmail.com":
        return("Accepted")
    elif password=="862005":
        return("Accepted")
    else:
        return("Not accepted")
input_gmail=input("Enter your gmail id : ")
input_password=int(input("Enter your password : "))
print(gmail_identification(gmail=input_gmail,password=input_password))
        
        