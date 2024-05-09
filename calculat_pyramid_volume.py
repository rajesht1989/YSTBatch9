def calculat_pyramid_volume(base_area,height):
    volume=(1/3)*base_area*height
    return volume 
    
base_area_input=int(input("enter the base area value : "))
height_input_value=int(input("enter the height value : "))

print ("pyramind volume value is : ",calculat_pyramid_volume(base_area=base_area_input,height=height_input_value))
