'''
Write a Python function to reverses a string if it's length is a multiple of 4.
'''

string = input("Please enter the string: ")

s_len = int(len(string))

if s_len%4 == 0:
    print(string[::-1])
else:
    print("As the entered string is not a multiple of 4 the string cannot be reversed.")
