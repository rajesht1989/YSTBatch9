def calculat_allipse_area(semi_major_axis,semi_minor_axis):
    ellipse_area=3.14*(semi_major_axis*semi_minor_axis)
    return ellipse_area
    
semi_major_axis_input=int(input("enter the semi major axis value : "))
semi_minor_axis_input=int(input("enter the semi minor axis : "))
print ("the allipse area value is : " , calculat_allipse_area(semi_major_axis=semi_major_axis_input,semi_minor_axis=semi_minor_axis_input))
