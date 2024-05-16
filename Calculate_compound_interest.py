def calculate_compound_interest(p,t,r):
    compound_interest=p*((1+r/100)**t)-p
    return compound_interest
principal_amount=int(input ("enter the amount : "))
interest_r=float(input ("enter the interest rate % :  "))
time=int(input ("enter the year : "))
result=calculate_compound_interest(p=principal_amount,t=time,r=interest_r)
print ("compound interest is", result)