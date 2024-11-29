# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
Data = namedtuple('Data',input())
sp = [Data(*input().split()) for i in range(N)]
print(f"{sum([int(i.MARKS) for i in sp])/N:.2f}")