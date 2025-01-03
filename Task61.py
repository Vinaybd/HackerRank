n=int(input(""))
A=set(map(int,input().split()))
N=int(input())
while N>0:
    a=input().split()
    B=set(map(int,input().split()))
    if a[0]=="intersection_update":
        A.intersection_update(B)
    elif a[0]=="difference_update":
        A.difference_update(B)
    elif a[0]=="symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif a[0]=="update":
        A.update(B)
    N-=1
print(sum(A))


# Sample input
# 16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66