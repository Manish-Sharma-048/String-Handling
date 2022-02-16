'''
Write a Python program to change a given string to a new string where the first and last chars have been exchanged.  
'''

string = input("Please enter a string value: ")

s1 = string[0:1:1]
s2 = string[-1:-2:-1]
s3 = string[1:-1]

print(s2+s3+s1)
