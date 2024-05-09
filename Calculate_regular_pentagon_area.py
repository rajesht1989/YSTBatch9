import math
def calculate_regular_pentagon_area(s):
    area=(1/4)*math.sqrt((5)*(5+2*math.sqrt(5)))*s**2
    return area
input_number=int(input("Enter your number : "))
print("Final result : ",calculate_regular_pentagon_area(s=input_number))
