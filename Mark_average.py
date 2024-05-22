def marks_average(m,p,c):
    maths=(m+p+c)/3
    if maths>=90:
        return("A grade")
    elif maths>=80:
        return("B grade")
    elif maths>=70:
        return("C grade")
    elif maths>=60:
        return("D grade")
    elif maths>=50:
        return("E grade")
    elif maths>=40:
        return("F grade")
    elif maths>=35:
        return("Pass")
    else:
        return("Fail")
input_first_mark=int(input("Enter your maths mark : "))
input_second_mark=int(input("Enter your physics mark : "))
input_final_mark=int(input("Enter your chemistry mark : "))
print(marks_average(m=input_first_mark,p=input_second_mark,c=input_final_mark))