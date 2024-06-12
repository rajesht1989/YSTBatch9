#write a program to get the string from the user and find occurrence letters on the values

def findoccurrenceletters(string,letter):
    count = 0
    for i in string:
        if i == letter:
            count += 1
    return count
string=input("enter a line or  word : ")
letter=input("enter a letter : ")
print(findoccurrenceletters(string,letter))
