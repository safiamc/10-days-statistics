from statistics import NormalDist
print(round(NormalDist(mu=20, sigma=2).cdf(19.5),3))
print(round(NormalDist(mu=20, sigma=2).cdf(22)-NormalDist(mu=20, sigma=2).cdf(20),3))
