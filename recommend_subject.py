def  recommend_subject(grade_level):
    if (1<=grade_level<=3):
        return("recommend \"Mathematics\".")
    elif (4<=grade_level<=6):
        return("recommend \"Science\".")
    elif (7<=grade_level<=9):
        return("recommend \"History\".")
    elif (10<=grade_level<=12):
        return(", recommend \"Literature\".")
    else:
        return("invalid subject")
try:
    user_grade_level=int(input("Enter your grade level in 1-12 : "))
    if not 1<=user_grade_level<=12 :
        raise ValueError("Grade level is enter in the 1-12")
    result=recommend_subject(grade_level=user_grade_level)
    print(result)
except Exception as e:
    print("something wrong",e)
