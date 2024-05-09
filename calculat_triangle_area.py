import math 
def calculat_triangle_area(a,b,c):
    sum=(a+b+c)/2
    Area = .sqrt((sum* (sum - a)) * (sum - b) * (sum - c))
    return Area
    
a_value_input=int(input("enter the a value : "))
b_value_input=int(input("enter the b value : "))
c_value_input=int(input("enter the c value : "))

print ("triangle area value is : ",calculat_triangle_area(a=a_value_input,b=b_value_input,c=c_value_input))
