'''
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).  
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
'''

string = ["red", "white", "black", "red", "green", "black"]
string.sort()
string1 = []

for i in range(len(string)):
    if string[i] not in string1:
        string1.append(string[i])

print(string)
print(string1)
