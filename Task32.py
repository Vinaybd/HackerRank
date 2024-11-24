# Enter your code here. Read input from STDIN. Print output to STDOUT
# print(*cmath.polar(complex(input())), sep='\n')

# You are given a complex X. Your task is to convert it to polar coordinates.

import cmath

com = complex(input("Enter the value (1+2j) :"))

r, phi = cmath.polar(com)
print(f"{r}\n{phi}")