number=[7,34,56,78,110]
num=int(input ("enter a number: "))
if num in number:
    if(0<num<=10):
        print ("the value is low ")
    elif(11<=num<=50):
        print ("the value is medium ")
    elif(51<=num<=100):
        print ("the value is high ")
    elif(num>100):
        print("the value is very high ")
    else:
        print ("enter only positive whole numbers" )
elif(num<0):
    print("enter only positive numbers")
else:
    print ("the number is not in the list")
