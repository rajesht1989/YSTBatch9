def calculate_cyclinder_volume(r,h):
    volume=3.14*r**2*h
    return volume
number1=int(input("enter your number1:"))
number2=int(input("enter your number2:"))
print("final result:",calculate_cyclinder_volume(r=number1,h=number2))
