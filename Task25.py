#!/bin/python3
#Capitalize the first letter of name

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(" ")  #splits by only single space
    new_str = ""
    
    for i in range(len(words)):
        new_str += words[i].lower().capitalize()
        new_str += ' '
    
    return new_str
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input("Enter your input :")

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
