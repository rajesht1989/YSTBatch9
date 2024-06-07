def calculate_final_price(product_price, is_loyalty_cardholder):
    if (product_price>=50) and (is_loyalty_cardholder=="True"):
        return(" they receive a 10% discount.")
    elif (product_price>=100):
        return("they receive a $20 discount.")
    else:
        return("invalid final price")
try:
    user_price=int(input("Enter your prodect price : $"))
    if user_price<0:
        raise ValueError("price is cannot be negative ")
    user_loyalty=input("Enter your loyalty cardholder in (True/False) : ").capitalize()
    if user_loyalty not in ("True","False"):
        raise ValueError("Enter your value in only True/False")
    result = calculate_final_price(product_price=user_price, is_loyalty_cardholder=user_loyalty)
    print(result)
except Exception as e:
    print("something wrong",e)
