def recommend_movie_rating(age,accompanied_by_adult):

    if(0<age<12):
        return ("recommend a G or PG movie")
        
    elif(12<=age<=17)and(accompanied_by_adult=="True"):
        return ("recommend a PG-13 movie")
    
    elif(12<=age<=17)and(accompanied_by_adult=="False"):
        return ("recommend a PG movie")
        
    elif(age>=18):
        return ("they can watch any movie")
    
    else:
        return ("enter correct details ")

age=int(input ("enter your age in number: "))
accompanied_by_adult=input ("you are accompanied by adult,say True or False :")
print ( recommend_movie_rating(age,accompanied_by_adult))
