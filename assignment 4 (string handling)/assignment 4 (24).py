'''
Write a Python program to reverse words in a string.
'''

string = input("Enter the string: ")
word = input("Please enter the word whose reverse you wish to see: ")
string1 = string.lower()
word1 = word.lower()

if word1 in string1:
    word = word[::-1]
    print("The reverse of requested word is: ",word)
else:
    print("The word is not present.")
