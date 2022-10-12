#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    num_list=sorted(arr)
    quarts=[]
    n=len(arr)
    m=n//4
    if n %4==0:
        quart_one = int((num_list[m-1]+num_list[m])/2)
        quart_two = int((num_list[2*m-1]+num_list[2*m])/2)
        quart_three = int((num_list[3*m-1]+num_list[3*m])/2)
    elif n%4==1:
        quart_one = int((num_list[m-1]+num_list[m])/2)
        quart_two = num_list[2*m]
        quart_three = int((num_list[3*m]+num_list[3*m+1])/2)
    elif n%4==2:
        quart_one = num_list[m]
        quart_two = int((num_list[2*m]+num_list[2*m+1])/2)
        quart_three = num_list[3*m+1]
    else:
        quart_one = num_list[m]
        quart_two = num_list[2*m+1]
        quart_three = num_list[3*m]
    quarts.extend([quart_one, quart_two, quart_three])
    return quarts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
