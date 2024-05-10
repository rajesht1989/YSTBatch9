import math

def calculate_reguler_pentagen_area(s):
    reguler_pentagen_area = (1/4)*math.sqrt(5*((5+2)*math.sqrt(5)))*s**2
    return reguler_pentagen_area

user_value1 = float(input("Enter your s value : "))

print("The triangle area is:", calculate_reguler_pentagen_area(s=user_value1))
