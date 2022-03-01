# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import comb
def Cumulative_df(n, k, p):
    cumulative_sum=0
    for i in range(k+1):
        cumulative_sum += comb(n,i)*(p**i)*((1-p)**(n-i))
    return cumulative_sum
    
p=0.12
print(round(Cumulative_df(10,2,0.12),3))
print(round(1-Cumulative_df(10,1,0.12), 3))
