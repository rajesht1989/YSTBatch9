def calculate_rectangular_prism_surface_area(L,W,H):
    surface_area=2*(L*W+L*H+W*H)
    return surface_area
value1=int(input("enter your number"))
value2=int(input("enter your number"))
value3=int(input("enter your number"))

print("final result",calculate_rectangular_prism_surface_area(L=value1,W=value2,H=value3))
