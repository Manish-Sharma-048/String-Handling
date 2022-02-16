'''
Write a Python program to check whether a string starts with specified characters
'''

string = input("Enter the string: ")
char = input("Please enter the character you wish to check: ")

if string.startswith(char):
    print("The string starts with following char: ",char)
else:
    print("The string doesn't start with this char: ", char)

