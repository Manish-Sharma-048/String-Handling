'''
Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. 
Sample function and result : 
first_three('ipy') ->ipy
first_three('python') ->pyt
'''

string = input("Please enter the string: ")

if int(len(string)) > 3:
    print(string[:3])
else:
    print(string)
