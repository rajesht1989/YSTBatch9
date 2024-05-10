def calculate_trapezoid_area(b1,b2,h):
    formula = (1/2)*(b1+b2)*h
    return formula 
    
base1_value=int(input("Enter your base1 value is : "))
base2_value=int(input("Enter your base2 value is : "))
height_value=float(input("Enter your height value is : "))
 
 
print("It is your trapezoidal area value : " , calculate_trapezoid_area(b1=base1_value,b2=base2_value,h=height_value))
