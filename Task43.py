# Enter your code here. Read input from STDIN. Print output to STDOUT

# You are given a string S.
# Your task is to print all possible combinations, up to size k , of the string in lexicographic sorted order.

from itertools import combinations, chain
S = input("Enter the string (HACK 2):").split()
n = int(S[1])

combs = chain.from_iterable(combinations(sorted(S[0]), i) for i in range(1, n + 1))
for comb in combs:
    print(''.join(comb))