def calculate_museum_ticket_price(age, exhibition_type):
    
    if(0<age<12):
        return ("no pay exhibition tickets ")
        
    elif(12<=age<=18)and(exhibition_type=="regular"):
        return ("you are pay 5$ for regular exhibition ticket")
    
    elif(12<=age<=18)and(exhibition_type=="special"):
        return ("you are pay 10$ for special exhibition ticket")
    
    
    elif(19<=age)and(exhibition_type=="regular"):
        return ("you are pay 10$ for regular exhibition ticket")
        
    elif(19<=age)and(exhibition_type=="special"):
        return ("you are pay 15$ for special exhibition ticket")
        
age= int(input ("enter your age in number : "))
exhibition_type=input ("tell you see the exhibition type(regular, special) : ")
print (calculate_museum_ticket_price(age, exhibition_type))
