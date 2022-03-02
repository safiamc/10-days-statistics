# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import NormalDist
from math import sqrt
mean_point = 2.4
std_point = 2.0
n=100
print(round(NormalDist(mu=n*mean_point, sigma = sqrt(n)*std_point).cdf(250),4))
