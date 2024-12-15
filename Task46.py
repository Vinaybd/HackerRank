# Enter your code here. Read input from STDIN. Print output to STDOUT
# You are given a string S .
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.
from itertools import combinations_with_replacement as cwr

S, k = input("Enter the input (HACK 2) :").split()
merged = cwr(sorted(S), int(k))

for i in merged:
        print(''.join(i))