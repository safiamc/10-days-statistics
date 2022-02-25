#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    n=len(arr)
    mean = sum(arr)/n
    diff_list = [(val-mean)**2 for val in arr]
    stdev = (sum(diff_list)/n)**.5
    print(round(stdev,1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
