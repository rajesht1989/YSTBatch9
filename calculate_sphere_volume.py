def calculate_sphere_volume(r):
    formula = 4/3*3.14*(r**3)
    return formula 
    
user_radius = int(input("Enter your radius is : "))

print("Enter your sphere volume is : ",calculate_sphere_volume(r=user_radius))
