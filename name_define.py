def name_define(a):
    if a=="Vishwa":
        return("you are allowed")
    elif a=="Sanjay":
        return("you are allowed")
    elif a=="Vijay":
        return("you are allowed")
    elif a=="Chanduru":
        return("you are allowed")
    else:
        return("you are not allowed")
input_name=input("Enter your name : ")
print(name_define(a=input_name))