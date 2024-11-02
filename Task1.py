
# My tried

# Function to check if the number is Weird or Not Weird

def check_weirdness(n):
    if n % 2 != 0:
        return "Weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        return "Not Weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        return "Weird"
    elif n % 2 == 0 and n > 20:
        return "Not Weird"

# Input
n = int(input("Enter a positive integer: ").strip())
# Output
print(check_weirdness(n))



# Code Accepted

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2==1:   #  odd
        print("Weird")
    else:
        if 2<=n<=5:
            print("Not Weird")
        elif 6<=n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")
