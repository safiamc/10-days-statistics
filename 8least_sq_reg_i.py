# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import mean, pstdev
data_X = [95, 85, 80, 70, 60]
std_X=pstdev(data_X)
data_Y = [85, 95, 70, 65, 70]
std_Y=pstdev(data_Y)
def pearson_corr_coeff(X_array, Y_array):
    mean_X = mean(X_array)
    std_X = pstdev(X_array, mean_X)
    mean_Y = mean(Y_array)
    std_Y = pstdev(Y_array, mean_Y)
    return sum([(x-mean_X)*(y-mean_Y) for (x,y) in zip(data_X, data_Y)])/(len(X_array)*std_X*std_Y)
b_coeff = round(pearson_corr_coeff(data_X, data_Y) * std_Y / std_X,3)
a_coeff = round(mean(data_Y) - b_coeff * mean(data_X),3)
print(round(a_coeff + b_coeff * 80,3))
