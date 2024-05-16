def calculate_pyramid_volume(base_area, height):
    volume=((1/2)*(base_area*height))
    return volume
Base=float(input ("enter length:"))

Height=float(input ("enter height:"))
result=calculate_pyramid_volume(base_area=Base, height=Height)
print ("Volume of the Pyramid is ;",result)
