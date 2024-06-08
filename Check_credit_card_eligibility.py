def check_credit_card_eligibility(annual_income, credit_score):
    if((annual_income>=50000)and (credit_score>=700)):
        return ("they are eligible for apply a credit card")
    elif (annual_income<=50000)and (credit_score>=650):
        return ("they are eligible for apply a credit card")
    else :
        return ("they are not eligible for apply credit card")
annual_income=int(input ("enter your annual_income in numbers : "))
credit_score=int(input("enter your credit_score in numbers : "))
print (check_credit_card_eligibility(annual_income, credit_score))
