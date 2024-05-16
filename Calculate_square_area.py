def calculate_square_area(side_length):
    area=side_length**2
    return area
length=float(input ("enter the value:"))
result=calculate_square_area(side_length=length)
print ("Area of the square is:", result)
