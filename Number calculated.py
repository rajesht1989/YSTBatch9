def clrsen(a,b,x):
    users = x**2+(a+b)*x+a*b
    return users
    
num1=int(input("firt num :"))
num2=int(input("second num :"))
num3=int(input("fainal num :"))
print("expactad result",clrsen(a=num1,b=num2,x=num3))
