def recommend_subject(grade_level):
    
    if (1<=grade_level<=3):
        return("recommend to Mathematics group")
        
    elif (4<=grade_level<=6):
        return("recommend to Science group")
        
    elif (7<=grade_level<=9):
        return("recommend to History group")
        
    elif (10<=grade_level<=12):
        return("recommend to Literature group")
    
    else:
        return ("enter grade level 1 to 12 the in whole numbers")

grade_level=int(input ("enter your grade level in numbers : "))
    
print (recommend_subject(grade_level))
