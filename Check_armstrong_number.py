def check_armstrong_number(number):
    num=number
    x=0
    while num>0:
        y=num%10
        num=int(num/10)
        x=x+(y**3)
        
    if(number==x):
        print("it is armstrong number ")
    else:
        print("it is not armstrong number ")
number=int(input ("enter the number: "))
check_armstrong_number(number)
