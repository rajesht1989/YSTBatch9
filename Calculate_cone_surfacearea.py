def calculate_cone_surface_area(radius, slant_height):
    surface_area=((3.14*radius)*(radius+slant_height))
    return surface_area
Radius=float(input("enter the Value:"))
Height=float(input("enter the Value:"))
result =calculate_cone_surface_area(radius=Radius, slant_height= Height)
print("Surface area of the Cone is:", result)
