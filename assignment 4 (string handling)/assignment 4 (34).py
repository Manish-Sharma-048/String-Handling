'''
Write a Python program to find the first non-repeating character in given string.
'''

string = input("Please enter the string: ")
string1 = string.lower()

for i in range(len(string1)):
    if string1[i] in string1:
        count = string1.count(string1[i])
        if count > 1:
            pass
        else:
            print(string1[i], "it is the first non-repeating character")
            break
else:
    print("There are repetetive characters")
