# Task
# The provided code stub reads and integer n, , from STDIN. For all non-negative integers i<n , print i^2.

if __name__ == '__main__':
    n = int(input())
    
    #same using for loop
    for i in range(0 , n):
        print(i*i)
    

    # same using while loop
    i = 0    
    while i<n:
        print(i**2)
        i += 1