A = set(input().split())
n = int(input())
for i in range(n):
    s = set(input().split())
        
    if(len(s) == len(A)):
        print(False)
        break
    elif(not A.issuperset(s)):
        print(False)
        break
else:
    print(True)


# Sample input
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12