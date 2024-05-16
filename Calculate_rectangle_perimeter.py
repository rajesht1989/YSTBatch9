def calculate_rectangle_perimetr(length,width):
    perimeter=2*(length+width)
    return perimeter
Length=float(input ("enter length:"))
Width=float(input ("enter width:"))
result=calculate_rectangle_perimetr(length=Length,width=Width)
print ("Perimeter of the Rectangle is ;",result)
