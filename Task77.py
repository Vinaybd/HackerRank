import re
N=int(input())
for i in range(N):
    num=input()
    if len(num)<10:
        print('NO')
    else:
        pattern=r"^[789][0-9]{9}$"
        
        if bool(re.match(pattern,num))==True:
            print('YES')
        else:
            print('NO')

# Sample Input/Output
# 2
# 9587456281
# 1252478965