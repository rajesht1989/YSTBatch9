def calculate_prime_number(num):
    if (6*num+1)and(6*num-1):
        return("prime number")
    elif (2*num+1):
        return("composite number")
    else:
        return("invalid code ")
n=int(input())
print(calculate_prime_number(num))
