#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n_pos = 0
    n_neg = 0
    for e in arr:
        if e > 0: 
            n_pos += 1
        elif e < 0:
            n_neg += 1
    n_zero = len(arr) - n_pos - n_neg
    print(f"{n_pos/len(arr):.6f}\n{n_neg/len(arr):.6f}\n{n_zero/len(arr):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
