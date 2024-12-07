# Enter your code here. Read input from STDIN. Print output to STDOUT

# Given  sets of integers, M and N , print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either  or  but do not exist in both.


M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

sorted = sorted(a ^ b)

for i in sorted:
    print(i)