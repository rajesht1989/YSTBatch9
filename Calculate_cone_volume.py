def calculate_cone_volume(radius, height):
    volume=(1/3)*3.14*(radius**2)*height 
    return volume 
Radius=float(input ("enter the value:"))
Height=float(input ("enter the value:"))
result=calculate_cone_volume(radius=Radius, height=Height)
print ("Volume of the cone is:", result)
