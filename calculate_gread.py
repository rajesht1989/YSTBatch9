def calculate_gread(score1,score2,score3):
    avg = (score1+score2+score3)/3
    print(round(avg,1))
    if avg>=90:
        return("gread A")
    elif (80<avg)and(avg<89):
        return("gread B")
    elif (70<avg)and(avg>79):
        return("gread C")
    elif (60<avg)and(avg>69):
        return("great D")
    elif 60<avg:
        return("gread E")
    elif (0>avg)or(100<avg):
        return("invaild score")
    else:
        return("fail")

        
user_value1=int(input("Enter your score1 : "))
user_value2=int(input("Enter your score2 : "))
user_value3=int(input("Enter your score3 : "))
answer=calculate_gread(score1=user_value1,score2=user_value2,score3=user_value3)
print(f"it is your {answer}")
