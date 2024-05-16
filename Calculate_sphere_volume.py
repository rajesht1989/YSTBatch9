def calculate_sphere_volume(radius):
    volume=((4/3)*3.14*(radius**3))
    return volume 
given_radius=float(input ("enter the radius :"))
result=calculate_sphere_volume (radius=given_radius)
print("Volume of the sphere is :", result)
