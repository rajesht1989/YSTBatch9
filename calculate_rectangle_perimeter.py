def calculate_rectangle_perimeter(length , width ):
    formula = 2*(length+width)
    return formula 
    
user_length_value=int(input("Enter your length value is : "))
user_width_value=int(input("Enter your width value is : "))

print("It os your rectangle perimeter : ",calculate_rectangle_perimeter(length=user_length_value, width=user_width_value))
