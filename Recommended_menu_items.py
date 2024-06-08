def recommend_menu_item(age, caffeinated):
    if(1<=age<18):
        return ("recommend to Hot Chocolate")
    elif(18<=age):
        if(caffeinated=="yes"):
            return ("recommend to caffeinated coffee")
        else:
            return ("recommend to Decaf coffee")
    else:
        return ("enter correct details ")

age=int(input ("enter your age in number : "))
caffeinated=input ("you like caffeinated coffee,say yes or no :")
print (recommend_menu_item(age, caffeinated))
