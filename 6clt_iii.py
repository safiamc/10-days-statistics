# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import NormalDist
from math import sqrt
mean_point = 500
std_point = 80
n=100
mean_sample=mean_point
std_sample=std_point/sqrt(n)
A = -1.96*std_sample+mean_sample
B = 1.96*std_sample+mean_sample
print(round(A,2))
print(round(B,2))
