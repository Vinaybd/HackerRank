# Enter your code here. Read input from STDIN. Print output to STDOUT
#intersection
el = int(input())
e = set(list(map(int, input().split()))[:el])
fl = int(input())
f = set(list(map(int, input().split()))[:fl])
print(len(e.intersection(f)))


#Sample input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8