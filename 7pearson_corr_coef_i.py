# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import mean, pstdev
n = int(input().strip())
data_X = list(map(float, input().rstrip().split()))
mean_X=mean(data_X)
std_X=pstdev(data_X, mean_X)
data_Y = list(map(float, input().rstrip().split()))
mean_Y=mean(data_Y)
std_Y=pstdev(data_Y, mean_Y)
print(round(sum([(x-mean_X)*(y-mean_Y) for (x,y) in zip(data_X, data_Y)])/(n*std_X*std_Y),3))
