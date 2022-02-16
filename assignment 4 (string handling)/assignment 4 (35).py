'''
Write a Python program to print all permutations with given repetition number of characters of a given string.
'''

from itertools import permutations

perm = [''.join(p) for p in permutations('STACK')]
print(perm)
