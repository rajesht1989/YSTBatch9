def Bodmas_rule(num1,num2,num3,num4):
    collaborate_numbers= (num1+num2)-(num3*num4)
    return collaborate_numbers
    
    
user_num1 = int(input("Enter your first number : "))
user_num2 = int(input("Enter your second : "))
user_num3 = int(input("Enter your third  : "))
user_num4 = int(input("Enter your fourth : "))


print("The add number is : ",
Bodmas_rule(num1=user_num1,num2=user_num2,num3=user_num3,num4=user_num4))
