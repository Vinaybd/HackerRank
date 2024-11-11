# Enter your code here. Read input from STDIN. Print output to S

# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.


n, m = map(int, input().split())
sym = 1

for x in range(n):
        if x < n//2:
            print((sym*".|.").center(m,"-"), end="")
            sym += 2
        elif x == n//2:
            print("WELCOME".center(m,"-"), end="")
        else:
            sym -= 2
            print((sym*".|.").center(m,"-"), end="") 
        print("") 