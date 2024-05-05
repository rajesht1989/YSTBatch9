def line_1(name,age,):
    user1 = name,age
    return user1
    
def line_2(a,b,x):
    users = a**2+(a+b)*x+a*b
    return users

num1=input("what is your name? :")
num2=int(input("what is your age? :"))
num3=int(("first number :"))
num4=int(input("second number :"))
num5=int(input("fainal number :"))
call_1 = line_1(name=num1,age=num2)
print("your detail :",call_1)
call_2 = line_2(a=num3,b=num4,x=num5)
print("expactad result :",call_2)