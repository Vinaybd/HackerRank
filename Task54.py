# Enter your code here. Read input from STDIN. Print output to STDOUT
# The input consists of three lines. The first line contains the integer N,
# denoting the length of the list. The next line consists of  space-separated lowercase English letters, 
# denoting the elements of the list.
# The third and the last line of input contains the integer N , 
# denoting the number of indices to be selected.

from itertools import combinations
n = int(input("Enter an number :").strip())
A = tuple( input("Enter an Alphabit(a b c d):").strip().split(" "))
K = int(input("Enter an number:").strip())

B = list(combinations(A,K))
print(len(list(filter( lambda x : "a" in x , B )))/len(B))