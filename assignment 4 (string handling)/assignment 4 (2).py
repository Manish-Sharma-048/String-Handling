'''
Write a Python program to count the number of characters (character frequency) in a string.  
Sample String : google.com'

Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

string = "google.com"
li = list(string)
li2 = []

for i in li:
    if i not in li2:
        li2.append(i)

for i in li2:
    if i in string:
        print(i,':',string.count(i))
