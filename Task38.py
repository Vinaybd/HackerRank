#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
# def time_delta(t1, t2):
    
#     d_format = "%a %d %b %Y %H:%M:%S %z"

#     time_stamp1 = datetime.strptime(t1, d_format)
#     time_stamp2 = datetime.strptime(t2, d_format)

#     time_dif = time_stamp2 - time_stamp1

#     time_delta_in_seconds = abs(time_dif.total_seconds())

#     return str(int(time_delta_in_seconds))

from datetime import datetime
def time_delta(t1, t2):
    df = '%a %d %b %Y %H:%M:%S %z'
    res = datetime.strptime(t1, df) - datetime.strptime(t2, df)
    return str(abs(int(res.total_seconds())))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
    #     t1 = input()

    #     t2 = input()

    #     delta = time_delta(t1, t2)

    #     fptr.write(delta + '\n')

    # fptr.close()
    
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)  # Print the output instead of writing to a file


#Sample input
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

#Sample output
# 25200
# 88200