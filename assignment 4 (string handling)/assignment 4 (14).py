'''
Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).  
Sample function and result : 
insert_end('Python') ->onononon
insert_end('Exercises') ->eseseses
'''

string = input("Please enter the string: ")

if len(string) > 2:
    l_char = string[-2::1]
    print(l_char * 4)
else:
    print("Invalid entry")
