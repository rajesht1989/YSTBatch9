pen = 100
pencile = 100
eraser = 100
for i in range(0,2):
    n=input().capitalize()
    if n == "Pen":
        print("pen quandity in : " , pen)
    elif n == "Pencile":
        print("pencile quandity in : " ,pencile)
    elif n == "Eraser":
        print("Eraser quandity in : ",eraser)
        break
    else:
        continue
