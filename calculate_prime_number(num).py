def calculate_prime_number(num):
    for i in range(2, num):
        if num%i==0:
            print ("not prime ")
        else:
            print (" it is prime ")
        
        
        
        
calculate_prime_number(5)
