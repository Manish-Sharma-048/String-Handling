'''
Write a Python program to remove duplicate characters of a given string.
'''

string = input("Please enter the string: ")

for i in range(len(string)):
    if string[i] in string:
        count = string.count(string[i])
        if count >=2:
            sring = string.replace(string[i],"")
        else:
            print(string[i], end = "")
