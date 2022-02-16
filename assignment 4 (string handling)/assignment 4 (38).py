'''
Write a Python program to find the first repeated word in a given string. 
'''

string = input("Enter string: ")
string = string.lower()
count = 1
li = string.split(" ")

for i in li:
    if i in li:
        count = li.count(i)
        if count >= 2:
            print(i, "is the first repeating word")
            break
else:
    print("There is no word repeating")
