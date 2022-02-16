'''
Write a Python program to find the first repeated character in a given string.
'''

string = input("Please enter the string: ")
string1 = string.lower()

for i in range(len(string1)):
        if string1[i] in string1[i+1:]:
            print(string[i], "is the first repeated character.")
            break
        else:
            pass
else:
    print("There is no repeated character")
