import math 
def calculat_tetrahedron_volume(side_length):
    volume = (1/6) * (math.sqrt(2 ))* (side_length**3)
    return volume 
    
input_side_length=int(input("enter the side length value : "))

print ("The tetrahedron volume value is : ",calculat_tetrahedron_volume(side_length=input_side_length))
