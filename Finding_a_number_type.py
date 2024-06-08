def finding_numbertype(number):
    if number>0:
        if number%2==0:
            return ("this is even number ")
            if number>100:
                return ("this number is above 100")
            else:
                return ("no")
        else:
            return ("this is odd number")
    elif number==0:
        return ("This is zero ")
    else:
        return ("this is negative number" )
number=int(input ("enter the number: "))
print(finding_numbertype(number))
