def check_event_registration_eligibility(age, event_type):
    if (age<18)and(event_type=="adult"):
        return("They are not eligible")
    else:
        return ("They are eligible")
try:
    user_age = int(input("Enter your age : "))
    if user_age<0:
        raise("Age is cannot be negative")
    user_event_type = input("Enter the type of event (adult/child) : ")
    if user_event_type not in ("adult","child"):
        raise("you\'r enter a value in (adult or child) ")
    result = check_event_registration_eligibility(age = user_age, event_type=user_event_type)
    print("Registration elgilibility :", result)
except ValueError as e:
    print("ValueError", e)
except Exception as e:
    print("somethhing worning",e)
