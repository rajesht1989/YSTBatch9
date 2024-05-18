def vote_eligible_age(vote_age):
    if 18<vote_age :
        return ("you are eligible for voting ")
    else:
        return ("you are not eligible for voting" )
vote_age=int(input ("enter your age:"))

print (vote_eligible_age(vote_age=vote_age))
