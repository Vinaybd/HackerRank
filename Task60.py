# Enter your code here. Read input from STDIN. Print output to STDOUT
# You are given two sets of student roll numbers.
# One set has subscribed to the English newspaper, 
# and one set has subscribed to the French newspaper. 
# Your task is to find the total number of students who have subscribed to either the English
# or the French newspaper but not both.


el = int(input())
e = list(map(int, input().split()))[:el]
fl = int(input())
f = list(map(int, input().split()))[:fl]
print(len(list(set(e).symmetric_difference(f))))


# Sample input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8