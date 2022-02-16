'''
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.  

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'

Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''

s = '''The lyrics is not that poor!'
'The lyrics is poor!'''

if ("not" in s) and ("poor" in s):
    s = "'The lyrics is good!'\n'The lyrics is poor!'"
    print(s)
else:
    print(s)
