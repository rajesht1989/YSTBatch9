import math

def calculat_regular_pentagon_area(side_length):
    pentagon_area=(1/4) * math .sqrt((5 * (5 + 2 * math.sqrt(5))) )* side_length**2
    return pentagon_area
    
length_input_value=int(input("enter the length value : "))

print ("regular pentagon area value is : " ,calculat_regular_pentagon_area(side_length=length_input_value))
