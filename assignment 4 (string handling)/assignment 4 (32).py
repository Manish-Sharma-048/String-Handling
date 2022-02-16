'''
Write a Python program to count and display the vowels of a given text. 
'''

string = input("Please enter the string: ")
string1 = string.lower()
li = ['a','e','i','o','u']
count = 0

for i in range(len(string1)):
    if string1[i] in li:
        print(string[i], "is a vowel")
        count+=1
        
print("Total number of vowels are: ", count)
