'''
WAP to find number of occurrences of character ‘o’ in the string entered through keyboard. If the character ‘o’ is not present in the string then show a message “o is not present in the entered string”.
'''

string = input("Please enter the string: ")

if 'o' in string:
    print("'O' is present in the string and appears", string.count("o"),"times")
else:
    print("There is no 'O' in the string.")
