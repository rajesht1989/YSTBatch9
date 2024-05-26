def recommend_subscription(age, preferred_genre):
    if (age<=18)and(preferred_genre=="comedy"):
        return("Don")
    elif (age<=18)and(preferred_genre=="romance"):
        return("96")
    elif (age>=18)and(preferred_genre=="action"):
        return ("Leo")
    elif (age>=18)and(preferred_genre=="horror"):
        return("Kanchana")
    else:
        return("You are not eligible for watch the movie")
input_age=int(input("Enter your age : "))
input_preferred_genre=input("Enter your movie : ")
print(recommend_subscription(age=input_age,preferred_genre=input_preferred_genre))