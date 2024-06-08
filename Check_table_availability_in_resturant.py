def check_table_availability(num_guests, time_slot):
    
    if(1<=num_guests<=4)and(time_slot=="lunch"):
        return("there are available tables")
        
    elif(1<=num_guests<=8)and(time_slot=="dinner"):
        return("there are available tables")
    else:
        return ("the tables are not available ")

num_guests=int(input ("number of guests : "))
time_slot=input ("enter the time slot (lunch, dinner) : ")
print (check_table_availability(num_guests, time_slot))
