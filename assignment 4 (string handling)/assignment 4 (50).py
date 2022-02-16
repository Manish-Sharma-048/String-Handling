'''
WAP which read the string and print only vowel characters of entered string on computer screen.
'''

string = input("Please enter the string: ")

string1 = string.lower()

for i in range(len(string1)):
    if string1[i] == 'a'or string1[i] == 'e'or string1[i] == 'i'or string1[i] == 'o'or string1[i] == 'u':
        print(string[i], "is a vowel")
    else:
        pass

