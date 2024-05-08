def calculat_cylinder_volume(radius,height):
    cylinder_volume=3.14*(radius**2)*height
    return cylinder_volume
    
radius_value_input=float(input("enter the radius value : "))
height_value_input=float(input("enter the height value : "))

print ("cylinder volume value is : ", calculat_cylinder_volume(radius=radius_value_input,height=height_value_input))
