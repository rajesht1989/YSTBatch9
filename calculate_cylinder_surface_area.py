def calculate_cylinder_surface_area(r,h):
    surface_area=(2*3.14)*(r^2+2)*(3.4*r*h)
    return surface_area
    
input_value1=int(input("enter your value1"))
input_value2=int(input("enter your value2"))
print("final result",calculate_cylinder_surface_area(r=input_value1,h=input_value2))
