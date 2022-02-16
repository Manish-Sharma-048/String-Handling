'''
Write a Python program to find the second most repeated word in a given string.
'''

string = input("Enter string: ")
count = 1
string = string.lower()

li = string.split(" ")
li2 = []

for i in li:
    if i in li:
        count = li.count(i)
        if count >= 2:
            li2.append(i)
            
if len(li2)>=2:
    print(li2[1], "is the second word that is repeating")
elif len(li2)<1:
    print("There is no word repeating")
else:
    print(li2[0], "is the only word that is repeating, there is no second repeating word")
