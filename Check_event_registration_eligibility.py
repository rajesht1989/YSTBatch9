def check_event_registration_eligibility(age, event_type):
    if (18>=age)and(event_type=="adult_event"):
        return("you are not eligible to register adult event")
    else :
        return ("you are eligible for register to event")
age=int(input ("enter your age in number: "))
event_type=input ("enter event type (child_event,adult_event):")
print ( check_event_registration_eligibility(age, event_type))
