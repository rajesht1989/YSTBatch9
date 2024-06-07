def  recommend_movie_rating(age, accompanied_by_adult):
    if (0>age<12):
        return("Recommend a G or PG movie")
    elif (12<age<17)and(accompanied_by_adult=="True"):
        return("Recommend a PG-13 movie")
    elif (12<age<17)and(accompanied_by_adult=="False"):
        return("Recommend a PG movie")
    elif (age>=18):
        return("They can watch any movie")
    else:
        ("invalid movie rating")
try:
    user_age=int(input("Enter your age : "))
    if user_age<0:
        raise ValueError("Age is cannot be negative")
    user_adult=input("your adult can you enter for (True/False)  : ").capitalize()
    if user_adult not in ("True","False"):
        raise ValueError("Enter only value for (True/False)")
    result = recommend_movie_rating(age=user_age, accompanied_by_adult=user_adult)
    print(result)
except Exception as e:
    print("something worning",e)
