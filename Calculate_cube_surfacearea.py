def calculate_cube_surface_area(side_length):
    surface_area=6*(side_length**2)
    return surface_area 
length=float(input ("enter the value:"))
result=calculate_cube_surface_area(side_length=length)
print ("Surface area of the cube is:", result)
