import math

def calculate_distance_2D(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

user_value1 = int(input("Enter your x1 value: "))
user_value2 = int(input("Enter your y1 value: "))
user_value3 = int(input("Enter your x2 value: "))
user_value4 = int(input("Enter your y2 value: "))

print("The distance in 2D is:", calculate_distance_2D(x1=user_value1, y1=user_value2, x2=user_value3, y2=user_value4))
