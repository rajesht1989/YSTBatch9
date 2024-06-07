def calculate_train_ticket_fare(age, is_student):
    if (age>=20)and(age<=59):
        return "price of adult ticket 20$"
    elif 0 < age < 12:
        return "Price of child ticket: 10$"
    elif is_student:
        return "Price of student ticket 20%"
    else:
        return "enter correct answer"

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    is_student = input("Are you a student? (True/False): ").strip().capitalize()
    if is_student not in ("True", "False"):
        raise ValueError("You must enter either True or False")
    is_student = (is_student == "True")
    print(calculate_train_ticket_fare(age, is_student))
except Exception as e:
    print("Error:", e)
