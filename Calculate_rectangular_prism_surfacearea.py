def calculate_rectangular_prism_surface_area(length, width, height):
    surface_area=2*((length*width)+(width*height)+(height*length))
    return surface_area
Length=float(input ("enter length:"))
Width=float(input ("enter width:"))
Height=float(input ("enter height:"))
result=calculate_rectangular_prism_surface_area(length=Length,width=Width, height=Height)
print ("Prism Surface area of the Rectangle is ;",result)
