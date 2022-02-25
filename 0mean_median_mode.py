# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from statistics import multimode
n = int(input())
numbers = [int(x) for x in input().split()]
print(np.mean(numbers))
print(np.median(numbers))
print(min(multimode(numbers)))
