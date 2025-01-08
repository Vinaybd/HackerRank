# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int,input().split(" "))
l = []
for _ in range(x):
    l.append(list(map(float,input().split(" "))))
for n in zip(*l):
    print(f"{(sum(n)/len(n)):.1f}")


#Sample input
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5