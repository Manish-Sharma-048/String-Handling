'''
Write a Python program to lowercase first n characters in a string.
'''

string = input("Please enter the string: ")
num = int(input("Please enter the number: "))

string1 = string[:num]
string1 = string1.lower()
print(string1 + string[num:])
