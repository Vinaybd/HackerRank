# Enter your code here. Read input from STDIN. Print output to STDOUT
# You are given a string S .
# Your task is to find out whether  S is a valid regex or not.
# works in Pypy 3 but not in Python3
import re

n = int(input("Enter a regex (2) :"))

for x in range(n):
    s = input("Enter an string (#$%):")
    try:
        re.compile(s)
        print("True")
    except re.error:
        print("False")