import math
def calculate_tetrahedron_volume(s):
    volume=(1/6)*math.sqrt(2)*s**3
    return volume
    
input_value=int(input("enter your number"))
print("final result",calculate_tetrahedron_volume(s=input_value))
