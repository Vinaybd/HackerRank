# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i . 
# print: Print the list.
# remove e: Delete the first occurrence of integer e . 
# append e: Insert integer e at the end of the list. 
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands 
# where each command will be of the  types listed above. Iterate through each command 
# in order and perform the corresponding operation on your list.





if __name__ == '__main__':
    lst=[ ]
    N = int(input("Enter an input :"))
    for _ in range(N):
    # Read the command
        command = input().strip().split()

    # Check the command type and perform the appropriate operation
        if command[0] == "insert":
             i, e = int(command[1]), int(command[2])
             lst.insert(i, e)
        elif command[0] == "print":
             print(lst)
        elif command[0] == "remove":
             e = int(command[1])
             if e in lst:
                lst.remove(e)
        elif command[0] == "append":
             e = int(command[1])
             lst.append(e)
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            if lst:
               lst.pop()
        elif command[0] == "reverse":
            lst.reverse()