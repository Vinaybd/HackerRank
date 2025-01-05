# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

dd = defaultdict(int)
mem = int(input())
ll = list(map(int,input().split()))
for v in ll:
    if v in dd.keys():
        dd[v]=dd[v]+1
    else:
        dd[v]=1
                        
for k,v in dd.items():
    if v==1:
        print(k)

# Sample input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 