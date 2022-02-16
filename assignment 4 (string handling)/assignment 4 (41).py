'''
Write a Python program to move spaces to the front of a given string.
'''

string = input("Please enter the string: ")

occ = string.count(" ")

string1 = string.replace(" ", "")

print(occ * " " + string1)
print("Number of space added in front are: ",occ)
