def calculate_shipping_cost(weight, international):
    if (weight>0)and(weight<=1):
        return("The cost is $5")
    elif (weight>=1)and(weight<=5):
        return("The cost is $10")
    elif (weight>=5):
        return("The cost is $20")
    elif international:
        return("an additional $15 is added to the cost")
    else:
        return ("invaild shipping cost")


try:
    user_weight = float(input("Enter the weight of the package in kilograms: "))
    if user_weight<0:
        raise ValueEror("Weight cannot be negative")
    user_international = input("Is the package being shipped internationally? (True/False): ").capitalize()
    if user_international not in {"True","False"}:
        raise ValueError("invaild your value is (True/False)")
    cost = calculate_shipping_cost(weight = user_weight, international = user_international)
    print(f"The shipping cost is: ${cost}")
except ValueError as ve:
    print("ValueError:", ve)
except TypeError as ty:
    print("TypeError",ty)
except Exception as e:
    print("Something went wrong:", e)
