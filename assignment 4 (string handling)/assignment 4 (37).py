'''
Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.
'''

string = input("Please enter the string: ")
string1 = string.lower()

for i in range(len(string1)):
        if string1[i] in string1[i+1:]:
            print(string[i], "is the first repeated character at index number:", string.index(string[i]))
            break
        else:
            pass
else:
    print("There is no repeated character")

