# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N=int(input())
pattern=r"^[+-]?\d*\.\d+$"

for i in range(N):
    num=input()
    print(bool(re.match(pattern, num)))


# Sample input
# 4
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff