def calculat_circle_area(radius):
    area=3.14*radius**2
    return area
  
radius_input_value=int(input("enter the radius value : "))
print ("The radius value is : " , calculat_circle_area(radius=radius_input_value))
