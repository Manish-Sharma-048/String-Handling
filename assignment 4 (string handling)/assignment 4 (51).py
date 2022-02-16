'''
WAP that reads a string from keyboard and determine whether the string is palindrome or not.
'''

string = input("Enter the string: ")
count = 0

pal1 = string
pal2 = string[::-1]

for i in range(len(string)):
    if pal1[i] == pal2[i]:
        count = count + 1
        if count == len(string):
            print("This string is a palindrome")
            break
    else:
        print("This string is not a palindrome")
        break
