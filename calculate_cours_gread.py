def calculate_cours_gread(midterm_score, final_score):
    overall_gread=(midterm_score+final_score)/2
    if (overall_gread>=60):
        return ('pass')
    else:
        return ('fail')
        
user_value1=float(input("Enter your midterm score in percentage % : "))
user_value2=float(input("Enter your final score in percentage % : "))
final_result=calculate_cours_gread(midterm_score = user_value1, final_score = user_value2)
print(f"overall great is {final_result} ")
