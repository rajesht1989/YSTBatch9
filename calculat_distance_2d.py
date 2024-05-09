import math 
def calculat_distance_2d(x1,y1,x2,y2):
    Distance = math.sqrt(((x2 - x1)**2) + (y2 - y1)**2)
    return Distance
    
X_1_value_input=int(input("enter the x1 value : "))
Y_1_value_input=int(input("enter the y1 value : "))
X_2_value_input=int(input("enter the x2 value : "))
Y_2_value_input=int(input("enter the y2 value : "))

print("distance 2d value is : ",calculat_distance_2d(x1=X_1_value_input,y1=Y_1_value_input,x2=X_2_value_input,y2=Y_2_value_input))
