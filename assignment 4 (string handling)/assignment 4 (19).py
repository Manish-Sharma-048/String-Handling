'''
Write a Python program to sort a string lexicographically.
'''

string = input("Enter the string: ")

li = string.split()
li.sort()

for i in li:
    print(i)
