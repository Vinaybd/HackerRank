# Enter your code here. Read input from STDIN. Print output to STDOUT

# Perform append, pop, popleft and appendleft methods on an empty deque d.
from collections import deque

lst = deque([])

for _ in range(int(input())):
    eval('lst.{0}({1})'.format(*input().split() + ['']))
    
print(*lst)


# sample input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# output
# 1 2