def ball_rate_finder(one_ball_rate, number_of_ball):
    result = one_ball_rate * number_of_ball
    return result
   
finding_value = int(input("One ball rate? : "))
number_of_ball = int(input("Number of balls? : "))

print("Total rate:", ball_rate_finder(one_ball_rate=finding_value, number_of_ball=number_of_ball))