def check_voting_eligibility(age, is_citizen):
    
    if(age>=18)and(is_citizen=="true"):
        return ("you are eligible to vote")
    else:
        return ("you are not eligible to vote")

age=int(input ("enter your age in number:"))
is_citizen=input ("you are a citizen,say true or false :")

print (check_voting_eligibility(age, is_citizen))
