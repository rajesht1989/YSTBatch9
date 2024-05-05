def calculat_bmi(weight,height):
    sum_bmi=weight/height**2
    return sum_bmi
weight_line=float(input("enter the weight : "))
height_line=float(input("enter your height : "))
print ("this a bmi calculat : ",calculat_bmi(weight=weight_line,height=height_line))
