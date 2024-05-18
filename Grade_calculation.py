def grade_calculation(mark1,mark2, mark3):
    avg=((mark1+mark2+mark3)/3)
    print(avg)
    if 90<=avg:
        return ("grade A")
    elif 80<=avg:
        return ("grade B")
    elif 70<=avg:
        return ("grade C")
    elif 60<=avg:
        return ("grade d")
    elif 35<=avg:
        return ("grade E")
    else:
        return ("fail")
Mark_1=float (input ("enter the mark1 : "))
Mark_2=float (input ("enter the mark2 : "))
Mark_3=float (input ("enter the mark3 : "))
print (grade_calculation(mark1=Mark_1,mark2=Mark_2,mark3=Mark_3))
