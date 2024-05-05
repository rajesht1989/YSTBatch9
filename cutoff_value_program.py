def cut_of_mark(maths, chemistry, physics):
    formula =((chemistry+physics)/2)+maths
    return formula 
    
    
maths_mark = int(input("your maths mark : "))
chemistry_mark = int(input("your chemistry mark : "))
physics_mark = int(input("your physics mark : "))
print("It os your cut of marks  :  ",cut_of_mark(maths=maths_mark, chemistry=chemistry_mark, physics=physics_mark))
