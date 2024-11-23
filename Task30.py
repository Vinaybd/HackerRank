# Raghu is a X shoe shop owner. His shop has  number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money  earned


# Enter your code
# X = input() # number of shoes
# shoeSizes = Counter(list(map(int, input().split())))
# N = int(input())
# total = 0
# for _ in range(N):
#     customer = list(map(int, input().split()))
#     try:
#         shoseSize = shoeSizes[customer[0]]
#         if shoeSizes[customer[0]] > 0:
#             total += customer[1]
#             shoeSizes[customer[0]] -= 1
#     except:
#         pass

# print(total)

import sys
from collections import Counter
arr = []
for line in sys.stdin.readlines():
    i = line.split()
    arr.append(i)

shoes = Counter(arr[1])
n = int(arr[2][0])
values = 0
for i in range(n):
    if arr[i+3][0] in shoes:
        if shoes[arr[i+3][0]] > 0:
            values += int(arr[i+3][1])
            shoes[arr[i+3][0]] -= 1
        
print(values)