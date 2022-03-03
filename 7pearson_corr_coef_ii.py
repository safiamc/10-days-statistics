# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import mean
n = int(input().strip())
data_X = list(map(float, input().rstrip().split()))
rank_X = {x:i for (i,x) in enumerate(sorted(data_X))}
data_Y = list(map(float, input().rstrip().split()))
rank_Y = {y:i for (i,y) in enumerate(sorted(data_Y))}
squared_diff = [(rank_X[x]-rank_Y[y])**2 for (x,y) in zip(data_X, data_Y)]
print(round(1-(6*sum(squared_diff))/(n*(n**2-1)),3))
