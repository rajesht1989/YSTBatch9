def calculate_isosceles_triangle_perimeter(a,b):
    perimeter=2*a+b
    return perimeter
input_first_number=int(input("Enter your first number : "))
input_second_number=int(input("Enter your second number : "))
print("Final triangle perimeter : ",calculate_isosceles_triangle_perimeter(a=input_first_number,b=input_second_number))
