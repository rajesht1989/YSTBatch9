def clothing_adivce(temperature,raining):
    if (temperature<10)and(raining==True):
        return(" Wear a heavy coat and take an umbrella. ")
    elif (temperature<10)and(raining==False):
        return(" Wear a heavy coat. ")
    elif (temperature>10)and(temperature<20)and(raining==True):
        return(" Wear a jacket and take an umbrella. ")
    elif (temperature>10)and(temperature<20)and(raining==False):
        return(" Wear a jacket. ")
    elif (temperature>20)and(raining==True):
        return(" Wear light clothes and take an umbrella. ")
    elif (temperature>20)and(raining==False):
        return(" Wear light clothes. ")
    else:
        return(" invaild founction ")

user_temperature=int(input("Enter your temerature"))
