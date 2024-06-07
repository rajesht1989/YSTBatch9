def it_my_detail(name,blood_group,age):
    result=age+100
    group=result,name
    details=group,blood_group
    return details
    
    
your_name=input("enter your name : ")
your_blood_group=input("enter your blood group : ")
your_age=int(input("enter your age : "))
print(it_my_detail(name=your_name,blood_group=your_blood_group,age=your_age))
