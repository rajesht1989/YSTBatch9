import math
def calculate_triangle_area(side_a,side_b,side_c):
    area=math.sqrt(s*(s-side_a)*(s-side_b)*(s-side_c))
    return area
side1=int(input ("enter the first value:"))
side2=int(input ("enter the second value:"))
side3=int(input ("enter the third value:"))
s=(side1+side2+side3)/2
result=calculate_triangle_area(side_a=side1,side_b=side2,side_c=side3)
print ("The area of the triangle is:", result)