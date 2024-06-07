def determine_meal_options(age, is_vegetarian):
    if (0<=age)and(10>age):
        return("They can only order from the kids menu")
    elif (age>=10)and(is_vegetarian=="True"):
        return("They can choose from the vegetarian menu")
    elif (age>=10)and(is_vegetarian=="False"):
        return("They can choose from the regular menu")
    else:
        return("invaild determine meal options")
        
try:
    user_age = int(input("Enter your age : "))
    if user_age<0:
        raise ValueError("Age is cannot be a negative")
    user_is_vegetarian = input("you are vegetarian or not vegetrian is say only (True/False) : ").capitalize()
    if user_is_vegetarian not in ("True","False"):
        raise ValueError("you are enter a value in True or False")
    result=determine_meal_options(age = user_age, is_vegetarian=user_is_vegetarian)
    print(result)
except Exception as e:
    print("something wrong",e)
