def cut_of_mark(biology, chemistry, physics):
    formula =((chemistry+physics)/2)+biology 
    return formula 
    
    
biology_mark = int(input("your biology mark : "))
chemistry_mark = int(input("your chemistry mark : "))
physics_mark = int(input("your physics mark : "))
print("It os your cut of marks  :  ",cut_of_mark(biology=biology_mark, chemistry=chemistry_mark, physics=physics_mark))
