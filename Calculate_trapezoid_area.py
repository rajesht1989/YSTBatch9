def calculate_trapezoid_area(base1, base2, height):
    area=(1/2)*(base1+base2)*height
    return area
base_a=float(input("enter the value:"))
base_b=float(input("entet the value:"))
Height=float(input("enter the value:"))
result=calculate_trapezoid_area(base1=base_a, base2=base_b, height=Height)
print("Area of the Trapezoid is:",result)
