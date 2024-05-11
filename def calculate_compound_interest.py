def calculate_compound_interest(P,R,T):
    compound_interest=p*(1+r/100)**t-p
    return compound_interest
input_1value=int(input("enter your 1number"))
input_2value=int(input("enter your 2number"))
input_3value=int(input("enter your 3number"))

print("final result",calculate_compound_interest(P=input_1value,R=input_2value,T=input_3value))
