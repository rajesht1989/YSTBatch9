def calculate_bmi(weight,height ):
    BMI=weight/height**2
    return BMI
    
    
    
user_weight=float(input ("Enter your weight in kg : "))
user_height=float(input ("Enter your height in meters: "))
print("BMI value:",calculate_bmi(weight=user_weight, height=user_height))
