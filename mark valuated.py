def line_1(name,age,):
    user1 = name,age
    return user1
    
def line_2(a,b,c,d):
    users = a+b+c+d
    return users

num1=input("what is your name? :")
num2=int(input("what is your age? :"))
num3=int(input("your Cprogram mark? :"))
num4=int(input("your java mark? :"))
num5=int(input("your python mark? :"))
num6=int(input("your linux mark? :"))
call_1 = line_1(name=num1,age=num2)
print("your detail :",call_1)
call_2 = line_2(a=num3,b=num4,c=num5,d=num6)
print("expactad result :",call_2)




