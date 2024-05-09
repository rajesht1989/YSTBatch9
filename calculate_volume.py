def calculate_cone_volume(r,h):
    volume=(1/3)*3.14*r**2*h
    return volume
value1=int(input("one man heidht"))
value2=int(input("one of the table height"))

print("final result",calculate_cone_volume(r=value1,h=value2))
