def  recommend_menu_item(age, caffeinated):
    if (0<age<18):
        return(" recommend \"Hot Chocolate\".")
    elif (age>=18)and(caffeinated=="True"):
        return(" recommend \"Espresso\".")
    elif (age>=18)and(caffeinated=="False"):
        return(" recommend \"Decaf Coffee\".")
    else:
        return("invalid menu item")
try:
    user_age=int(input("Enter your age : "))
    if user_age<0:
        raise ValueError("Age is cannot be negative")
    user_caffe=input("Enter your caffeinated value in (True/False) : ").capitalize()
    if user_caffe not in ("True","False"):
        raise ValueError("Enter your caffeinated value in (True/False)")
    result=recommend_menu_item(age=user_age, caffeinated=user_caffe)
    print(result)
except Exception as e:
    print("something wrong",e)
