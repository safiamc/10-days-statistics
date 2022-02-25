#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    val_list = []
    for val, freq in zip(values, freqs):
        val_list.extend([val]*freq)
    sorted_list=sorted(val_list)
    length = len(sorted_list)
    if length%2==0:
        L = sorted_list[:length//2]
        U = sorted_list[length//2:]
    else:
        L = sorted_list[:length//2]
        U = sorted_list[length//2+1:]
    print(float(median(U)-median(L)))
    
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
