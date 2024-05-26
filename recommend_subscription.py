def recommend_subscription(age,preferred_genre):
    if age<18:
        return("Student subscription")
    elif (age>=18)and(preferred_genre=="jazz")or(preferred_genre=="classical"):
        return("premium plus")
    elif (age>=18)and(preferred_genre=="pop")or(preferred_genre=="rock")or(preferred_genre=="hip hop"):
        return("premium")
    else:
        return("not accept")
input_age=int(input("Enter your age : "))
input_preferred_genre=input("Enter a song you like : ")
print(recommend_subscription(age=input_age,preferred_genre=input_preferred_genre))