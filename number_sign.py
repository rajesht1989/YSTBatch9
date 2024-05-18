def number_sign(num):
    if num>0:
        return ("it is positive number ")
    elif num==0:
        return ("it is zero ")
    else:
        return ("it is negative number ")
Number=int(input ("enter a number: "))
print (number_sign(num=Number))
