import math
def calculate_distance_2d(x1,y1,x2,y2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance
point1=float(input ("enter point x1:"))
point2=float(input ("enter point x2:"))
point3=float(input ("enter point y1:"))
point4=float(input ("enter point y2:"))
result=calculate_distance_2d(x1=point1,y1=point3,x2=point2,y2=point4)
print ("Distance between two lines is:",result)
