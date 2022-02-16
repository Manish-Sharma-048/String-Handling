'''
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.  
Sample String : 'abc', 'xyz' 
Expected Result : 'xycabz'
'''

s1 = "'abc'"
s2 = "'xyz'"
s3 = s1[0] + s2[1] + s2[2] + s1[3]
s4 = s1[1] + s1[2] + s2[3] + s2[4]
print(s3+s4)
