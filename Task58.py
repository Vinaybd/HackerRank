# Enter your code here. Read input from STDIN. Print output to STDOUT
# The tool .difference() returns a set with all the elements from the set that are not in an iterable.

el = int(input())
e = list(map(int, input().split()))[:el]
fl = int(input())
f = list(map(int, input().split()))[:fl]
print(len(list(set(e).difference(f))))