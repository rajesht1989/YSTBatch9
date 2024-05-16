def calculate_ellips_area(semi_minor_axis,semi_major_axis):
    area=(3.14*semi_major_axis*semi_minor_axis)
    return area 
minor_axis=float(input ("enter the value:"))
major_axis=float(input ("enter the value:"))
result=calculate_ellips_area(semi_minor_axis=minor_axis,semi_major_axis=major_axis)
print ("Area of the Ellipse:", result)
