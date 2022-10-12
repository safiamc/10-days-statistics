# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import NormalDist
from math import sqrt
mean_point = 205
std_point = 15
n=49
print(round(NormalDist(mu=n*mean_point, sigma = sqrt(n)*std_point).cdf(9800),4))
