'''
Write a Python program to capitalize first and last letters of each word of a given string.
'''

string = input("Enter string: ")

string = string.strip()

li = string.split(" ")
li2 = []
join = " "

if len(string)<=2:
    print(string.upper())
elif len(string)>2:
    for i in li:
        word = str(i)
        w1 = i[0:1]
        w2 = i[1:-1]
        w3 = i[-1::1]
        word = w1.upper()+w2+w3.upper()
        li2.append(word)

if len(li2) > 1:
    join = join.join(li2)
print(join)
