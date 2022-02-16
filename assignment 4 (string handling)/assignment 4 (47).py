'''
WAP to find whether string entered from keyboard contains the character ‘a’ or not.
'''

string = input("Please enter a string: ")
string1 = string.lower()

if 'a' in string1:
    print("Character 'A' is present in string")
else:
    print("Character 'A' is not present in this string")
