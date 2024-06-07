def check_table_availability(num_guests, time_slot):
    if (1<=num_guests<=4)and(time_slot=="lunch"):
        return("they are available tables")
    elif (1<=num_guests<=8)and(time_slot=="dinner"):
        return("they are available tables")
    else:
        return("invalid table availablety")
try:
    user_num=int(input("Enter your guests value in 1-8 : "))
    if not 1<=user_num<=8 :
        raise ValueError("Guests value is only 1-8")
    user_time=input("Enter your time solt in (lunch/dinner) : ")
    if user_time not in ("lunch","dinner"):
        raise ValueError("Enter your time solt in only lunch or dinner")
    result = check_table_availability(num_guests=user_num, time_slot=user_time)
    print(result)
except Exception as e:
    print("something wrong",e)
