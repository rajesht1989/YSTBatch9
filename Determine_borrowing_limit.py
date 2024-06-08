def determine_borrowing_limit(age, library_card_type):
    
    if(18>age):
        return ("you can borrow up to 5 books")
    
    elif(18<=age)and(library_card_type=="basic"):
        return ("you can borrow up to 3 books")
        
    elif(18<=age)and(library_card_type=="premium"):
        return ("you can borrow up to 7 books")
        
    else:
        return ("you can't borrow books ")
        
age=int (input ("enter your age in number: "))
library_card_type=input ("what is your librarycard type (basic, premium) : ")

print (determine_borrowing_limit(age, library_card_type))
