def calculate_cone_surface_area(radius, slant_height):
    surface_area = 3.14 * radius * (radius+slant_height)
    return surface_area
    
radius_value_input=float(input("enter the radius value : "))
slant_height_input=float(input("enter the slant height value : "))

print ("cone surface area value is : ",calculate_cone_surface_area(radius=radius_value_input, slant_height=slant_height_input))
