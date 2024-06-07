def determine_borrowing_limit(age, library_card_type):
    if (0<age<18):
        return("they can borrow up to 5 books.")
    elif (age>=18)and(library_card_type=="basic"):
        return(" they can borrow up to 3 books.")
    elif (age>=18)and(library_card_type=="premium"):
        return("they can borrow up to 7 books.")
    else:
        return("invalid borrowing limit")
try:
    user_age=int(input("Enter your age : "))
    if user_age<0:
        raise ValueError("Age is cannot be negative ")
    user_card = input("Enter your library card tybe in (basic/premium) : ")
    if user_card not in ("basic","premium"):
        raise ValueError("Enter your library card type in basic or premium")
    result=determine_borrowing_limit(age=user_age, library_card_type=user_card)
    print(result)
except Exception as e:
    print("something wrong ",e)
