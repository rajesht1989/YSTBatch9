def calculate_cone_volume(r,h):
    π=3.14
    cone_volume=(1/3)*π*r**2*h
    return cone_volume
    
radius=float(input("enter your radius value : "))
height=float(input("enter your height value : "))



print("this is your come volume value :  ",calculate_cone_volume(r=radius,h=height))
