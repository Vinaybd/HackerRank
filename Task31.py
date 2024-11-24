# Enter your code here. Read input from STDIN. Print output to STDOUT
# You are given a string S .
# Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

import sys
from itertools import permutations

for line in sys.stdin.readlines():
    m, n = line.split()
    
str = sorted(permutations(m, int(n)))
for i in str:
    print(''.join(i))