'''
Write a Python program to get the last part of a string before a specified character.
'''

string = "https://en.wikipedia.org/wiki/Che_Guevara"
li = string.split('/')

print(string)
print("\nThe last part of the string before a specified character (/) is: ",li[-1])
