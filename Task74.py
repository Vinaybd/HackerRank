# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
pattern = r'(?<= )(&{2}|\|{2})(?= )'
func = lambda x: 'and' if x.group() == '&&' else 'or'

for _ in range(n):
    print(re.sub(pattern, func, input()))


# Sample input
# 11
# a = 1;
# b = input();
# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.