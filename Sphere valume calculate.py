def calculate_speare_volume(radius):
    volume=(4/3)*3.14*radius**3
    return volume
given_radius=float(input("enter the radius:"))
result=calculate_speare_volume(radius=given_radius)
print ("The volume of the speare is:", result)
