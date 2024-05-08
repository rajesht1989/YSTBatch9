def calculat_cone_volume(radius,height):
    cone_volume=(1/3)*3.14*(radius**2)*height
    return cone_volume
    
radius_value_input=float(input("enter the radius value : "))
height_value_input=float(input("enter the height value : "))
 
print ("The calculat cone volume : " ,calculat_cone_volume(radius=radius_value_input,height=height_value_input))
