

# You have a non-empty set s, and you have to execute N commands given in N lines.

# The commands will be pop, remove and discard.


n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    command_line = input().split()
    command, elem = (command_line[0], int(command_line[1]) if len(command_line)==2 else None)
    
    if command == "discard":
        s.discard(elem)
    else:
        try:
            if command == "remove":
                s.remove(elem)
            if command == "pop":
                s.pop()
        except KeyError:
            pass
print(sum(s))

# Sample input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5