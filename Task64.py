# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    a = int(input())
    A = set(input().split())
    b = int(input())
    B = set(input().split())
                    
    print(A.issubset(B))

# Sample input
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2