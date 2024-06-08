def findVowels(string):
    vowels=["A","E","I","O","U","a","e","i","o","u"]
    c=0
    for i in string:
        if i in vowels:
            c+=1
            print(i)
    print(c)
string=input("enter a word or line :")
findVowels(string)
