'''
Write a Python function to insert a string in the middle of a string.
'''

string1 = input("Please enter the string: ")
string2 = input("Please enter the string you wish to insert in middle: ")

slen = int(len(string1)/2)

part1 = string1[:slen]
part2 = string1[slen:]

print(part1 + string2 + part2)
