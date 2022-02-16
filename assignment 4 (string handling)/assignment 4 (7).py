'''
Write a Python function that takes a list of words and returns the length of the longest one.
'''

s1 = input("Please enter the word: ")
s2 = input("Please enter the word: ")
s3 = input("Please enter the word: ")

l1 = len(s1)
l2 = len(s2)
l3 = len(s3)

if (l1 > l2 and l1 > l3):
    if l1 == l2:
        print(s1," and ", s2, "are of same length.")
    print(s1, "is the longest one")
elif (l2 > l1 and l2 > l3):
    print(s, "is the longest one")
else:
    print(s3, "is the longest one")
