def calculat_isosceles_triangle(base,side_length):
    perimeter = 2 * (side_length+ base)
    return perimeter
    
base_value_input=int(input("enter the base value : "))
side_length_input=int(input("enter the side length value : "))

print ("calculat isosceles triangle value is : ", calculat_isosceles_triangle(base=base_value_input,side_length=side_length_input))
