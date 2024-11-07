# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple 



if __name__ == '__main__':
    n = int(input("Enter a number :"))
    integer_list = map(int, input("Enter a number :").split())
    
    print(hash(tuple(integer_list)))