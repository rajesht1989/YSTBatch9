def calculat_cylinder_surface_area(radius,height):
    surface_area=(2*3.14*radius**2)+(2*3.14*radius*height)
    return surface_area
    
radius_input_value=int(input("enter the radius value : "))
height_input_value=float(input("enter the height value : "))

print ("the calculat cylinder surface area value is : " ,calculat_cylinder_surface_area(radius=radius_input_value,height=height_input_value))
