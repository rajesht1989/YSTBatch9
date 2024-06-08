def determine_meal_options(age, is_vegetarian):
    if 0<age<10:
        return("they can only order from the kids menu")
    elif (age>=10) and is_vegetarian=="True":
        return ("they can choose from the vegetarian menu")
    else:
        return ("they can choose from the regular menu")
age = int (input ("enter your age in number:"))
is_vegetarian= input ("you're vegetarian,say True or False:")
print (determine_meal_options(age, is_vegetarian))
