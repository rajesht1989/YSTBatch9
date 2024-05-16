def calculate_cylinder_volume(radius, height):
    volume=(3.14*(radius**2)*height) 
    return volume 
Radius=float(input ("enter the value:"))
Height=float(input ("enter the value:"))
result=calculate_cylinder_volume(radius=Radius, height=Height)
print ("Volume of the cone is:", result)
