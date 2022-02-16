'''
Write a Python program to count the occurrences of each word in a given sentence.
'''

st = input("Please enter the string: ").strip()
lt = list(st.split(' '))
se_t = set(st.split(' '))

for i in se_t:
    st1 = lt.count(i)
    print(i+" : "+str(st1))
