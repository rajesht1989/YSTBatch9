import math

def calculate_triangle_area(a, b, c):
    s = (a+b+c)/2
    triangle_area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return triangle_area

user_value1 = int(input("Enter your a value : "))
user_value2 = int(input("Enter your b valueb: "))
user_value3 = int(input("Enter your c value : "))

print("The triangle area is:", calculate_triangle_area(a=user_value1, b=user_value2, c=user_value3))
