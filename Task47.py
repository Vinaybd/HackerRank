# Enter your code here. Read input from STDIN. Print output to STDOUT

# The first line contains the integer,n .
# The next  n lines each contain a word.
from collections import OrderedDict


ordered_dict = OrderedDict()

n = int(input())

for _ in range(n):
    myinput = input()
    try:
        if ordered_dict[myinput]:
            ordered_dict[myinput] += 1
    except KeyError:
        ordered_dict[myinput] = 1
        
print(len(ordered_dict.items()))
for x,y in ordered_dict.items():
    print(y, end=" ")

# Sample input
# 4
# bcdef
# abcdefg
# bcde
# bcdef