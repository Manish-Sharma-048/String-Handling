'''
Write a Python program to count occurrences of a substring in a string.
'''

string = input("Please enter the string: ")
char = input("Please enter the character whose occurence you wish to check: ")

string1 = string.lower()
char1 = char.lower()

if char in string1:
    occ = string1.count(char)
    print("Total number of occurence of: '", char,"' in '", string, "' is: ", occ)
else:
    print(char, "is not present")
