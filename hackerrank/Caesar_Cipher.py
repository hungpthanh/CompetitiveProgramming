#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    result = ""
    k = k % (int (len(alphabet) / 2))
    for c in s:
        if not (c.lower() in alphabet):
            result += c
            continue
        if ord(c) >= ord('a'):
            result += alphabet[ord(c) - ord('a') + k]
        else:
            result += alphabet[ord(c.lower()) - ord('a') + k].upper()
    return result
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
