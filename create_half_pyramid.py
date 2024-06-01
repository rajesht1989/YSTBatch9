def inverted_half_pyramid(number):
    for i in range(number, 0, -1):
        for j in range(1,i + 1):
            print("* ", end="")
        print("\r")
input_number=int(input("Entet your number : "))
inverted_half_pyramid(number=input_number)