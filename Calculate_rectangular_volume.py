def calculate_rectangular_prism_volume(length, width, height):
    volume=length*width*height
    return volume
Length=float(input ("enter length:"))
Width=float(input ("enter width:"))
Height=float(input ("enter height:"))
result=calculate_rectangular_prism_volume(length=Length,width=Width, height=Height)
print ("Volume of the Rectangle is ;",result)
