#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
MOD = int(1e9 + 7)

def legoBlocks(n, m):
    # Write your code here
    pers = [0 for i in range(m + 1)]
    totals = [1 for i in range(m + 1)]
    bad = [0 for i in range(m + 1)]
    good = [0 for i in range(m + 1)]
    pers[1:5] = [1, 2, 4, 8]
    for i in range(5, m + 1):
        pers[i] = (pers[i - 1] + pers[i - 2] + pers[i - 3] + pers[i - 4]) % MOD
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            totals[i] = (totals[i] * pers[i]) % MOD
    
    for i in range(1, m + 1):
        for j in range(1, i + 1):
            bad[i] = (bad[i] + (good[j] * (bad[i - j] + good[i - j])) % MOD) % MOD
        good[i] = (totals[i] - bad[i] + MOD) % MOD
    return good[m]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
