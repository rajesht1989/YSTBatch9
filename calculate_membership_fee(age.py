def calculate_membership_fee(age, membership_type):
    if (0<age)and(age<18):
        return "They get a 50% discount on both membership types."
    elif membership_type == "Standard":
        return "Costs $20 per month."
    elif membership_type == "Premium":
        return "Costs $40 per month."
    else:
        return "Invalid membership type."

try:
    user_age = int(input("Enter your age: "))
    if user_age < 0:
       raise ValueError("Age cannot be negative.")
    user_membership_type = input("Enter membership type (standard/premium): ").capitalize()
    if user_membership_type not in {"Standard","Premium"}:
        raise ValueError("invalid membership type.")
    
    result = calculate_membership_fee(age=user_age, membership_type=user_membership_type)
    print(result)
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Exception:", e)
