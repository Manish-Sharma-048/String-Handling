'''
WAP to delete all vowel from a sentence of the character length 15. The sentence should be entered through keyboard.
'''

string = input("Enter the string: ")
string1 = string[:15]
string2 = string.lower()
vow = 'a','e','i','o','u'

if len(string1) == 15:
    for i in range(len(string1)):
        if string1[i] in vow:
            pass
        else:
            print(string[i], end = '')
else:
    print("The characters entered are less than 15.")
    
    
