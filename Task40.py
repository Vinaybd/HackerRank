# Enter your code here. Read input from STDIN. Print output to STDOUT

# The first line contains integers n and m  separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, a  and b , respectively.

f_line = input().split()
n = f_line[0]
m = f_line[1]
integers = input().split()
A = set(input().split())
B = set(input().split())

h = 0
for i in integers:
    if i in A:
        h += 1
    elif i in B:
        h -= 1
print(h)

# input
# 3 2
# 1 5 3
# 3 1
# 5 7

# output
# 1