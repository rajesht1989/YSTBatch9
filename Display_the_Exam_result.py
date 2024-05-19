def exam_result(reg_no):
    if reg_no=="6135390":
        return ("""                 +2 Exam Result
                  Muthukumar.S 
                    Total marks = 424
                    Tamil-91
                    English-60
                    Maths-77
                    Computer Science-87
                    Physics-54
                    Chemistry-55""")
    else:
        return ("incorrect number,check your number ")
Reg_number=(input ("enter your register number : ")) 
print (exam_result(reg_no=Reg_number))
