# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

full_string = input().strip()
search_string = input().strip()
l = []
i = 0
while i <= len(full_string):
    string = re.search(search_string , full_string[i:] )
    if(string):
        l.append(tuple([string.start() + i, string.end() - 1 + i]))
        i += int(string.span()[0]) + 1
    else:
        break
[print(x) for x in l] if len(l)!=0 else print("(-1, -1)")


# Sample input
# aaadaa
# aa