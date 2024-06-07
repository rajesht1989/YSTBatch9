def categorize_age_group(age):
    if (0<=age)and(age<=12):
        return ("Child")
    elif (13<=age)and(age<=19):
        return ("Teenager")
    elif (20<=age)and(age<=59):
        return ("Adult")
    elif (age>=60):
        return ("senier")
    else:
        return ("Invalid Age")

try:
    user_age = int(input("Enter your age: "))
    if user_age<0:
        raise ValueError("Age cannot be negative ")
    result = categorize_age_group(user_age)
    print(result)
except ValueError as va:
    print("Invalid input Please enter a valid integer for age.",va)
except NameError as na:
    print("NameError",na)
except Exception as e:
    print("something worng please chack your input")
