def calculate_final_price(product_price, is_loyalty_cardholder):
    
    if(50<=product_price<100)and(is_loyalty_cardholder=="yes"):
        return ("you receive a 10% discount")
        
    elif(product_price>=100):
        return ("you receive a 20% discount")
        
    else:
        return ("you are not eligible for discount")
        
product_price=int(input ("enter product price in number: "))
is_loyalty_cardholder=input ("Are you a loyalty card holder,say yes or no :")

print (calculate_final_price(product_price, is_loyalty_cardholder))
