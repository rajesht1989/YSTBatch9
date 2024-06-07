def check_credit_card_eligibility(annual_income, credit_score):
    if (annual_income>50000)and(credit_score>700):
        return("They are eligible for a credit card")
    elif (0<annual_income<50000)and(credit_score>650):
        return("They are eligible for a credit card")
    else:
        (" they are not eligible")
try:
    user_annual_income=int(input("Enter your annual income : $"))
    if user_annual_income<=0:
        raise ValueError("Income value cannot be negative")
    user_credit_score=int(input("Enter your credit : "))
    if user_credit_score<=0:
        raise ValueError("your credit score  value is cannot be negative")
    result = check_credit_card_eligibility(annual_income=user_annual_income,credit_score=user_credit_score)
    print(result)
except Exception as e:
    print("something wrong",e)
