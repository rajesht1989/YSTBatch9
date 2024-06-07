def classify_school_grade(grade_level):
    if (1<=grade_level )and(grade_level<=5):
        return ("Elementary School")
    elif (6<=grade_level)and(grade_level<=8):
        return ("Middle School")
    elif (9<=grade_level)and(grade_level<=12):
        return ("High School")
    else:
        return ("Invalid Grade Level")

try:
    user_grade_level = int(input("Enter your in (1-12) : "))
    if not (1<=user_grade_level<=12):
        raise ValueError(" Grade level is 1-12 so you enter a number is 1-12 and no enter the negative number ")
    result = classify_school_grade(grade_level=user_grade_level)
    print(result)
except ValueError as va:
    print("ValueError",va)
except TypeError as ty:
    print("TypeError",ty)
except NameError as na:
    print("NameError",na)
except Exception as e:
    print("something wrong",e)
