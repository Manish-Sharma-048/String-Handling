'''
Write a Python program to check if a string contains all letters of the alphabet.
'''

string = input("Please enter the string: ")

for i in range(len(string)):
    char = ord(string[i])
    if char in range(65,91) or char in range(97,123):
        pass
    else:
        print("String contains special value")
        break
else:
    print("This string contains all characters of the alphabet")

