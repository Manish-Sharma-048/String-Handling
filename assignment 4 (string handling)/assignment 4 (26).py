'''
Write a Python program to count repeated characters in a string.  
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
'''

string = "thequickbrownfoxjumpsoverthelazydog"
occ = 0
a = 'o', 'e', 'u', 'h', 'r', 't', 'end'

for i in range(len(string)):
    if a[i] != 'end':
        if(a[i] in string):
            occ = string.count(a[i])
            print(a[i], occ)
    else:
        break
