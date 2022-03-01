from statistics import NormalDist
print(round((1-NormalDist(mu=70, sigma=10).cdf(80))*100,2))
print(round((1-NormalDist(mu=70, sigma=10).cdf(60))*100,2))
print(round(NormalDist(mu=70, sigma=10).cdf(60)*100,2))
