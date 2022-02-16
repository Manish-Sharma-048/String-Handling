'''
Write a Python program to find the maximum occurring character in a given string.
'''

string = input("Enter string: ")
string2 = string.replace(" ","")
string2.lower()
l = list(string2)
str = set(l)
ct = []

for i in str:
    cout = l.count(i)
    ct.append(cout)
for i in str:
    if max(ct) == l.count(i):
        print(max(ct),":",i)
