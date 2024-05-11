def calculate_compound_interest(p,r,t):
    compound_interest=p*(1+r/100)**t-p
    return compound_interest
input_1value=int(input("enter your 1number"))
input_2value=int(input("enter your 2number"))
input_3value=int(input("enter your 3number"))

print("final result",calculate_compound_interest(p=input_1value,r=input_2value,t=input_3value))
