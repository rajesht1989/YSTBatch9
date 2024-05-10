def calculate_circle_area(r):
    formula = 3.14*(r**2)
    return formula 
    
    
user_radius=int(input("Enter your radius : "))
print("circle area is : ", calculate_circle_area(r=user_radius))
