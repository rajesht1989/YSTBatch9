def calculat_rectangular_prism_volume(length,width,height):
    rectangular_prism_value=length*width*height
    return rectangular_prism_value
    
length_input_value=int(input("enter the length value : "))
width_input_value=int(input("enter the width value : "))
height_input_value=float(input("enter the height value : "))
   
print ("calculat rectangular prism volume is : ",calculat_rectangular_prism_volume(length=length_input_value,width=width_input_value,height=height_input_value))
