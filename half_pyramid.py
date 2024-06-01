def half_pyramid(number):
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")
input_number=int(input("Enter your number : "))
half_pyramid(number=input_number)