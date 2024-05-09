import math
def calculate_distance_2d(x1,y1,x2,y2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance
input_value1=int(input("enter your 1number"))
input_value2=int(input("enter your 2number"))
input_value3=int(input("enter your 3number"))
input_value4=int(input("enter your 4number"))
print("final result",calculate_distance_2d(x1=input_value1,y1=input_value2,x2=input_value3,y2=input_value4))