def calculate_bmi_category(height_cm,weight_kg):
    BMI =weight_kg/height_cm**2
    print(BMI)
    if (BMI>0)and(BMI<18.5):
        return("unter weight ")
    elif (BMI>18.5)and(BMI<24.9):
        return(" Normul weight ")
    elif (BMI>25.0)and(BMI<29.9):
        return("Over weight ")
    elif (BMI>=30.0):
        return("Obese")
    else:
        return("invalid BMI")
        
user_height=float(input("Enter your height in cm  : "))
user_weight=float(input("Enter your weight in kg : "))
result=calculate_bmi_category(height_cm=user_height,weight_kg=user_weight)
print(f"that is your BMI value is : {result}")
