def colors_define(color):
    if color=="red":
        return("STOP")
    elif color=="yellow":
        return("READY")
    elif color=="green":
        return("GO")
    else:
        return("This color was not accepted")
input_name=input("Enter your color : ")
print(colors_define(color=input_name))