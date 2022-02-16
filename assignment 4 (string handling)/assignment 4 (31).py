'''
Write a Python program to swap comma and dot in a string.  
Sample string: "32.054,23"
Expected Output: "32,054.23"
'''

string = "32.054,23"
string1 = ''

li = list(string)

for i in range(len(li)):
    if li[i] == '.':
        li[i] = ','
    elif li[i] == ',':
        li[i] = '.'

string1 = string1.join(li)

print(string1)
