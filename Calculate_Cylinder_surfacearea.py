def calculate_cylinder_surface_area(radius,height):
  surface_area=(2*3.14*(radius**2))+(2*3.14*radius*height)
  return surface_area
value1=float(input("enter the value:"))
value2=float(input ("enter the value:"))
result=calculate_cylinder_surface_area(radius=value1,height=value2)
print ("Cylindet Surface area:",result)
