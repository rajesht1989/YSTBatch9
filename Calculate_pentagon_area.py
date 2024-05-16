import math 
def calculate_regular_pentagon_area(side_length):
    area=(1/4)*(math.sqrt(5*(5+2*math.sqrt(5) )))*(side_length)
    return area
length=float (input ("enter the value :"))
result=calculate_regular_pentagon_area(side_length=length)
print ("Area of the Pentagon is:", result)
