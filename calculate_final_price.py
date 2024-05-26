def calculate_final_price(total_price,num_book):
    if total_price>=50:
        return("10% offer for you")
    elif num_book>=5:
        return("10$ offer for you")
    else:
        return("No offer")
input_num_book=int(input("Enter your number of books : "))
input_total_price=int(input("Enter your total price : "))
print(calculate_final_price(total_price=input_total_price,num_book=input_num_book))