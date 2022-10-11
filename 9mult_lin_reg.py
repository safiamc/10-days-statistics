# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model
m, n = map(int,input().split())
x=[]
y=[]
for i in range(n):
    *coeffs, output = map(float, input().split())
    x.append([*coeffs])
    y.append(output)
lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_
q = int(input())
new_x=[]
for i in range(q):
    new_coeffs = list(map(float,input().split()))
    new_x.append(new_coeffs)
for pred in lm.predict((new_x)):
    print(round(pred,2))
