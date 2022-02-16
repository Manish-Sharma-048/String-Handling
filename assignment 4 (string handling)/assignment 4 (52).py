'''
WAP to extract a sub String from a string, values of string and sub string entered through keyboard.
'''

string = input("Please enter the string: ")
start = int(input("Please enter the index number from where you want the sub string to start: "))
end = int(input("till : "))
step = int(input("step : "))

if step == 0:
    step = 1

print("The desired sub string is : ", string[start:end:step])
