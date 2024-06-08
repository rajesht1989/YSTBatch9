def check_car_rental_eligibility(age, car_type):
    if (age<=25)and(car_type=="economy"):
        return ("you are eligible to select economy type car")
    elif(age<=25)and(car_type=="standard"):
        return ("you are eligible to select standard type  car")
    elif(age<=25)and(car_type=="luxury"):
        return ("you are not eligible to select luxury car")
        
    elif(age>=25)and(car_type=="economy"):
        return ("you are eligible to select economy type car")
        
    elif(age>=25)and(car_type=="standard"):
        return ("you are eligible to select standard type  car")
    elif(age>=25)and(car_type=="luxury"):
        return ("you are eligible to select luxury car")
        
    else:
        ("enter correct details ")

age=int(input ("enter your age in number:"))
car_type=input ("enter car type (economy, standard, luxury ) : ")
print (check_car_rental_eligibility(age, car_type))
