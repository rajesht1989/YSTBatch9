def categorize_age_group (age):
    if 0<age<=12:
        return ("child")
    elif 13<=age<=19:
        return ("teenager")
    elif 20<=age<=59:
        return ("adult")
    elif 60<=age:
        return ("senior")
    else:
        return ("enter positive whole number")
age = int( input ("enter your age : "))
print ( categorize_age_group (age))
