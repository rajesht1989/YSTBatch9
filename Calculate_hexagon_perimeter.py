def calculate_hexagon_perimeter(side_length):
    perimeter=6*side_length
    return perimeter 
length=float(input ("enter the value:"))
result=calculate_hexagon_perimeter(side_length=length)
print ("Perimeter of the Hexagon is:", result)
