#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    ans = 0
    pos = [i - 1 for i in range(len(q) + 1)]
    arr = [i for i in range(1, len(q) + 1)]
    for i in range(len(q)):
        if q[i] - i - 1 > 2:
            print("Too chaotic")
            return
        ans += pos[q[i]] - i
        for j in range(i, pos[q[i]]):
            pos[arr[j]] = j + 1
        for j in range(pos[q[i]], i, -1):
            arr[j] = arr[j - 1]
        arr[i] = q[i]
        pos[q[i]] = i
    print(ans)
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

