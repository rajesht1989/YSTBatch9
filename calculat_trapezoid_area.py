def calculat_trapezoid_area(base1,base2,height):
    trapezoid_area=(1/2)*(base1+base2)*height
    return trapezoid_area
    
Base_input_value_1=int(input("enter the base1 value : "))
base_input_value_2=int(input("enter the base2 value : "))
height_input_value=float(input("enter the height value : "))

print ("The calculat trapezoid area value is : " , calculat_trapezoid_area(base1=Base_input_value_1,base2=base_input_value_2,height=height_input_value))
