def check_scholarship_eligibility(score, attendance_percentage):
    if (score>=90)and(85<=attendance_percentage):
        return ("They are eligible for the full scholarship ")
    elif (score>80)and(89>score)and(80<=attendance_percentage):
        return ("They are eligible for the partial scholarship ")
    elif (score<80)and(80>attendance_percentage):
        return ("Not eligible for scholarship ")
    else:
        return ("invalid score and attendance percentage ")
       
user_score=float(input("Enter your score "))
user_attendance=float(input("Enter your attendance value in percentage "))
result=check_scholarship_eligibility(score = user_score, attendance_percentage=user_attendance)
print(result)
