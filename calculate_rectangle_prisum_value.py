def calculate_rectangle_prisum_value(L,W,H):
    formula = L*W*H
    return formula 
    
length_value=int(input("Enter your length value is : "))
width_value=int(input("Enter your width value is : "))
height_value=float(input("Enter your height value is : "))
 
 
print("It is your rectangle prisum value : " , calculate_rectangle_prisum_value(L=length_value,W=width_value,H=height_value))
