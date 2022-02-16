'''
Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
'''

string = input("Please enter the string: ")
por = list(string[:4])
a = 0
count = 0

for i in por:
    a = ord(i)
    if a in range(65,91):
        count = count + 1

if count >= 2:
    print(string.upper())
else:
    print(string)
