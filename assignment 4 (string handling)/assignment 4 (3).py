'''
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.  
Sample String : 'restart'
Expected Result : 'resta$t'
'''

x= "restart"
y=x[0]
x=x.replace('r', '$')
x=y+x[1:]
print(x)
