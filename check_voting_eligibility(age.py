def check_voting_eligibility(age, is_citizen):
    if (age>=18)and(is_citizen=="True"):
        return("They are eligible to vote")
    else:
        return("They are not eligible")
try:
    user_age=int(input("Enter your age : "))
    if user_age<0:
        raise ValueError("Age is cannot be negative")
    user_is_citizen=input ("your citizen in say(True/False) : ").capitalize()
    if user_is_citizen not in ("True","False"):
        raise ValueError("your citizen is enter a True/False")
    result=check_voting_eligibility(age=user_age, is_citizen=user_is_citizen)
    print(result)
except Exception as e:
    print("something wrong",e)
