def traffic_signal(colour):
    
    if colour=="red":
        return ("stop 🔴")
    
    elif colour=="yellow":
        return ("ready 🟡")
    
    elif colour==("green"):
        return ("go 🟢")
        
    else:
        return ("try again")
        
given_colour=input ("enter a colour : ")

print (traffic_signal(colour=given_colour))
