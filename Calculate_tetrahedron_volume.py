import math
def calculate_tetrahedron_volume(side_length):
    volume=(1/6)*(math.sqrt (2))*(side_length**3)
    return volume
length= int(input ("enter the value: "))
result=calculate_tetrahedron_volume(side_length=length)
print ("The tetrahedron volume is :", result)
