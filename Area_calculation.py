def calculate_circlearea (radius):
    area=3.14*radius**2
    return area
given_radius=float(input ("enter the radius :"))
result=calculate_circlearea (radius=given_radius)
print("Area of the circle is :", result)
