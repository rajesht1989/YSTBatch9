def calculate_cylinder_surface_area(h,r):
    π=3.14
    cylinder_surface_area=(2*π*r**2)+(2*π*r*h)
    return cylinder_surface_area
    
radius=float(input("enter your radius value : "))
height=float(input("enter your height value : "))

print("this is your cylinder surface area : ",calculate_cylinder_surface_area(h=height,r=radius))
