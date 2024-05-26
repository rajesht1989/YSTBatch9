def recommend_travel_package(destination,budget):
    if (destination=="beach")and(budget>=3000):
        return("Beach resort package")
    elif (destination=="mountain")and(budget>=6000):
        return("Mountain resort package")
    elif (destination=="city")and(budget>=9000):
        return("City resort package")
    else:
        return("Not accepted")
input_destination=input("Enter your destination : ")
input_budget=int(input("Enter your budget : "))
print(recommend_travel_package(destination=input_destination,budget=input_budget))