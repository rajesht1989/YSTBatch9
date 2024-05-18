def convert_temperature(Celcius): 
    fahrenheit=((9/5)*Celcius)+32
    return fahrenheit
celcius=float(input("enter the value:"))
print ("The temperature in Fahrenheit is:",convert_temperature(Celcius=celcius))
