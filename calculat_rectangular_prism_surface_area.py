def calculat_rectangular_prism_surface_area(length,width,height):
    surface_area=2 * (length*width + length*height + width*height)
    return surface_area
    
length_input=int(input("enter the lenght value : "))
width_input=int(input("enter the width value : "))
height_input=float(input("enter the height value : "))
print ("calculat rectangular prism surface area value is : " , calculat_rectangular_prism_surface_area(length=length_input,width=width_input,height=height_input))
