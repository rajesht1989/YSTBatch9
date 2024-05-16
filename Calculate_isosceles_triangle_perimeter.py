def calculate_isosceles_triangle_perimeter(base, side_length):
    area=((2*side_length)+base)
    return area 
Base=float(input ("enter the value:"))
Length=float(input ("enter the value:"))
result=calculate_isosceles_triangle_perimeter(base=Base, side_length=Length)
print ("perimeter of the isosceles Triangle is:", result)
