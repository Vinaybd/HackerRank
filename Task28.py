# Enter your code here. Read input from STDIN. Print output to ST
# You are given a two lists  and A and B. Your task is to compute their cartesian product X.
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.

# Both lists have no duplicate integer elements.


import itertools

# Taking input for list A
A = list(map(int, input("Enter the value:").split()))

# Taking input for list B
B = list(map(int, input("Enter the value:").split()))


cartesian_product = list(itertools.product(A, B))

for pair in cartesian_product:
    print(pair, end=" ")