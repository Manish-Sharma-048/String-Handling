'''
Write a Python program to remove the characters which have odd index values of a given string.
'''

string = input("Please enter the string: ")
odd = 0

for i in range(len(string)):
    if i%2 == 0:
        print(string[i], end = "")
    else:
        odd+=1

print("\n\nTotal number of characters which have odd index value are: ", odd)
